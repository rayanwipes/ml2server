# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job_info import JobInfo  # noqa: F401,E501
from swagger_server import util


class JobsData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, jobs: List[JobInfo]=None):  # noqa: E501
        """JobsData - a model defined in Swagger

        :param jobs: The jobs of this JobsData.  # noqa: E501
        :type jobs: List[JobInfo]
        """
        self.swagger_types = {
            'jobs': List[JobInfo]
        }

        self.attribute_map = {
            'jobs': 'jobs'
        }

        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'JobsData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobsData of this JobsData.  # noqa: E501
        :rtype: JobsData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def jobs(self) -> List[JobInfo]:
        """Gets the jobs of this JobsData.


        :return: The jobs of this JobsData.
        :rtype: List[JobInfo]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[JobInfo]):
        """Sets the jobs of this JobsData.


        :param jobs: The jobs of this JobsData.
        :type jobs: List[JobInfo]
        """

        self._jobs = jobs
