# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IReadOnlyDictionary21(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_none': 'list[str]',
        'acoustic': 'list[str]',
        'language': 'list[str]',
        'acoustic_and_language': 'list[str]',
        'custom_voice': 'list[str]',
        'language_generation': 'list[str]',
        'sentiment': 'list[str]',
        'language_identification': 'list[str]',
        'diarization': 'list[str]'
    }

    attribute_map = {
        '_none': 'None',
        'acoustic': 'Acoustic',
        'language': 'Language',
        'acoustic_and_language': 'AcousticAndLanguage',
        'custom_voice': 'CustomVoice',
        'language_generation': 'LanguageGeneration',
        'sentiment': 'Sentiment',
        'language_identification': 'LanguageIdentification',
        'diarization': 'Diarization'
    }

    def __init__(self, _none=None, acoustic=None, language=None, acoustic_and_language=None, custom_voice=None, language_generation=None, sentiment=None, language_identification=None, diarization=None):  # noqa: E501
        """IReadOnlyDictionary21 - a model defined in Swagger"""  # noqa: E501

        self.__none = None
        self._acoustic = None
        self._language = None
        self._acoustic_and_language = None
        self._custom_voice = None
        self._language_generation = None
        self._sentiment = None
        self._language_identification = None
        self._diarization = None
        self.discriminator = None

        if _none is not None:
            self._none = _none
        if acoustic is not None:
            self.acoustic = acoustic
        if language is not None:
            self.language = language
        if acoustic_and_language is not None:
            self.acoustic_and_language = acoustic_and_language
        if custom_voice is not None:
            self.custom_voice = custom_voice
        if language_generation is not None:
            self.language_generation = language_generation
        if sentiment is not None:
            self.sentiment = sentiment
        if language_identification is not None:
            self.language_identification = language_identification
        if diarization is not None:
            self.diarization = diarization

    @property
    def _none(self):
        """Gets the _none of this IReadOnlyDictionary21.  # noqa: E501


        :return: The _none of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this IReadOnlyDictionary21.


        :param _none: The _none of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self.__none = _none

    @property
    def acoustic(self):
        """Gets the acoustic of this IReadOnlyDictionary21.  # noqa: E501


        :return: The acoustic of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._acoustic

    @acoustic.setter
    def acoustic(self, acoustic):
        """Sets the acoustic of this IReadOnlyDictionary21.


        :param acoustic: The acoustic of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._acoustic = acoustic

    @property
    def language(self):
        """Gets the language of this IReadOnlyDictionary21.  # noqa: E501


        :return: The language of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this IReadOnlyDictionary21.


        :param language: The language of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._language = language

    @property
    def acoustic_and_language(self):
        """Gets the acoustic_and_language of this IReadOnlyDictionary21.  # noqa: E501


        :return: The acoustic_and_language of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._acoustic_and_language

    @acoustic_and_language.setter
    def acoustic_and_language(self, acoustic_and_language):
        """Sets the acoustic_and_language of this IReadOnlyDictionary21.


        :param acoustic_and_language: The acoustic_and_language of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._acoustic_and_language = acoustic_and_language

    @property
    def custom_voice(self):
        """Gets the custom_voice of this IReadOnlyDictionary21.  # noqa: E501


        :return: The custom_voice of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_voice

    @custom_voice.setter
    def custom_voice(self, custom_voice):
        """Sets the custom_voice of this IReadOnlyDictionary21.


        :param custom_voice: The custom_voice of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._custom_voice = custom_voice

    @property
    def language_generation(self):
        """Gets the language_generation of this IReadOnlyDictionary21.  # noqa: E501


        :return: The language_generation of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._language_generation

    @language_generation.setter
    def language_generation(self, language_generation):
        """Sets the language_generation of this IReadOnlyDictionary21.


        :param language_generation: The language_generation of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._language_generation = language_generation

    @property
    def sentiment(self):
        """Gets the sentiment of this IReadOnlyDictionary21.  # noqa: E501


        :return: The sentiment of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this IReadOnlyDictionary21.


        :param sentiment: The sentiment of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._sentiment = sentiment

    @property
    def language_identification(self):
        """Gets the language_identification of this IReadOnlyDictionary21.  # noqa: E501


        :return: The language_identification of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._language_identification

    @language_identification.setter
    def language_identification(self, language_identification):
        """Sets the language_identification of this IReadOnlyDictionary21.


        :param language_identification: The language_identification of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._language_identification = language_identification

    @property
    def diarization(self):
        """Gets the diarization of this IReadOnlyDictionary21.  # noqa: E501


        :return: The diarization of this IReadOnlyDictionary21.  # noqa: E501
        :rtype: list[str]
        """
        return self._diarization

    @diarization.setter
    def diarization(self, diarization):
        """Sets the diarization of this IReadOnlyDictionary21.


        :param diarization: The diarization of this IReadOnlyDictionary21.  # noqa: E501
        :type: list[str]
        """

        self._diarization = diarization

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IReadOnlyDictionary21, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IReadOnlyDictionary21):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
