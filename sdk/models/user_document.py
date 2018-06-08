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


class UserDocument(object):
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
        'name': 'str',
        'created': 'datetime',
        'id': 'int',
        'content': 'str',
        'content_type': 'str',
        'preview': 'str',
        'last_modified': 'datetime',
        'document_id': 'str',
        'document_type': 'str',
        'auto_save_last_modified': 'datetime',
        'grammar_score': 'int',
        'style_score': 'int',
        'spelling_score': 'int',
        'term_score': 'int',
        'overall_score': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'created': 'Created',
        'id': 'Id',
        'content': 'Content',
        'content_type': 'ContentType',
        'preview': 'Preview',
        'last_modified': 'LastModified',
        'document_id': 'DocumentId',
        'document_type': 'DocumentType',
        'auto_save_last_modified': 'AutoSaveLastModified',
        'grammar_score': 'GrammarScore',
        'style_score': 'StyleScore',
        'spelling_score': 'SpellingScore',
        'term_score': 'TermScore',
        'overall_score': 'OverallScore'
    }

    def __init__(self, name=None, created=None, id=None, content=None, content_type=None, preview=None, last_modified=None, document_id=None, document_type=None, auto_save_last_modified=None, grammar_score=None, style_score=None, spelling_score=None, term_score=None, overall_score=None):
        """
        UserDocument - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._id = None
        self._content = None
        self._content_type = None
        self._preview = None
        self._last_modified = None
        self._document_id = None
        self._document_type = None
        self._auto_save_last_modified = None
        self._grammar_score = None
        self._style_score = None
        self._spelling_score = None
        self._term_score = None
        self._overall_score = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if id is not None:
          self.id = id
        if content is not None:
          self.content = content
        if content_type is not None:
          self.content_type = content_type
        if preview is not None:
          self.preview = preview
        if last_modified is not None:
          self.last_modified = last_modified
        if document_id is not None:
          self.document_id = document_id
        if document_type is not None:
          self.document_type = document_type
        if auto_save_last_modified is not None:
          self.auto_save_last_modified = auto_save_last_modified
        if grammar_score is not None:
          self.grammar_score = grammar_score
        if style_score is not None:
          self.style_score = style_score
        if spelling_score is not None:
          self.spelling_score = spelling_score
        if term_score is not None:
          self.term_score = term_score
        if overall_score is not None:
          self.overall_score = overall_score

    @property
    def name(self):
        """
        Gets the name of this UserDocument.
        Name of the document

        :return: The name of this UserDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserDocument.
        Name of the document

        :param name: The name of this UserDocument.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this UserDocument.
        Document creation date/time

        :return: The created of this UserDocument.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this UserDocument.
        Document creation date/time

        :param created: The created of this UserDocument.
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this UserDocument.
        Document ID

        :return: The id of this UserDocument.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserDocument.
        Document ID

        :param id: The id of this UserDocument.
        :type: int
        """

        self._id = id

    @property
    def content(self):
        """
        Gets the content of this UserDocument.
        Document contents, as HTML or text (see ContentType)

        :return: The content of this UserDocument.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this UserDocument.
        Document contents, as HTML or text (see ContentType)

        :param content: The content of this UserDocument.
        :type: str
        """

        self._content = content

    @property
    def content_type(self):
        """
        Gets the content_type of this UserDocument.
        Document content type: \"T\" for text, null or empty for HTML

        :return: The content_type of this UserDocument.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this UserDocument.
        Document content type: \"T\" for text, null or empty for HTML

        :param content_type: The content_type of this UserDocument.
        :type: str
        """

        self._content_type = content_type

    @property
    def preview(self):
        """
        Gets the preview of this UserDocument.
        Preview of the document content, as text

        :return: The preview of this UserDocument.
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """
        Sets the preview of this UserDocument.
        Preview of the document content, as text

        :param preview: The preview of this UserDocument.
        :type: str
        """

        self._preview = preview

    @property
    def last_modified(self):
        """
        Gets the last_modified of this UserDocument.
        Date/time of the last document modification

        :return: The last_modified of this UserDocument.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this UserDocument.
        Date/time of the last document modification

        :param last_modified: The last_modified of this UserDocument.
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def document_id(self):
        """
        Gets the document_id of this UserDocument.
        Internal document ID (GUID)

        :return: The document_id of this UserDocument.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this UserDocument.
        Internal document ID (GUID)

        :param document_id: The document_id of this UserDocument.
        :type: str
        """

        self._document_id = document_id

    @property
    def document_type(self):
        """
        Gets the document_type of this UserDocument.
        Internal document Type (string)

        :return: The document_type of this UserDocument.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this UserDocument.
        Internal document Type (string)

        :param document_type: The document_type of this UserDocument.
        :type: str
        """

        self._document_type = document_type

    @property
    def auto_save_last_modified(self):
        """
        Gets the auto_save_last_modified of this UserDocument.
        Date/time of the last document auto save

        :return: The auto_save_last_modified of this UserDocument.
        :rtype: datetime
        """
        return self._auto_save_last_modified

    @auto_save_last_modified.setter
    def auto_save_last_modified(self, auto_save_last_modified):
        """
        Sets the auto_save_last_modified of this UserDocument.
        Date/time of the last document auto save

        :param auto_save_last_modified: The auto_save_last_modified of this UserDocument.
        :type: datetime
        """

        self._auto_save_last_modified = auto_save_last_modified

    @property
    def grammar_score(self):
        """
        Gets the grammar_score of this UserDocument.
        Grammar score

        :return: The grammar_score of this UserDocument.
        :rtype: int
        """
        return self._grammar_score

    @grammar_score.setter
    def grammar_score(self, grammar_score):
        """
        Sets the grammar_score of this UserDocument.
        Grammar score

        :param grammar_score: The grammar_score of this UserDocument.
        :type: int
        """

        self._grammar_score = grammar_score

    @property
    def style_score(self):
        """
        Gets the style_score of this UserDocument.
        Style score

        :return: The style_score of this UserDocument.
        :rtype: int
        """
        return self._style_score

    @style_score.setter
    def style_score(self, style_score):
        """
        Sets the style_score of this UserDocument.
        Style score

        :param style_score: The style_score of this UserDocument.
        :type: int
        """

        self._style_score = style_score

    @property
    def spelling_score(self):
        """
        Gets the spelling_score of this UserDocument.
        Spelling score

        :return: The spelling_score of this UserDocument.
        :rtype: int
        """
        return self._spelling_score

    @spelling_score.setter
    def spelling_score(self, spelling_score):
        """
        Sets the spelling_score of this UserDocument.
        Spelling score

        :param spelling_score: The spelling_score of this UserDocument.
        :type: int
        """

        self._spelling_score = spelling_score

    @property
    def term_score(self):
        """
        Gets the term_score of this UserDocument.
        Term score

        :return: The term_score of this UserDocument.
        :rtype: int
        """
        return self._term_score

    @term_score.setter
    def term_score(self, term_score):
        """
        Sets the term_score of this UserDocument.
        Term score

        :param term_score: The term_score of this UserDocument.
        :type: int
        """

        self._term_score = term_score

    @property
    def overall_score(self):
        """
        Gets the overall_score of this UserDocument.
        Overall score, based on the previous scores

        :return: The overall_score of this UserDocument.
        :rtype: int
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score):
        """
        Sets the overall_score of this UserDocument.
        Overall score, based on the previous scores

        :param overall_score: The overall_score of this UserDocument.
        :type: int
        """

        self._overall_score = overall_score

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
        if not isinstance(other, UserDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
