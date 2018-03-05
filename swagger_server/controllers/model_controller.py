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
from swagger_server.models.status_array import StatusArray  # noqa: E501
from swagger_server.models.training_response import TrainingResponse  # noqa: E501
from swagger_server import util
from swagger_server.algorithms import wrapper

def create_model(data):  # noqa: E501
    """send model to backend """
    if connexion.request.is_json:
        data = CreateModelData.from_dict(connexion.request.get_json())  # noqa: E50
    model = wrapper.create_model(wrapper.MDL_RANDOM_FOREST)
    wrapper.fit(data, model)
    return jsonify("happy ending coming")


def delete_training(model_id, project_name):  # noqa: E501
    """Forcefully stop training a model. If model has finished training, it deletes the model file in BE.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str

    :rtype: Empty
    """

    return 'do some magic!'


def get_list(project_name):  # noqa: E501
    """Get a list of models inside a given project.

     # noqa: E501

    :param project_name: Project name
    :type project_name: str

    :rtype: StatusArray
    """

    return 'do some magic!'


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
    return 'do some magic!'


def stop_training(model_id, project_name):  # noqa: E501
    """Forcefully stop training an incrementally trained model. The partially trained model will be saved and can be used for predictions.

     # noqa: E501

    :param model_id: Model UUID
    :type model_id: str
    :param project_name: Name of project model is within
    :type project_name: str

    :rtype: Empty
    """
    return 'do some magic!'
