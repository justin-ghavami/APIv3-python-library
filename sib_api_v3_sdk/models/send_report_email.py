# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendReportEmail(object):
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
        'subject': 'str',
        'to': 'list[str]',
        'content_type': 'str',
        'bcc': 'list[str]',
        'cc': 'list[str]',
        'body': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'to': 'to',
        'content_type': 'contentType',
        'bcc': 'bcc',
        'cc': 'cc',
        'body': 'body'
    }

    def __init__(self, subject=None, to=None, content_type='html', bcc=None, cc=None, body=None):  # noqa: E501
        """SendReportEmail - a model defined in Swagger"""  # noqa: E501

        self._subject = None
        self._to = None
        self._content_type = None
        self._bcc = None
        self._cc = None
        self._body = None
        self.discriminator = None

        self.subject = subject
        self.to = to
        if content_type is not None:
            self.content_type = content_type
        if bcc is not None:
            self.bcc = bcc
        if cc is not None:
            self.cc = cc
        self.body = body

    @property
    def subject(self):
        """Gets the subject of this SendReportEmail.  # noqa: E501

        Subject of the email message  # noqa: E501

        :return: The subject of this SendReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendReportEmail.

        Subject of the email message  # noqa: E501

        :param subject: The subject of this SendReportEmail.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this SendReportEmail.  # noqa: E501

        Email addresses of the recipients  # noqa: E501

        :return: The to of this SendReportEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendReportEmail.

        Email addresses of the recipients  # noqa: E501

        :param to: The to of this SendReportEmail.  # noqa: E501
        :type: list[str]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def content_type(self):
        """Gets the content_type of this SendReportEmail.  # noqa: E501

        Type of the message body  # noqa: E501

        :return: The content_type of this SendReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this SendReportEmail.

        Type of the message body  # noqa: E501

        :param content_type: The content_type of this SendReportEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "html"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def bcc(self):
        """Gets the bcc of this SendReportEmail.  # noqa: E501

        Email addresses of the recipients in bcc  # noqa: E501

        :return: The bcc of this SendReportEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SendReportEmail.

        Email addresses of the recipients in bcc  # noqa: E501

        :param bcc: The bcc of this SendReportEmail.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def cc(self):
        """Gets the cc of this SendReportEmail.  # noqa: E501

        Email addresses of the recipients in cc  # noqa: E501

        :return: The cc of this SendReportEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SendReportEmail.

        Email addresses of the recipients in cc  # noqa: E501

        :param cc: The cc of this SendReportEmail.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def body(self):
        """Gets the body of this SendReportEmail.  # noqa: E501

        Body of the email message  # noqa: E501

        :return: The body of this SendReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendReportEmail.

        Body of the email message  # noqa: E501

        :param body: The body of this SendReportEmail.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendReportEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
