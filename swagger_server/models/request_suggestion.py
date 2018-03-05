# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.column import Column  # noqa: F401,E501
from swagger_server.models.data_input import DataInput  # noqa: F401,E501
from swagger_server import util


class RequestSuggestion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data_file: DataInput=None, input_columns: List[Column]=None, output_columns: List[Column]=None):  # noqa: E501
        """RequestSuggestion - a model defined in Swagger

        :param data_file: The data_file of this RequestSuggestion.  # noqa: E501
        :type data_file: DataInput
        :param input_columns: The input_columns of this RequestSuggestion.  # noqa: E501
        :type input_columns: List[Column]
        :param output_columns: The output_columns of this RequestSuggestion.  # noqa: E501
        :type output_columns: List[Column]
        """
        self.swagger_types = {
            'data_file': DataInput,
            'input_columns': List[Column],
            'output_columns': List[Column]
        }

        self.attribute_map = {
            'data_file': 'data_file',
            'input_columns': 'input_columns',
            'output_columns': 'output_columns'
        }

        self._data_file = data_file
        self._input_columns = input_columns
        self._output_columns = output_columns

    @classmethod
    def from_dict(cls, dikt) -> 'RequestSuggestion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestSuggestion of this RequestSuggestion.  # noqa: E501
        :rtype: RequestSuggestion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_file(self) -> DataInput:
        """Gets the data_file of this RequestSuggestion.


        :return: The data_file of this RequestSuggestion.
        :rtype: DataInput
        """
        return self._data_file

    @data_file.setter
    def data_file(self, data_file: DataInput):
        """Sets the data_file of this RequestSuggestion.


        :param data_file: The data_file of this RequestSuggestion.
        :type data_file: DataInput
        """

        self._data_file = data_file

    @property
    def input_columns(self) -> List[Column]:
        """Gets the input_columns of this RequestSuggestion.


        :return: The input_columns of this RequestSuggestion.
        :rtype: List[Column]
        """
        return self._input_columns

    @input_columns.setter
    def input_columns(self, input_columns: List[Column]):
        """Sets the input_columns of this RequestSuggestion.


        :param input_columns: The input_columns of this RequestSuggestion.
        :type input_columns: List[Column]
        """

        self._input_columns = input_columns

    @property
    def output_columns(self) -> List[Column]:
        """Gets the output_columns of this RequestSuggestion.


        :return: The output_columns of this RequestSuggestion.
        :rtype: List[Column]
        """
        return self._output_columns

    @output_columns.setter
    def output_columns(self, output_columns: List[Column]):
        """Sets the output_columns of this RequestSuggestion.


        :param output_columns: The output_columns of this RequestSuggestion.
        :type output_columns: List[Column]
        """

        self._output_columns = output_columns
