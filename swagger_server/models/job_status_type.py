# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class JobStatusType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def __init__(self):  # noqa: E501
        """JobStatusType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'JobStatusType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobStatusType of this JobStatusType.  # noqa: E501
        :rtype: JobStatusType
        """
        return util.deserialize_model(dikt, cls)
