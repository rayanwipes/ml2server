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
from swagger_server.algorithms.backend-client import *
from swagger_server.algorithms.suggest_algorithm import *
from swagger_server.algorithms.csv_loader import *
from swagger_server.controllers.check_auth import *
from swagger_server.controllers.global_variables import *


# FULLY WORKING
def jobs():  # noqa: E501
    (auth_header_value,is_authorised) = check_auth(connexion.request)
    if not is_authorised:
        return auth_header_value, 401
    listData = fetch_list()
    job = Jobs(listData)
    return job,200

# NEEDS FILES FROM CLIENTS
def suggest(data):  # noqa: E501
    # deal with header values
    (auth_header_value,is_authorised) = check_auth(connexion.request)
    if not is_authorised:
        return auth_header_value, 401

    if connexion.request.is_json:
        data = RequestSuggestion.from_dict(connexion.request.get_json())  # noqa: E501
        ip = get_ip()
        c = Client(authHeaderValue,connexion.headers[authHeaderValue],ip)

        # things to pass to Client, not passed yet obvs
        project_name = data.training_data.project_name
        file_id = data.training_data.id
        filename = "suggest_" + str(train_data) + "_"+ str(id) + ".csv"
        # idk if this works but it might
        (response_code,message) = c.requestDataByID(project_name,file_id,filename)

        if response_code == 401:
            return "Error Unauthorised Usage", 401
        elif response_code == 404:
            ret = Model404Error("The file does not exist","File invalid","Invalid file data")
            return ret,404

        csv_data = load_csv_xy(filename, [
            c.column_index for c in data.output_columns
        ], [
            c.column_index for c in data.input_columns
        ])

        sug = SuggestAlgorithm()
        '''
        order of the suggest algorithms:
        Naive Bayes Gaussian
        Naive Bayes Multinomial
        Naive Bayes Bernoulli
        Random Forests
        Support Vector Machine
        '''
        no_rows = n
        ret_list = sug.suggest_algorithms(csv_data, no_rows)
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
