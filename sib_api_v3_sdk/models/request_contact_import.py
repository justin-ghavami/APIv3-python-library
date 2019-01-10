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

from sib_api_v3_sdk.models.request_contact_import_new_list import RequestContactImportNewList  # noqa: F401,E501


class RequestContactImport(object):
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
        'file_url': 'str',
        'file_body': 'str',
        'list_ids': 'list[int]',
        'notify_url': 'str',
        'new_list': 'RequestContactImportNewList',
        'email_blacklist': 'bool',
        'sms_blacklist': 'bool',
        'update_existing_contacts': 'bool',
        'empty_contacts_attributes': 'bool'
    }

    attribute_map = {
        'file_url': 'fileUrl',
        'file_body': 'fileBody',
        'list_ids': 'listIds',
        'notify_url': 'notifyUrl',
        'new_list': 'newList',
        'email_blacklist': 'emailBlacklist',
        'sms_blacklist': 'smsBlacklist',
        'update_existing_contacts': 'updateExistingContacts',
        'empty_contacts_attributes': 'emptyContactsAttributes'
    }

    def __init__(self, file_url=None, file_body=None, list_ids=None, notify_url=None, new_list=None, email_blacklist=False, sms_blacklist=False, update_existing_contacts=True, empty_contacts_attributes=False):  # noqa: E501
        """RequestContactImport - a model defined in Swagger"""  # noqa: E501

        self._file_url = None
        self._file_body = None
        self._list_ids = None
        self._notify_url = None
        self._new_list = None
        self._email_blacklist = None
        self._sms_blacklist = None
        self._update_existing_contacts = None
        self._empty_contacts_attributes = None
        self.discriminator = None

        if file_url is not None:
            self.file_url = file_url
        if file_body is not None:
            self.file_body = file_body
        if list_ids is not None:
            self.list_ids = list_ids
        if notify_url is not None:
            self.notify_url = notify_url
        if new_list is not None:
            self.new_list = new_list
        if email_blacklist is not None:
            self.email_blacklist = email_blacklist
        if sms_blacklist is not None:
            self.sms_blacklist = sms_blacklist
        if update_existing_contacts is not None:
            self.update_existing_contacts = update_existing_contacts
        if empty_contacts_attributes is not None:
            self.empty_contacts_attributes = empty_contacts_attributes

    @property
    def file_url(self):
        """Gets the file_url of this RequestContactImport.  # noqa: E501

        Mandatory if fileBody is not defined. URL of the file to be imported (no local file). Possible file formats: .txt, .csv  # noqa: E501

        :return: The file_url of this RequestContactImport.  # noqa: E501
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this RequestContactImport.

        Mandatory if fileBody is not defined. URL of the file to be imported (no local file). Possible file formats: .txt, .csv  # noqa: E501

        :param file_url: The file_url of this RequestContactImport.  # noqa: E501
        :type: str
        """

        self._file_url = file_url

    @property
    def file_body(self):
        """Gets the file_body of this RequestContactImport.  # noqa: E501

        Mandatory if fileUrl is not defined. CSV content to be imported. Use semicolon to separate multiple attributes  # noqa: E501

        :return: The file_body of this RequestContactImport.  # noqa: E501
        :rtype: str
        """
        return self._file_body

    @file_body.setter
    def file_body(self, file_body):
        """Sets the file_body of this RequestContactImport.

        Mandatory if fileUrl is not defined. CSV content to be imported. Use semicolon to separate multiple attributes  # noqa: E501

        :param file_body: The file_body of this RequestContactImport.  # noqa: E501
        :type: str
        """

        self._file_body = file_body

    @property
    def list_ids(self):
        """Gets the list_ids of this RequestContactImport.  # noqa: E501

        Mandatory if newList is not defined. Ids of the lists in which the contacts shall be imported. For example, [2, 4, 7].  # noqa: E501

        :return: The list_ids of this RequestContactImport.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """Sets the list_ids of this RequestContactImport.

        Mandatory if newList is not defined. Ids of the lists in which the contacts shall be imported. For example, [2, 4, 7].  # noqa: E501

        :param list_ids: The list_ids of this RequestContactImport.  # noqa: E501
        :type: list[int]
        """

        self._list_ids = list_ids

    @property
    def notify_url(self):
        """Gets the notify_url of this RequestContactImport.  # noqa: E501

        URL that will be called once the export process is finished  # noqa: E501

        :return: The notify_url of this RequestContactImport.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this RequestContactImport.

        URL that will be called once the export process is finished  # noqa: E501

        :param notify_url: The notify_url of this RequestContactImport.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def new_list(self):
        """Gets the new_list of this RequestContactImport.  # noqa: E501


        :return: The new_list of this RequestContactImport.  # noqa: E501
        :rtype: RequestContactImportNewList
        """
        return self._new_list

    @new_list.setter
    def new_list(self, new_list):
        """Sets the new_list of this RequestContactImport.


        :param new_list: The new_list of this RequestContactImport.  # noqa: E501
        :type: RequestContactImportNewList
        """

        self._new_list = new_list

    @property
    def email_blacklist(self):
        """Gets the email_blacklist of this RequestContactImport.  # noqa: E501

        To blacklist all the contacts for email  # noqa: E501

        :return: The email_blacklist of this RequestContactImport.  # noqa: E501
        :rtype: bool
        """
        return self._email_blacklist

    @email_blacklist.setter
    def email_blacklist(self, email_blacklist):
        """Sets the email_blacklist of this RequestContactImport.

        To blacklist all the contacts for email  # noqa: E501

        :param email_blacklist: The email_blacklist of this RequestContactImport.  # noqa: E501
        :type: bool
        """

        self._email_blacklist = email_blacklist

    @property
    def sms_blacklist(self):
        """Gets the sms_blacklist of this RequestContactImport.  # noqa: E501

        To blacklist all the contacts for sms  # noqa: E501

        :return: The sms_blacklist of this RequestContactImport.  # noqa: E501
        :rtype: bool
        """
        return self._sms_blacklist

    @sms_blacklist.setter
    def sms_blacklist(self, sms_blacklist):
        """Sets the sms_blacklist of this RequestContactImport.

        To blacklist all the contacts for sms  # noqa: E501

        :param sms_blacklist: The sms_blacklist of this RequestContactImport.  # noqa: E501
        :type: bool
        """

        self._sms_blacklist = sms_blacklist

    @property
    def update_existing_contacts(self):
        """Gets the update_existing_contacts of this RequestContactImport.  # noqa: E501

        To facilitate the choice to update the existing contacts  # noqa: E501

        :return: The update_existing_contacts of this RequestContactImport.  # noqa: E501
        :rtype: bool
        """
        return self._update_existing_contacts

    @update_existing_contacts.setter
    def update_existing_contacts(self, update_existing_contacts):
        """Sets the update_existing_contacts of this RequestContactImport.

        To facilitate the choice to update the existing contacts  # noqa: E501

        :param update_existing_contacts: The update_existing_contacts of this RequestContactImport.  # noqa: E501
        :type: bool
        """

        self._update_existing_contacts = update_existing_contacts

    @property
    def empty_contacts_attributes(self):
        """Gets the empty_contacts_attributes of this RequestContactImport.  # noqa: E501

        To facilitate the choice to erase any attribute of the existing contacts with empty value. emptyContactsAttributes = true means the empty fields in your import will erase any attribute that currently contain data in SendinBlue, & emptyContactsAttributes = false means the empty fields will not affect your existing data ( only available if `updateExistingContacts` set to true )  # noqa: E501

        :return: The empty_contacts_attributes of this RequestContactImport.  # noqa: E501
        :rtype: bool
        """
        return self._empty_contacts_attributes

    @empty_contacts_attributes.setter
    def empty_contacts_attributes(self, empty_contacts_attributes):
        """Sets the empty_contacts_attributes of this RequestContactImport.

        To facilitate the choice to erase any attribute of the existing contacts with empty value. emptyContactsAttributes = true means the empty fields in your import will erase any attribute that currently contain data in SendinBlue, & emptyContactsAttributes = false means the empty fields will not affect your existing data ( only available if `updateExistingContacts` set to true )  # noqa: E501

        :param empty_contacts_attributes: The empty_contacts_attributes of this RequestContactImport.  # noqa: E501
        :type: bool
        """

        self._empty_contacts_attributes = empty_contacts_attributes

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
        if not isinstance(other, RequestContactImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
