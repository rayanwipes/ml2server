import connexion
import six
from flask import jsonify
import json
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.jobs import Jobs  # noqa: E501
from swagger_server.models.jobs_data import JobsData  # noqa: E501
from swagger_server.models.job_info import JobInfo  # noqa: E501
from swagger_server.models.model404_error import Model404Error  # noqa: E501
from swagger_server.models.request_suggestion import RequestSuggestion  # noqa: E501
from swagger_server.models.suggest import Suggest  # noqa: E501
from swagger_server.models.suggest_data import SuggestData  # noqa: E501
from swagger_server.models.suggest_data_jobs import SuggestDataJobs  # noqa: E501
from swagger_server.controllers.feature_support import *
from swagger_server import util
from swagger_server.algorithms.client import *
from swagger_server.algorithms.suggest_algorithm import *
from swagger_server.algorithms.csv_loader import *
from swagger_server.controllers.check_auth import *



def jobs():  # noqa: E501
    (auth_header_value,is_authorised) = check_auth(connexion.request)
    if not is_authorised:
        return auth_header_value, 401
    listData = fetch_list()
    job = Jobs(listData)
    return job,200

def suggest(data):  # noqa: E501
    # deal with header values
    (auth_header_value,is_authorised) = check_auth(connexion.request)
    if not is_authorised:
        return auth_header_value, 401

    if connexion.request.is_json:
        data = RequestSuggestion.from_dict(connexion.request.get_json())  # noqa: E501
        input_column = data.input_columns
        val = input_column[0].column_type
        train_data = data.training_data
        '''
        ID and the project name can be fetched by doing
        train_data.id
        or
        train_data.project_name

        the column individual values can be reached by iterating through the input_column and doing
        input_column[0].column_index
        or
        inpuht_column[0].column_type
        '''
        c = Client()
        (filename,response_code) = c.request_data(input_column)

        if response_code is 401:
            return "Error Unauthorised Usage", 401
        elif response_code is 404:
            ret = Model404Error("Things broken","File invalid","Invalid file data")
            return ret,404

        csv = CSVLoader()
        csv_data = csv.load_csv(filename)

        sug = SuggestAlgorithm()
        '''
        order of the suggest algorithms:
        Naive Bayes Gaussian
        Naive Bayes Multinomial
        Naive Bayes Bernoulli
        Random Forests
        Support Vector Machine
        '''
        ret_list = sug.fit_percentage(csv_data)
        nb_g_score = SuggestDataJobs(nb_g,ret_list[0])
        nb_m_score = SuggestDataJobs(nb_m,ret_list[1])
        nb_b_score = SuggestDataJobs(nb_b,ret_list[2])
        rf_score = SuggestDataJobs(rf,ret_list[3])
        svm_score=  SuggestDataJobs(svm,ret_list[4])

        score_list =[]
        score_list.append(nb_g_score)
        score_list.append(nb_m_score)
        score_list.append(nb_b_score)
        score_list.append(rf_score)
        score_list.append(svm_score)

        sug_data = SuggestData(score_list)
        print(type(sug_data))
        ret_suggest = Suggest(sug_data)
        return ret_suggest,200

    else:
        return "Invalid format of data", 418

    return 'do some magic!'
