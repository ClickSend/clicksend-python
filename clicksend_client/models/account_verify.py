# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountVerify(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      clicksend_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    clicksend_types = {
        'country': 'str',
        'user_phone': 'str',
        'type': 'str'
    }

    attribute_map = {
        'country': 'country',
        'user_phone': 'user_phone',
        'type': 'type'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, country=None, user_phone=None, type=None):  # noqa: E501
        """AccountVerify - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._user_phone = None
        self._type = None
        self.discriminator = 'classType'

        self.country = country
        self.user_phone = user_phone
        self.type = type

    @property
    def country(self):
        """Gets the country of this AccountVerify.  # noqa: E501

        Country code  # noqa: E501

        :return: The country of this AccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AccountVerify.

        Country code  # noqa: E501

        :param country: The country of this AccountVerify.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def user_phone(self):
        """Gets the user_phone of this AccountVerify.  # noqa: E501

        User's phone number  # noqa: E501

        :return: The user_phone of this AccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        """Sets the user_phone of this AccountVerify.

        User's phone number  # noqa: E501

        :param user_phone: The user_phone of this AccountVerify.  # noqa: E501
        :type: str
        """
        if user_phone is None:
            raise ValueError("Invalid value for `user_phone`, must not be `None`")  # noqa: E501

        self._user_phone = user_phone

    @property
    def type(self):
        """Gets the type of this AccountVerify.  # noqa: E501

        Type of verification  # noqa: E501

        :return: The type of this AccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountVerify.

        Type of verification  # noqa: E501

        :param type: The type of this AccountVerify.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.clicksend_types):
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
        if issubclass(AccountVerify, dict):
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
        if not isinstance(other, AccountVerify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
