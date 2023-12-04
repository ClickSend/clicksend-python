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

from clicksend_client.configuration import Configuration


class CountryListIds(object):
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
        'country_list_ids': 'list[int]'
    }

    attribute_map = {
        'country_list_ids': 'country_list_ids'
    }

    def __init__(self, country_list_ids=None, _configuration=None):  # noqa: E501
        """CountryListIds - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country_list_ids = None
        self.discriminator = None

        self.country_list_ids = country_list_ids

    @property
    def country_list_ids(self):
        """Gets the country_list_ids of this CountryListIds.  # noqa: E501

        Array of country ids  # noqa: E501

        :return: The country_list_ids of this CountryListIds.  # noqa: E501
        :rtype: list[int]
        """
        return self._country_list_ids

    @country_list_ids.setter
    def country_list_ids(self, country_list_ids):
        """Sets the country_list_ids of this CountryListIds.

        Array of country ids  # noqa: E501

        :param country_list_ids: The country_list_ids of this CountryListIds.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and country_list_ids is None:
            raise ValueError("Invalid value for `country_list_ids`, must not be `None`")  # noqa: E501

        self._country_list_ids = country_list_ids

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
        if issubclass(CountryListIds, dict):
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
        if not isinstance(other, CountryListIds):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CountryListIds):
            return True

        return self.to_dict() != other.to_dict()