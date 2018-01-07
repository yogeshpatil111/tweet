# coding: utf-8

from __future__ import absolute_import
#from django.db.models import Model
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class URL(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, display_url: str=None, expanded_url: str=None, indices: str=None, url: str=None):
        """
        URL - a model defined in Swagger

        :param display_url: The display_url of this URL.
        :type display_url: str
        :param expanded_url: The expanded_url of this URL.
        :type expanded_url: str
        :param indices: The indices of this URL.
        :type indices: str
        :param url: The url of this URL.
        :type url: str
        """
        self.swagger_types = {
            'display_url': str,
            'expanded_url': str,
            'indices': str,
            'url': str
        }

        self.attribute_map = {
            'display_url': 'display_url',
            'expanded_url': 'expanded_url',
            'indices': 'indices',
            'url': 'url'
        }

        self._display_url = display_url
        self._expanded_url = expanded_url
        self._indices = indices
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'URL':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The URL of this URL.
        :rtype: URL
        """
        return deserialize_model(dikt, cls)

    @property
    def display_url(self) -> str:
        """
        Gets the display_url of this URL.

        :return: The display_url of this URL.
        :rtype: str
        """
        return self._display_url

    @display_url.setter
    def display_url(self, display_url: str):
        """
        Sets the display_url of this URL.

        :param display_url: The display_url of this URL.
        :type display_url: str
        """

        self._display_url = display_url

    @property
    def expanded_url(self) -> str:
        """
        Gets the expanded_url of this URL.

        :return: The expanded_url of this URL.
        :rtype: str
        """
        return self._expanded_url

    @expanded_url.setter
    def expanded_url(self, expanded_url: str):
        """
        Sets the expanded_url of this URL.

        :param expanded_url: The expanded_url of this URL.
        :type expanded_url: str
        """

        self._expanded_url = expanded_url

    @property
    def indices(self) -> str:
        """
        Gets the indices of this URL.

        :return: The indices of this URL.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices: str):
        """
        Sets the indices of this URL.

        :param indices: The indices of this URL.
        :type indices: str
        """

        self._indices = indices

    @property
    def url(self) -> str:
        """
        Gets the url of this URL.

        :return: The url of this URL.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """
        Sets the url of this URL.

        :param url: The url of this URL.
        :type url: str
        """

        self._url = url
