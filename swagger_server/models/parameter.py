# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.param_type import ParamType  # noqa: F401,E501
from swagger_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, required: bool=None, type: ParamType=None, description: str=None):  # noqa: E501
        """Parameter - a model defined in Swagger

        :param id: The id of this Parameter.  # noqa: E501
        :type id: str
        :param required: The required of this Parameter.  # noqa: E501
        :type required: bool
        :param type: The type of this Parameter.  # noqa: E501
        :type type: ParamType
        :param description: The description of this Parameter.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'id': str,
            'required': bool,
            'type': ParamType,
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'required': 'required',
            'type': 'type',
            'description': 'description'
        }

        self._id = id
        self._required = required
        self._type = type
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Parameter.


        :return: The id of this Parameter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Parameter.


        :param id: The id of this Parameter.
        :type id: str
        """

        self._id = id

    @property
    def required(self) -> bool:
        """Gets the required of this Parameter.


        :return: The required of this Parameter.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required: bool):
        """Sets the required of this Parameter.


        :param required: The required of this Parameter.
        :type required: bool
        """

        self._required = required

    @property
    def type(self) -> ParamType:
        """Gets the type of this Parameter.


        :return: The type of this Parameter.
        :rtype: ParamType
        """
        return self._type

    @type.setter
    def type(self, type: ParamType):
        """Sets the type of this Parameter.


        :param type: The type of this Parameter.
        :type type: ParamType
        """

        self._type = type

    @property
    def description(self) -> str:
        """Gets the description of this Parameter.


        :return: The description of this Parameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Parameter.


        :param description: The description of this Parameter.
        :type description: str
        """

        self._description = description
