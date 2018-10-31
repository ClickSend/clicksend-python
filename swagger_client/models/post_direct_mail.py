# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.post_direct_mail_area import PostDirectMailArea  # noqa: F401,E501


class PostDirectMail(object):
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
        'name': 'str',
        'file_urls': 'list[str]',
        'size': 'str',
        'areas': 'list[PostDirectMailArea]',
        'schedule': 'int',
        'source': 'str',
        'custom_string': 'str'
    }

    attribute_map = {
        'name': 'name',
        'file_urls': 'file_urls',
        'size': 'size',
        'areas': 'areas',
        'schedule': 'schedule',
        'source': 'source',
        'custom_string': 'custom_string'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, name=None, file_urls=None, size=None, areas=None, schedule=0, source='sdk', custom_string=None):  # noqa: E501
        """PostDirectMail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._file_urls = None
        self._size = None
        self._areas = None
        self._schedule = None
        self._source = None
        self._custom_string = None
        self.discriminator = 'classType'

        self.name = name
        self.file_urls = file_urls
        self.size = size
        self.areas = areas
        if schedule is not None:
            self.schedule = schedule
        if source is not None:
            self.source = source
        if custom_string is not None:
            self.custom_string = custom_string

    @property
    def name(self):
        """Gets the name of this PostDirectMail.  # noqa: E501

        Campaign name  # noqa: E501

        :return: The name of this PostDirectMail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostDirectMail.

        Campaign name  # noqa: E501

        :param name: The name of this PostDirectMail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def file_urls(self):
        """Gets the file_urls of this PostDirectMail.  # noqa: E501

        Campaign file URLs (maximum 2)  # noqa: E501

        :return: The file_urls of this PostDirectMail.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_urls

    @file_urls.setter
    def file_urls(self, file_urls):
        """Sets the file_urls of this PostDirectMail.

        Campaign file URLs (maximum 2)  # noqa: E501

        :param file_urls: The file_urls of this PostDirectMail.  # noqa: E501
        :type: list[str]
        """
        if file_urls is None:
            raise ValueError("Invalid value for `file_urls`, must not be `None`")  # noqa: E501

        self._file_urls = file_urls

    @property
    def size(self):
        """Gets the size of this PostDirectMail.  # noqa: E501

        Document size - A5 or DL  # noqa: E501

        :return: The size of this PostDirectMail.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PostDirectMail.

        Document size - A5 or DL  # noqa: E501

        :param size: The size of this PostDirectMail.  # noqa: E501
        :type: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def areas(self):
        """Gets the areas of this PostDirectMail.  # noqa: E501

        PostDirectMailArea model  # noqa: E501

        :return: The areas of this PostDirectMail.  # noqa: E501
        :rtype: list[PostDirectMailArea]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this PostDirectMail.

        PostDirectMailArea model  # noqa: E501

        :param areas: The areas of this PostDirectMail.  # noqa: E501
        :type: list[PostDirectMailArea]
        """
        if areas is None:
            raise ValueError("Invalid value for `areas`, must not be `None`")  # noqa: E501

        self._areas = areas

    @property
    def schedule(self):
        """Gets the schedule of this PostDirectMail.  # noqa: E501

        Leave blank for immediate delivery. Your schedule time in unix format.  # noqa: E501

        :return: The schedule of this PostDirectMail.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this PostDirectMail.

        Leave blank for immediate delivery. Your schedule time in unix format.  # noqa: E501

        :param schedule: The schedule of this PostDirectMail.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

    @property
    def source(self):
        """Gets the source of this PostDirectMail.  # noqa: E501

        Your method of sending e.g. 'wordpress', 'php', 'c#'.  # noqa: E501

        :return: The source of this PostDirectMail.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PostDirectMail.

        Your method of sending e.g. 'wordpress', 'php', 'c#'.  # noqa: E501

        :param source: The source of this PostDirectMail.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def custom_string(self):
        """Gets the custom_string of this PostDirectMail.  # noqa: E501

        A custom string for your own reference  # noqa: E501

        :return: The custom_string of this PostDirectMail.  # noqa: E501
        :rtype: str
        """
        return self._custom_string

    @custom_string.setter
    def custom_string(self, custom_string):
        """Sets the custom_string of this PostDirectMail.

        A custom string for your own reference  # noqa: E501

        :param custom_string: The custom_string of this PostDirectMail.  # noqa: E501
        :type: str
        """

        self._custom_string = custom_string

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(PostDirectMail, dict):
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
        if not isinstance(other, PostDirectMail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
