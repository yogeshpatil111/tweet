# coding: utf-8

from __future__ import absolute_import
#from django.db.models import Model
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Hashtags(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, indices: List[int]=None, text: str=None):
        """
        Hashtags - a model defined in Swagger

        :param indices: The indices of this Hashtags.
        :type indices: List[int]
        :param text: The text of this Hashtags.
        :type text: str
        """
        self.swagger_types = {
            'indices': List[int],
            'text': str
        }

        self.attribute_map = {
            'indices': 'indices',
            'text': 'text'
        }

        self._indices = indices
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Hashtags':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Hashtags of this Hashtags.
        :rtype: Hashtags
        """
        return deserialize_model(dikt, cls)

    @property
    def indices(self) -> List[int]:
        """
        Gets the indices of this Hashtags.

        :return: The indices of this Hashtags.
        :rtype: List[int]
        """
        return self._indices

    @indices.setter
    def indices(self, indices: List[int]):
        """
        Sets the indices of this Hashtags.

        :param indices: The indices of this Hashtags.
        :type indices: List[int]
        """

        self._indices = indices

    @property
    def text(self) -> str:
        """
        Gets the text of this Hashtags.

        :return: The text of this Hashtags.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """
        Sets the text of this Hashtags.

        :param text: The text of this Hashtags.
        :type text: str
        """

        self._text = text
