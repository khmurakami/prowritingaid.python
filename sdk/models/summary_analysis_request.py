# coding: utf-8

"""
    ProWritingAid API V2

    Official ProWritingAid API Version 2

    OpenAPI spec version: v2
    Contact: hello@prowritingaid.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SummaryAnalysisRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'text': 'str',
        'settings': 'AnalysisSettings',
        'style': 'str',
        'language': 'str'
    }

    attribute_map = {
        'text': 'Text',
        'settings': 'Settings',
        'style': 'Style',
        'language': 'Language'
    }

    def __init__(self, text=None, settings=None, style='General', language='en'):
        """
        SummaryAnalysisRequest - a model defined in Swagger
        """

        self._text = None
        self._settings = None
        self._style = None
        self._language = None

        self.text = text
        self.settings = settings
        self.style = style
        self.language = language

    @property
    def text(self):
        """
        Gets the text of this SummaryAnalysisRequest.
        Text to be analyzed

        :return: The text of this SummaryAnalysisRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SummaryAnalysisRequest.
        Text to be analyzed

        :param text: The text of this SummaryAnalysisRequest.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def settings(self):
        """
        Gets the settings of this SummaryAnalysisRequest.
        Analysis settings

        :return: The settings of this SummaryAnalysisRequest.
        :rtype: AnalysisSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this SummaryAnalysisRequest.
        Analysis settings

        :param settings: The settings of this SummaryAnalysisRequest.
        :type: AnalysisSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")

        self._settings = settings

    @property
    def style(self):
        """
        Gets the style of this SummaryAnalysisRequest.
        Document's writing style

        :return: The style of this SummaryAnalysisRequest.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Sets the style of this SummaryAnalysisRequest.
        Document's writing style

        :param style: The style of this SummaryAnalysisRequest.
        :type: str
        """
        if style is None:
            raise ValueError("Invalid value for `style`, must not be `None`")
        allowed_values = ["NotSet", "General", "Academic", "Business", "Technical", "Creative", "Casual", "Web"]
        if style not in allowed_values:
            raise ValueError(
                "Invalid value for `style` ({0}), must be one of {1}"
                .format(style, allowed_values)
            )

        self._style = style

    @property
    def language(self):
        """
        Gets the language of this SummaryAnalysisRequest.
        Document's language. Set correct UK/US language to get region-specific suggestions

        :return: The language of this SummaryAnalysisRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this SummaryAnalysisRequest.
        Document's language. Set correct UK/US language to get region-specific suggestions

        :param language: The language of this SummaryAnalysisRequest.
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")
        allowed_values = ["en_US", "en_UK", "en", "es"]
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"
                .format(language, allowed_values)
            )

        self._language = language

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SummaryAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
