# coding: utf-8

from __future__ import absolute_import
from feed.models.sizes import Sizes
#from django.db.models import Model
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Media(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, display_url: str=None, expanded_url: str=None, id: int=None, id_str: str=None, indices: List[int]=None, media_url: str=None, media_url_https: str=None, sizes: Sizes=None, source_status_id: int=None, source_status_id_str: int=None, type: str=None, url: str=None):
        """
        Media - a model defined in Swagger

        :param display_url: The display_url of this Media.
        :type display_url: str
        :param expanded_url: The expanded_url of this Media.
        :type expanded_url: str
        :param id: The id of this Media.
        :type id: int
        :param id_str: The id_str of this Media.
        :type id_str: str
        :param indices: The indices of this Media.
        :type indices: List[int]
        :param media_url: The media_url of this Media.
        :type media_url: str
        :param media_url_https: The media_url_https of this Media.
        :type media_url_https: str
        :param sizes: The sizes of this Media.
        :type sizes: Sizes
        :param source_status_id: The source_status_id of this Media.
        :type source_status_id: int
        :param source_status_id_str: The source_status_id_str of this Media.
        :type source_status_id_str: int
        :param type: The type of this Media.
        :type type: str
        :param url: The url of this Media.
        :type url: str
        """
        self.swagger_types = {
            'display_url': str,
            'expanded_url': str,
            'id': int,
            'id_str': str,
            'indices': List[int],
            'media_url': str,
            'media_url_https': str,
            'sizes': Sizes,
            'source_status_id': int,
            'source_status_id_str': int,
            'type': str,
            'url': str
        }

        self.attribute_map = {
            'display_url': 'display_url',
            'expanded_url': 'expanded_url',
            'id': 'id',
            'id_str': 'id_str',
            'indices': 'indices',
            'media_url': 'media_url',
            'media_url_https': 'media_url_https',
            'sizes': 'sizes',
            'source_status_id': 'source_status_id',
            'source_status_id_str': 'source_status_id_str',
            'type': 'type',
            'url': 'url'
        }

        self._display_url = display_url
        self._expanded_url = expanded_url
        self._id = id
        self._id_str = id_str
        self._indices = indices
        self._media_url = media_url
        self._media_url_https = media_url_https
        self._sizes = sizes
        self._source_status_id = source_status_id
        self._source_status_id_str = source_status_id_str
        self._type = type
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Media':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Media of this Media.
        :rtype: Media
        """
        return deserialize_model(dikt, cls)

    @property
    def display_url(self) -> str:
        """
        Gets the display_url of this Media.

        :return: The display_url of this Media.
        :rtype: str
        """
        return self._display_url

    @display_url.setter
    def display_url(self, display_url: str):
        """
        Sets the display_url of this Media.

        :param display_url: The display_url of this Media.
        :type display_url: str
        """

        self._display_url = display_url

    @property
    def expanded_url(self) -> str:
        """
        Gets the expanded_url of this Media.

        :return: The expanded_url of this Media.
        :rtype: str
        """
        return self._expanded_url

    @expanded_url.setter
    def expanded_url(self, expanded_url: str):
        """
        Sets the expanded_url of this Media.

        :param expanded_url: The expanded_url of this Media.
        :type expanded_url: str
        """

        self._expanded_url = expanded_url

    @property
    def id(self) -> int:
        """
        Gets the id of this Media.

        :return: The id of this Media.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Media.

        :param id: The id of this Media.
        :type id: int
        """

        self._id = id

    @property
    def id_str(self) -> str:
        """
        Gets the id_str of this Media.

        :return: The id_str of this Media.
        :rtype: str
        """
        return self._id_str

    @id_str.setter
    def id_str(self, id_str: str):
        """
        Sets the id_str of this Media.

        :param id_str: The id_str of this Media.
        :type id_str: str
        """

        self._id_str = id_str

    @property
    def indices(self) -> List[int]:
        """
        Gets the indices of this Media.

        :return: The indices of this Media.
        :rtype: List[int]
        """
        return self._indices

    @indices.setter
    def indices(self, indices: List[int]):
        """
        Sets the indices of this Media.

        :param indices: The indices of this Media.
        :type indices: List[int]
        """

        self._indices = indices

    @property
    def media_url(self) -> str:
        """
        Gets the media_url of this Media.

        :return: The media_url of this Media.
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url: str):
        """
        Sets the media_url of this Media.

        :param media_url: The media_url of this Media.
        :type media_url: str
        """

        self._media_url = media_url

    @property
    def media_url_https(self) -> str:
        """
        Gets the media_url_https of this Media.

        :return: The media_url_https of this Media.
        :rtype: str
        """
        return self._media_url_https

    @media_url_https.setter
    def media_url_https(self, media_url_https: str):
        """
        Sets the media_url_https of this Media.

        :param media_url_https: The media_url_https of this Media.
        :type media_url_https: str
        """

        self._media_url_https = media_url_https

    @property
    def sizes(self) -> Sizes:
        """
        Gets the sizes of this Media.

        :return: The sizes of this Media.
        :rtype: Sizes
        """
        return self._sizes

    @sizes.setter
    def sizes(self, sizes: Sizes):
        """
        Sets the sizes of this Media.

        :param sizes: The sizes of this Media.
        :type sizes: Sizes
        """

        self._sizes = sizes

    @property
    def source_status_id(self) -> int:
        """
        Gets the source_status_id of this Media.

        :return: The source_status_id of this Media.
        :rtype: int
        """
        return self._source_status_id

    @source_status_id.setter
    def source_status_id(self, source_status_id: int):
        """
        Sets the source_status_id of this Media.

        :param source_status_id: The source_status_id of this Media.
        :type source_status_id: int
        """

        self._source_status_id = source_status_id

    @property
    def source_status_id_str(self) -> int:
        """
        Gets the source_status_id_str of this Media.

        :return: The source_status_id_str of this Media.
        :rtype: int
        """
        return self._source_status_id_str

    @source_status_id_str.setter
    def source_status_id_str(self, source_status_id_str: int):
        """
        Sets the source_status_id_str of this Media.

        :param source_status_id_str: The source_status_id_str of this Media.
        :type source_status_id_str: int
        """

        self._source_status_id_str = source_status_id_str

    @property
    def type(self) -> str:
        """
        Gets the type of this Media.

        :return: The type of this Media.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Media.

        :param type: The type of this Media.
        :type type: str
        """

        self._type = type

    @property
    def url(self) -> str:
        """
        Gets the url of this Media.

        :return: The url of this Media.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """
        Sets the url of this Media.

        :param url: The url of this Media.
        :type url: str
        """

        self._url = url

