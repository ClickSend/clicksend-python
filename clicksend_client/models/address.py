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


class Address(object):
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
        'address_name': 'str',
        'address_line_1': 'str',
        'address_city': 'str',
        'address_postal_code': 'str',
        'address_country': 'str',
        'address_line_2': 'str',
        'address_state': 'str'
    }

    attribute_map = {
        'address_name': 'address_name',
        'address_line_1': 'address_line_1',
        'address_city': 'address_city',
        'address_postal_code': 'address_postal_code',
        'address_country': 'address_country',
        'address_line_2': 'address_line_2',
        'address_state': 'address_state'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, address_name=None, address_line_1=None, address_city=None, address_postal_code=None, address_country=None, address_line_2=None, address_state=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501

        self._address_name = None
        self._address_line_1 = None
        self._address_city = None
        self._address_postal_code = None
        self._address_country = None
        self._address_line_2 = None
        self._address_state = None
        self.discriminator = 'classType'

        self.address_name = address_name
        self.address_line_1 = address_line_1
        self.address_city = address_city
        self.address_postal_code = address_postal_code
        self.address_country = address_country
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if address_state is not None:
            self.address_state = address_state

    @property
    def address_name(self):
        """Gets the address_name of this Address.  # noqa: E501

        Your address name.  # noqa: E501

        :return: The address_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_name

    @address_name.setter
    def address_name(self, address_name):
        """Sets the address_name of this Address.

        Your address name.  # noqa: E501

        :param address_name: The address_name of this Address.  # noqa: E501
        :type: str
        """
        if address_name is None:
            raise ValueError("Invalid value for `address_name`, must not be `None`")  # noqa: E501

        self._address_name = address_name

    @property
    def address_line_1(self):
        """Gets the address_line_1 of this Address.  # noqa: E501

        Your address line 1  # noqa: E501

        :return: The address_line_1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        """Sets the address_line_1 of this Address.

        Your address line 1  # noqa: E501

        :param address_line_1: The address_line_1 of this Address.  # noqa: E501
        :type: str
        """
        if address_line_1 is None:
            raise ValueError("Invalid value for `address_line_1`, must not be `None`")  # noqa: E501

        self._address_line_1 = address_line_1

    @property
    def address_city(self):
        """Gets the address_city of this Address.  # noqa: E501

        Your city  # noqa: E501

        :return: The address_city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this Address.

        Your city  # noqa: E501

        :param address_city: The address_city of this Address.  # noqa: E501
        :type: str
        """
        if address_city is None:
            raise ValueError("Invalid value for `address_city`, must not be `None`")  # noqa: E501

        self._address_city = address_city

    @property
    def address_postal_code(self):
        """Gets the address_postal_code of this Address.  # noqa: E501

        Your postal code  # noqa: E501

        :return: The address_postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_postal_code

    @address_postal_code.setter
    def address_postal_code(self, address_postal_code):
        """Sets the address_postal_code of this Address.

        Your postal code  # noqa: E501

        :param address_postal_code: The address_postal_code of this Address.  # noqa: E501
        :type: str
        """
        if address_postal_code is None:
            raise ValueError("Invalid value for `address_postal_code`, must not be `None`")  # noqa: E501

        self._address_postal_code = address_postal_code

    @property
    def address_country(self):
        """Gets the address_country of this Address.  # noqa: E501

        Your country  # noqa: E501

        :return: The address_country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this Address.

        Your country  # noqa: E501

        :param address_country: The address_country of this Address.  # noqa: E501
        :type: str
        """
        if address_country is None:
            raise ValueError("Invalid value for `address_country`, must not be `None`")  # noqa: E501

        self._address_country = address_country

    @property
    def address_line_2(self):
        """Gets the address_line_2 of this Address.  # noqa: E501

        Your address line 2  # noqa: E501

        :return: The address_line_2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        """Sets the address_line_2 of this Address.

        Your address line 2  # noqa: E501

        :param address_line_2: The address_line_2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line_2 = address_line_2

    @property
    def address_state(self):
        """Gets the address_state of this Address.  # noqa: E501

        Your state  # noqa: E501

        :return: The address_state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """Sets the address_state of this Address.

        Your state  # noqa: E501

        :param address_state: The address_state of this Address.  # noqa: E501
        :type: str
        """

        self._address_state = address_state

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
