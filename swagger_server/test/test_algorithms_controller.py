# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.jobs import Jobs  # noqa: E501
from swagger_server.models.model404_error import Model404Error  # noqa: E501
from swagger_server.models.request_suggestion import RequestSuggestion  # noqa: E501
from swagger_server.models.suggest import Suggest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAlgorithmsController(BaseTestCase):
    """AlgorithmsController integration test stubs"""

    def test_jobs(self):
        """Test case for jobs

        List all possible jobs ML supports.
        """
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/jobs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suggest(self):
        """Test case for suggest

        Suggest relevant ML algorithms for a given training set.
        """
        data = RequestSuggestion()
        response = self.client.open(
            '/JH-Project/machine-learning-api/1.0/suggest',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
