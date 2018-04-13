import connexion
import six
from flask import jsonify
from swagger_server.models.create_model_data import CreateModelData  # noqa: E501
from swagger_server.models.empty import Empty  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_prediction import GetPrediction  # noqa: E501
from swagger_server.models.model404_error import Model404Error  # noqa: E501
from swagger_server.models.prediction_input import PredictionInput  # noqa: E501
from swagger_server.models.status import Status  # noqa: E501
from swagger_server.models.status_data import StatusData  # noqa: E501
from swagger_server.models.status_array import StatusArray  # noqa: E501
from swagger_server.models.training_response import TrainingResponse  # noqa: E501
from swagger_server.models.training_response_data import TrainingResponseData  # noqa: E501
from swagger_server import util
from swagger_server.algorithms import wrapper
from swagger_server.controllers.check_auth import *
from swagger_server.algorithms.client import *
from swagger_server.algorithms.csv_loader import *
from swagger_server.fitter.fitter import *
from swagger_server.controllers.utils import *
from swagger_server.controllers.feature_support import *
from swagger_server.controllers.global_variables import *
import uuid
import datetime
import os
import json


def task_manager_action(f):
    global lock
    global task_manager
    lock.acquire()
    task_manager.remove_finished()
    f(task_manager)
    lock.release()


def create_model(data):  # noqa: E501
    """send model to backend """
    if connexion.request.is_json:
        data = CreateModelData.from_dict(connexion.request.get_json())  # noqa: E50
        (auth_header_value,author_token) = check_auth(connexion.request)

        UUID = uuid.uuid1()

        if not author_token :
            return auth_header_value, 401
            ret = Model404Error("Invalid Job ID","invalid data","Invalid data")
        if not is_in_jobs_list(data.job_id):
            return ret, 404

        data_fname = str(datetime.datetime.now()) + str(data.job_id)

        project_name = data.training_data.project_name
        c = Client()
        response_code = c.request_data(data_fname)

        if response_code == 401:
            return "Error Unauthorised Usage", 401
        elif response_code == 404:
            ret = Model404Error("Invalid file data","File invalid","Invalid file data")
            return ret, 404

        (message,response_code) = c.create_model(str(UUID),"some project name")


        # md = MetaData(json,end_client_things)
        id_to_set = str(datetime.datetime.now()) + str(data.job_id)
        ycolumns = [int(c.column_index) for c in data.output_columns]
        xcolumns = [int(c.column_index) for c in data.input_columns]
        outfile = str(id_to_set) + "_model_" + str(datetime.datetime.now())
        successfile = base_path_to_files + str(id_to_set) + "_succesfile_" + str(datetime.datetime.now())
        jsonfile = base_path_to_files + str(id_to_set) + "_json_file_" + str(datetime.datetime.now())

        # fit = ClassifierFitter(successfile)
        fit = TaskLauncher(successfile)
        metadata = {
        "data": {
            "description": "sample test data",
            "id": id_to_set,
            "percent_trained": "NA",
            "start_time": str(datetime.datetime.now()),
            "started_by": "easter bunny",
            "status": "RUNNING"
            }
        }
        metadata['auth_header_name'] = str(auth_header_value)
        metadata["auth_header_value"] = str(connexion.request.headers[auth_header_value])
        metadata['uuid'] = str(UUID)
        metadata['task_type'] = 'fit'
        metadata['model_out'] = str(outfile)
        metadata['xcolumns'] = str(xcolumns)
        metadata['ycolumns'] = str(ycolumns)
        metadata['datafile'] = str(data_fname)
        metadata['function_name'] = "name"
        metadata['jsonfile'] = str(jsonfile)
        metadata['id_to_set'] = str(id_to_set)
        metadata['task_type'] = "fit"
        metadata['algorithm'] = str(data.job_id)
        if not os.path.exists(base_path_to_files):
            os.makedirs(base_path_to_files)

        with open(str(jsonfile), 'w') as fp:
            json.dump(metadata, fp)

        task_manager_action(lambda tm:
                            tm.add(fit, project_name,UUID,metadata))

        response = TrainingResponseData(str(UUID))
        return TrainingResponse(response),200

def delete_training(model_id, project_name):  # noqa: E501
    """Forcefully stop training a model. If model has finished training, it deletes the model file in BE.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str

    :rtype: Empty
    """

    (auth_header_value,author_token) = check_auth(connexion.request)
    if not author_token :
        return auth_header_value, 401

    c = Client()
    metadata,check_user_authorisation = c.request_model(model_id,project_name,view="Meta")
    if check_user_authorisation == 401:
        return "User is not authorised", 401

    if check_user_authorisation != 404:
        global task_manager
        print("runs")
        task_manager_action(lambda tm:
                            tm.kill_task(
                                tm.get_task_id(
                                               project_name,
                                               model_id)))
        c.delete_model(model_id,project_name)
        c.remove_from_metadata(model_id,project_name)
    else:
        return "model doesn't exist", 404
    # Check in the subshell if the model is there, if so stop the process, and then get the data
    return "Model deleted.", 204

def get_list(project_name):  # noqa: E501
    """Get a list of models inside a given project.

     # noqa: E501

    :param project_name: Project name
    :type project_name: str
    :rtype: StatusArray
    """
    (auth_header_value,author_token) = check_auth(connexion.request)
    if not author_token :
        return auth_header_value, 401

    c = Client()
    metadata,check_user_authorisation = c.get_metadata(project_name)
    if check_user_authorisation == 401:
        return "User is not authorised",401

    if check_user_authorisation != 404:
        list_to_return = []
        for i in metadata:
            metadata,check_user_authorisation = c.get_metadata(i,project_name)
            if check_user_authorisation is 200:
                list_to_return.append(metadata)
        for model in stuff:
            if model.project_name == project_name:
                list_to_return.append(model.metadata)
        return list_to_return,200
    else:
        return "This project does not exist",404

def make_classifier(model_fname):
    model = pickle.load(model_fname)
    tp = type(model)
    if tp in [RandomForestRegressor, RandomForestClassifier]:
        return RandomForests(filename=model_fname)
    elif tp in [SVM.SVC, SVM.SVR]:
        return SupportVectorMachine(filename=model_fname)
    elif tp == naive_bayes.GaussianNB:
        return NaiveBayes(modeltype=NaiveBayes.GAUSSIAN,
                          filename=model_fname)
    elif tp == naive_bayes.BernoilliNB:
        return NaiveByes(modeltype=NaiveBayes.BERNOULLI,
                         filename=model_fname)
    elif tp == naive_bayes.MULTINOMIAL:
        return NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL,
                          filename=model_fname)
    else:
        raise Exception("unable to make classifier from model of type " + str(tp))

def get_prediction(model_id, project_name, data):  # noqa: E501
    """Get a prediction given a model and input data.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str
    :param data: The input data for the model
    :type data: dict | bytes X
    :rtype: GetPrediction
    """
    if connexion.request.is_json:
        data = PredictionInput.from_dict(connexion.request.get_json())  # noqa: E501
        (auth_header_value,author_token) = check_auth(connexion.request)
        if not author_token :
            return auth_header_value, 401

        c = Client()
        metadata,check_user_authorisation = c.request_model(model_id,project_name)
        model_fname,user = c.request_model(model_id,project_name)
        if check_user_authorisation is 401:
            return "User is not authorised",401
        #
        if response_code == 401:
            return "Error Unauthorised Usage", 401
        elif response_code == 404:
            ret = Model404Error("Things broken","File invalid","Invalid file data")
            return ret,404
        input_column = data.input_columns
        # val = input_column[0].column_type
        # train_data = data.training_data
        (filename,response_code) = c.request_data(input_column)
        columns = [int(c.column_index) for c in data.input_columns]
        csv_data = load_csv(filename,columns)

        try:
            clf = make_classifier(model_fname)
        except Exception:
            return "borked",404

        predict_data = clf.predict(csv_data)

        # potentially not here, might just pass the filename, need to train
        # and call the write function at some point
        # also need to add stuff to write the metadata when the model is written

        # wrapper stuff, this doesn't go in the subshell
        return predict_data,200
    return 'do some magic!'

def status(model_id, project_name):  # noqa: E501
    """Get status of model training.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str

    :rtype: Status
    """
    (auth_header_value,author_token) = check_auth(connexion.request)
    if not author_token :
        return auth_header_value, 401

    c = Client()
    metadata,check_user_authorisation = c.request_model(model_id,project_name,view="Meta")
    if check_user_authorisation == 401:
        return "User is not authorised",401
    elif check_user_authorisation == 404:
        ret = Model404Error("This Model Does Not Exist","This Model Does Not Exist","This Model Does Not Exist")
        return ret
    # gotta access the subshell here somehow
    lock.aquire()
    task_manager.remove_finished()
    task_id  = task_manager.get_task_id(project_name,model_id)
    if task_id is not -1:
        # need to use the metadata here when getting a task id
        lock.release()
        return "helloworld",200
    else:
        status = "COMPLETED"
        algorithm_type="NaiveBayesGaussian"
        start_time = "well its a time"
        status_data = StatusData(100,status,"some description stuff",algorithm_type,model_id,start_time,"some person")
        lock.release()
        return Status(status_data),200
    # data = 5
    # # data = subshell.getStuff()
    # if data is None:
    #     if check_use_authorisation is 404:
    #         return "The file/model does not exist" ,404
    #
    #     status = "COMPLETED"
    #     algorithm_type="NaiveBayesGaussian"
    #     start_time = "well its a time"
    #     status_data = StatusData(33,status,"some description stuff",algorithm_type,model_id,start_time,"some person")
    #     return Status(status_data),200
    # else:
    #     status = "RUNNING"
    #     algorithm_type="NaiveBayesGaussian"
    #     start_time = "well its a time"
    #     status_data = StatusData(33,status,"some description stuff",algorithm_type,model_id,start_time,"some person")
    #     return Status(status_data),200

def stop_training(model_id, project_name):  # noqa: E501
    """Forcefully stop training an incrementally trained model. The partially trained model will be saved and can be used for predictions.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str

    :rtype: Empty
    """

    (auth_header_value,author_token) = check_auth(connexion.request)
    if not author_token :
        return auth_header_value, 401

    c = Client()
    metadata,check_user_authorisation = c.request_model(model_id,project_name)
    if check_user_authorisation == 401:
        return "User is not authorised",401

    if check_user_authorisation != 404:
        return "model is not partially trainable", 405
        # check if the user exists in the
        # data_to_upload = 20
        # c.upload_model(model_id,project_name,data_to_upload)
        # c.remove_from_metadata(model_id,project_name)
    else:
        ret = Model404Error("The Model does not exist","Model does not exist","Model does not exist")
        return ret,404
