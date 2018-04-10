# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_type import DataType  # noqa: F401,E501
from swagger_server import util


class Column(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, column_index: int=None, column_type: DataType=None):  # noqa: E501
        """Column - a model defined in Swagger

        :param column_index: The column_index of this Column.  # noqa: E501
        :type column_index: int
        :param column_type: The column_type of this Column.  # noqa: E501
        :type column_type: DataType
        """
        self.swagger_types = {
            'column_index': int,
            'column_type': DataType
        }

        self.attribute_map = {
            'column_index': 'column_index',
            'column_type': 'column_type'
        }

        self._column_index = column_index
        self._column_type = column_type

    @classmethod
    def from_dict(cls, dikt) -> 'Column':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Column of this Column.  # noqa: E501
        :rtype: Column
        """
        return util.deserialize_model(dikt, cls)

    @property
    def column_index(self) -> int:
        """Gets the column_index of this Column.


        :return: The column_index of this Column.
        :rtype: int
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index: int):
        """Sets the column_index of this Column.


        :param column_index: The column_index of this Column.
        :type column_index: int
        """

        self._column_index = column_index

    @property
    def column_type(self) -> DataType:
        """Gets the column_type of this Column.


        :return: The column_type of this Column.
        :rtype: DataType
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: DataType):
        """Sets the column_type of this Column.


        :param column_type: The column_type of this Column.
        :type column_type: DataType
        """

        self._column_type = column_type
