import connexion
import six
from flask import jsonify
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.jobs import Jobs  # noqa: E501
from swagger_server.models.model404_error import Model404Error  # noqa: E501
from swagger_server.models.request_suggestion import RequestSuggestion  # noqa: E501
from swagger_server.models.suggest import Suggest  # noqa: E501
from swagger_server import util
from swagger_server.algorithm import feature_support

def jobs():  # noqa: E501
    return jsonify(feature_support.jobs)

def suggest(data):  # noqa: E501
    if connexion.request.is_json:
        data = RequestSuggestion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
