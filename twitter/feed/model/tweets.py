# coding: utf-8

from __future__ import absolute_import
from feed.models.entities import Entities
from feed.models.users import Users
#from django.db.models import Model
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Tweets(Model):

    def __init__(self, created_at: str = None, entities: Entities = None, id: int = None,
                 id_str: str = None, user: Users = None, text: str = None):

        self.swagger_types = {
            'created_at': str,
            'entities': Entities,
            'id': int,
            'id_str': str,
            'text': str,
            'user': Users
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'entities': 'entities',
            'id': 'id',
            'id_str': 'id_str',
            'text': 'text',
            'user': 'user',
        }

        self._created_at = created_at
        self._entities = entities
        self._id = id
        self._id_str = id_str
        self._text = text
        self._user = user

    @classmethod
    def from_dict(cls, dikt) -> 'Tweets':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tweets of this Tweets.
        :rtype: Tweets
        """
        return deserialize_model(dikt, cls)

    @property
    def created_at(self) -> str:
        """
        Gets the created_at of this Tweets.

        :return: The created_at of this Tweets.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """
        Sets the created_at of this Tweets.

        :param created_at: The created_at of this Tweets.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def entities(self) -> Entities:
        """
        Gets the entities of this Tweets.

        :return: The entities of this Tweets.
        :rtype: Entities
        """
        return self._entities

    @entities.setter
    def entities(self, entities: Entities):
        """
        Sets the entities of this Tweets.

        :param entities: The entities of this Tweets.
        :type entities: Entities
        """

        self._entities = entities

    @property
    def favorite_count(self) -> int:
        """
        Gets the favorite_count of this Tweets.

        :return: The favorite_count of this Tweets.
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count: int):
        """
        Sets the favorite_count of this Tweets.

        :param favorite_count: The favorite_count of this Tweets.
        :type favorite_count: int
        """

        self._favorite_count = favorite_count

    @property
    def favorited(self) -> bool:
        """
        Gets the favorited of this Tweets.

        :return: The favorited of this Tweets.
        :rtype: bool
        """
        return self._favorited

    @favorited.setter
    def favorited(self, favorited: bool):
        """
        Sets the favorited of this Tweets.

        :param favorited: The favorited of this Tweets.
        :type favorited: bool
        """

        self._favorited = favorited

    @property
    def filter_level(self) -> str:
        """
        Gets the filter_level of this Tweets.

        :return: The filter_level of this Tweets.
        :rtype: str
        """
        return self._filter_level

    @filter_level.setter
    def filter_level(self, filter_level: str):
        """
        Sets the filter_level of this Tweets.

        :param filter_level: The filter_level of this Tweets.
        :type filter_level: str
        """

        self._filter_level = filter_level

    @property
    def id(self) -> int:
        """
        Gets the id of this Tweets.

        :return: The id of this Tweets.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Tweets.

        :param id: The id of this Tweets.
        :type id: int
        """

        self._id = id

    @property
    def id_str(self) -> str:
        """
        Gets the id_str of this Tweets.

        :return: The id_str of this Tweets.
        :rtype: str
        """
        return self._id_str

    @id_str.setter
    def id_str(self, id_str: str):
        """
        Sets the id_str of this Tweets.

        :param id_str: The id_str of this Tweets.
        :type id_str: str
        """

        self._id_str = id_str

    @property
    def in_reply_to_screen_name(self) -> str:
        """
        Gets the in_reply_to_screen_name of this Tweets.

        :return: The in_reply_to_screen_name of this Tweets.
        :rtype: str
        """
        return self._in_reply_to_screen_name

    @in_reply_to_screen_name.setter
    def in_reply_to_screen_name(self, in_reply_to_screen_name: str):
        """
        Sets the in_reply_to_screen_name of this Tweets.

        :param in_reply_to_screen_name: The in_reply_to_screen_name of this Tweets.
        :type in_reply_to_screen_name: str
        """

        self._in_reply_to_screen_name = in_reply_to_screen_name

    @property
    def in_reply_to_status_id(self) -> int:
        """
        Gets the in_reply_to_status_id of this Tweets.

        :return: The in_reply_to_status_id of this Tweets.
        :rtype: int
        """
        return self._in_reply_to_status_id

    @in_reply_to_status_id.setter
    def in_reply_to_status_id(self, in_reply_to_status_id: int):
        """
        Sets the in_reply_to_status_id of this Tweets.

        :param in_reply_to_status_id: The in_reply_to_status_id of this Tweets.
        :type in_reply_to_status_id: int
        """

        self._in_reply_to_status_id = in_reply_to_status_id

    @property
    def in_reply_to_status_id_str(self) -> str:
        """
        Gets the in_reply_to_status_id_str of this Tweets.

        :return: The in_reply_to_status_id_str of this Tweets.
        :rtype: str
        """
        return self._in_reply_to_status_id_str

    @in_reply_to_status_id_str.setter
    def in_reply_to_status_id_str(self, in_reply_to_status_id_str: str):
        """
        Sets the in_reply_to_status_id_str of this Tweets.

        :param in_reply_to_status_id_str: The in_reply_to_status_id_str of this Tweets.
        :type in_reply_to_status_id_str: str
        """

        self._in_reply_to_status_id_str = in_reply_to_status_id_str

    @property
    def in_reply_to_user_id(self) -> int:
        """
        Gets the in_reply_to_user_id of this Tweets.

        :return: The in_reply_to_user_id of this Tweets.
        :rtype: int
        """
        return self._in_reply_to_user_id

    @in_reply_to_user_id.setter
    def in_reply_to_user_id(self, in_reply_to_user_id: int):
        """
        Sets the in_reply_to_user_id of this Tweets.

        :param in_reply_to_user_id: The in_reply_to_user_id of this Tweets.
        :type in_reply_to_user_id: int
        """

        self._in_reply_to_user_id = in_reply_to_user_id

    @property
    def in_reply_to_user_id_str(self) -> str:
        """
        Gets the in_reply_to_user_id_str of this Tweets.

        :return: The in_reply_to_user_id_str of this Tweets.
        :rtype: str
        """
        return self._in_reply_to_user_id_str

    @in_reply_to_user_id_str.setter
    def in_reply_to_user_id_str(self, in_reply_to_user_id_str: str):
        """
        Sets the in_reply_to_user_id_str of this Tweets.

        :param in_reply_to_user_id_str: The in_reply_to_user_id_str of this Tweets.
        :type in_reply_to_user_id_str: str
        """

        self._in_reply_to_user_id_str = in_reply_to_user_id_str

    @property
    def lang(self) -> str:
        """
        Gets the lang of this Tweets.

        :return: The lang of this Tweets.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """
        Sets the lang of this Tweets.

        :param lang: The lang of this Tweets.
        :type lang: str
        """

        self._lang = lang

    @property
    def possibly_sensitive(self) -> bool:
        """
        Gets the possibly_sensitive of this Tweets.

        :return: The possibly_sensitive of this Tweets.
        :rtype: bool
        """
        return self._possibly_sensitive

    @possibly_sensitive.setter
    def possibly_sensitive(self, possibly_sensitive: bool):
        """
        Sets the possibly_sensitive of this Tweets.

        :param possibly_sensitive: The possibly_sensitive of this Tweets.
        :type possibly_sensitive: bool
        """

        self._possibly_sensitive = possibly_sensitive

    @property
    def quoted_status_id(self) -> int:
        """
        Gets the quoted_status_id of this Tweets.

        :return: The quoted_status_id of this Tweets.
        :rtype: int
        """
        return self._quoted_status_id

    @quoted_status_id.setter
    def quoted_status_id(self, quoted_status_id: int):
        """
        Sets the quoted_status_id of this Tweets.

        :param quoted_status_id: The quoted_status_id of this Tweets.
        :type quoted_status_id: int
        """

        self._quoted_status_id = quoted_status_id

    @property
    def quoted_status_id_str(self) -> str:
        """
        Gets the quoted_status_id_str of this Tweets.

        :return: The quoted_status_id_str of this Tweets.
        :rtype: str
        """
        return self._quoted_status_id_str

    @quoted_status_id_str.setter
    def quoted_status_id_str(self, quoted_status_id_str: str):
        """
        Sets the quoted_status_id_str of this Tweets.

        :param quoted_status_id_str: The quoted_status_id_str of this Tweets.
        :type quoted_status_id_str: str
        """

        self._quoted_status_id_str = quoted_status_id_str

    @property
    def scopes(self) -> object:
        """
        Gets the scopes of this Tweets.

        :return: The scopes of this Tweets.
        :rtype: object
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes: object):
        """
        Sets the scopes of this Tweets.

        :param scopes: The scopes of this Tweets.
        :type scopes: object
        """

        self._scopes = scopes

    @property
    def retweet_count(self) -> int:
        """
        Gets the retweet_count of this Tweets.

        :return: The retweet_count of this Tweets.
        :rtype: int
        """
        return self._retweet_count

    @retweet_count.setter
    def retweet_count(self, retweet_count: int):
        """
        Sets the retweet_count of this Tweets.

        :param retweet_count: The retweet_count of this Tweets.
        :type retweet_count: int
        """

        self._retweet_count = retweet_count

    @property
    def retweeted(self) -> bool:
        """
        Gets the retweeted of this Tweets.

        :return: The retweeted of this Tweets.
        :rtype: bool
        """
        return self._retweeted

    @retweeted.setter
    def retweeted(self, retweeted: bool):
        """
        Sets the retweeted of this Tweets.

        :param retweeted: The retweeted of this Tweets.
        :type retweeted: bool
        """

        self._retweeted = retweeted

    @property
    def source(self) -> str:
        """
        Gets the source of this Tweets.

        :return: The source of this Tweets.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """
        Sets the source of this Tweets.

        :param source: The source of this Tweets.
        :type source: str
        """

        self._source = source

    @property
    def text(self) -> str:
        """
        Gets the text of this Tweets.

        :return: The text of this Tweets.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """
        Sets the text of this Tweets.

        :param text: The text of this Tweets.
        :type text: str
        """

        self._text = text

    @property
    def truncated(self) -> str:
        """
        Gets the truncated of this Tweets.

        :return: The truncated of this Tweets.
        :rtype: str
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated: str):
        """
        Sets the truncated of this Tweets.

        :param truncated: The truncated of this Tweets.
        :type truncated: str
        """

        self._truncated = truncated

    @property
    def user(self) -> Users:
        """
        Gets the user of this Tweets.

        :return: The user of this Tweets.
        :rtype: Users
        """
        return self._user

    @user.setter
    def user(self, user: Users):
        """
        Sets the user of this Tweets.

        :param user: The user of this Tweets.
        :type user: Users
        """

        self._user = user

    @property
    def withheld_copyright(self) -> bool:
        """
        Gets the withheld_copyright of this Tweets.

        :return: The withheld_copyright of this Tweets.
        :rtype: bool
        """
        return self._withheld_copyright

    @withheld_copyright.setter
    def withheld_copyright(self, withheld_copyright: bool):
        """
        Sets the withheld_copyright of this Tweets.

        :param withheld_copyright: The withheld_copyright of this Tweets.
        :type withheld_copyright: bool
        """

        self._withheld_copyright = withheld_copyright

    @property
    def withheld_countries(self) -> List[str]:
        """
        Gets the withheld_countries of this Tweets.

        :return: The withheld_countries of this Tweets.
        :rtype: List[str]
        """
        return self._withheld_countries

    @withheld_countries.setter
    def withheld_countries(self, withheld_countries: List[str]):
        """
        Sets the withheld_countries of this Tweets.

        :param withheld_countries: The withheld_countries of this Tweets.
        :type withheld_countries: List[str]
        """

        self._withheld_countries = withheld_countries

    @property
    def withheld_scope(self) -> str:
        """
        Gets the withheld_scope of this Tweets.

        :return: The withheld_scope of this Tweets.
        :rtype: str
        """
        return self._withheld_scope

    @withheld_scope.setter
    def withheld_scope(self, withheld_scope: str):
        """
        Sets the withheld_scope of this Tweets.

        :param withheld_scope: The withheld_scope of this Tweets.
        :type withheld_scope: str
        """

        self._withheld_scope = withheld_scope

