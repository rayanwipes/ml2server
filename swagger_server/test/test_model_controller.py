# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_model_data import CreateModelData  # noqa: E501
from swagger_server.models.empty import Empty  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_prediction import GetPrediction  # noqa: E501
from swagger_server.models.model404_error import Model404Error  # noqa: E501
from swagger_server.models.prediction_input import PredictionInput  # noqa: E501
from swagger_server.models.status import Status  # noqa: E501
from swagger_server.models.status_array import StatusArray  # noqa: E501
from swagger_server.models.training_response import TrainingResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModelController(BaseTestCase):
    """ModelController integration test stubs"""

    def test_create_model(self):
        """Test case for create_model

        Start training a machine-learning model with the given model_id.
        """
        data = CreateModelData()
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_training(self):
        """Test case for delete_training

        Forcefully stop training a model. If model has finished training, it deletes the model file in BE.
        """
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models/{project_name}/{model_id}'.format(model_id='model_id_example', project_name='project_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list(self):
        """Test case for get_list

        Get a list of models inside a given project.
        """
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models/{project_name}'.format(project_name='project_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_prediction(self):
        """Test case for get_prediction

        Get a prediction given a model and input data.
        """
        data = PredictionInput()
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models/prediction/{project_name}/{model_id}'.format(model_id='model_id_example', project_name='project_name_example'),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status(self):
        """Test case for status

        Get status of model training.
        """
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models/{project_name}/{model_id}'.format(model_id='model_id_example', project_name='project_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_training(self):
        """Test case for stop_training

        Forcefully stop training an incrementally trained model. The partially trained model will be saved and can be used for predictions.
        """
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/models/stop/{project_name}/{model_id}'.format(model_id='model_id_example', project_name='project_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
