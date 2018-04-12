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
from swagger_server.fitter.fitter import *
import uuid
import datetime


def create_model(data):  # noqa: E501
    """send model to backend """
    global task_manager
    if connexion.request.is_json:
        data = CreateModelData.from_dict(connexion.request.get_json())  # noqa: E50
        (auth_header_value,author_token) = check_auth(connexion.request)
        if not author_token :
            return auth_header_value, 401
        if not is_in_jobs_list(data.job_id):
            ret = Model404Error("Invalid Job ID","invalid data","Invalid data")
            return ret, 404

        c = Client()
        # Some things here potentially to be able to do things
        input_column = data.input_columns
        val = input_column[0].column_type
        train_data = data.training_data
        response_code = c.request_data(input_column)

        if response_code is 401:
            return "Error Unauthorised Usage", 401
        elif response_code is 404:
            ret = Model404Error("Invalid file data","File invalid","Invalid file data")
            return ret, 404

        # potentially not here, might just pass the filename, need to train
        # and call the write function at some point
        # also need to add stuff to write the metadata when the model is written
        #
        # data
        # ->request to the backend
        #
        # -> return 200 "model started training"
        #
        # ->start training
        # model = wrapper.create_model(wrapper.MDL_RANDOM_FOREST)
        # wrapper.fit(data, model)
        # return jsonify("happy ending coming")
        metadata = {
                "data": {
                        "description": "sample test data",
                        "id": "id",
                        "percent_trained": "NA",
                        "start_time": str(datetime.datetime.now()),
                        "started_by": "",
                        "status": "RUNNING"
                        }
                }
        UUID = uuid.uuid1()
        (message,response_code) = c.create_model(str(UUID),"some project name")
        response = TrainingResponseData(str(UUID))

        # md = MetaData(json,end_client_things)
        id_to_set = str(datetime.datetime.now()) + str(data.job_id)
        fname = str(datetime.datetime.now()) + str(data.job_id)
        column_names = [c['column_index'] for c in data['output_columns']]
        column_names += [c['column_index'] for c in data['input_columns']]
        fit = ClassifierFitter(args)
        # await task_manager.add(fit,data['training_data'])

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
    metadata,check_user_authorisation = c.request_model(model_id,project_name)
    if check_user_authorisation is 401:
        return "User is not authorised",401

    if check_user_authorisation is not 404:
        global task_manager
        task_manager.kill_task_uuid(model_id)
        c.delete_model(model_id,project_name)
        c.remove_from_metadata(model_id,project_name)
    else:
        return "model doesn't exists",
    # Check in the subshell if the model is there, if so stop the process, and then get the data


    return "Model deleted.",204

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
    if check_user_authorisation is 401:
        return "User is not authorised",401

    if check_user_authorisation is not 404:
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

def get_prediction(model_id, project_name, data):  # noqa: E501
    """Get a prediction given a model and input data.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str
    :param data: The input data for the model
    :type data: dict | bytes

    :rtype: GetPrediction
    """
    if connexion.request.is_json:
        data = PredictionInput.from_dict(connexion.request.get_json())  # noqa: E501
        (auth_header_value,author_token) = check_auth(connexion.request)
        if not author_token :
            return auth_header_value, 401

        c = Client()
        metadata,check_user_authorisation = c.request_model(model_id,project_name)
        if check_user_authorisation is 401:
            return "User is not authorised",401

        input_column = data.input_columns
        val = input_column[0].column_type
        train_data = data.training_data
        (filename,response_code) = c.request_data(input_column)

        if response_code is 401:
            return "Error Unauthorised Usage", 401
        elif response_code is 404:
            ret = Model404Error("Things broken","File invalid","Invalid file data")
            return ret,404

        # potentially not here, might just pass the filename, need to train
        # and call the write function at some point
        # also need to add stuff to write the metadata when the model is written

        csv = CSVLoader()
        csv_data = csv.load_csv(filename)
        # wrapper stuff, this doesn't go in the subshell
        return "the data is things",200
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
    metadata,check_user_authorisation = c.request_model(model_id,project_name)
    if check_user_authorisation is 401:
        return "User is not authorised",401

    # gotta access the subshell here somehow
    data = 5
    # data = subshell.getStuff()
    if data is None:
        if check_use_authorisation is 404:
            return "The file/model does not exist" ,404

        status = "COMPLETED"
        algorithm_type="NaiveBayesGaussian"
        start_time = "well its a time"
        status_data = StatusData(33,status,"some description stuff",algorithm_type,model_id,start_time,"some person")
        return Status(status_data),200
    else:
        status = "RUNNING"
        algorithm_type="NaiveBayesGaussian"
        start_time = "well its a time"
        status_data = StatusData(33,status,"some description stuff",algorithm_type,model_id,start_time,"some person")
        return Status(status_data),200

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
    if check_user_authorisation is 401:
        return "User is not authorised",401

    if check_user_authorisation is not 404:
        # check if the user exists in the
        data_to_upload = 20
        c.upload_model(model_id,project_name,data_to_upload)
        c.remove_from_metadata(model_id,project_name)
    else:
        return "model doesn't exist",404
    # Check in the subshell if the model is there, if so stop the process, and then get the data


    return "Model training successfully stopped, or had successfully finished before stop call was made.",204
