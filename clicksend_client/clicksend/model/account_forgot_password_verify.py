# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountForgotPasswordVerify(object):
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
        'subaccount_id': 'int',
        'activation_token': 'str',
        'password': 'str'
    }

    attribute_map = {
        'subaccount_id': 'subaccount_id',
        'activation_token': 'activation_token',
        'password': 'password'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, subaccount_id=None, activation_token=None, password=None):  # noqa: E501
        """AccountForgotPasswordVerify - a model defined in Swagger"""  # noqa: E501

        self._subaccount_id = None
        self._activation_token = None
        self._password = None
        self.discriminator = 'classType'

        self.subaccount_id = subaccount_id
        self.activation_token = activation_token
        self.password = password

    @property
    def subaccount_id(self):
        """Gets the subaccount_id of this AccountForgotPasswordVerify.  # noqa: E501

        ID of subaccount  # noqa: E501

        :return: The subaccount_id of this AccountForgotPasswordVerify.  # noqa: E501
        :rtype: int
        """
        return self._subaccount_id

    @subaccount_id.setter
    def subaccount_id(self, subaccount_id):
        """Sets the subaccount_id of this AccountForgotPasswordVerify.

        ID of subaccount  # noqa: E501

        :param subaccount_id: The subaccount_id of this AccountForgotPasswordVerify.  # noqa: E501
        :type: int
        """
        if subaccount_id is None:
            raise ValueError("Invalid value for `subaccount_id`, must not be `None`")  # noqa: E501

        self._subaccount_id = subaccount_id

    @property
    def activation_token(self):
        """Gets the activation_token of this AccountForgotPasswordVerify.  # noqa: E501

        Activation token  # noqa: E501

        :return: The activation_token of this AccountForgotPasswordVerify.  # noqa: E501
        :rtype: str
        """
        return self._activation_token

    @activation_token.setter
    def activation_token(self, activation_token):
        """Sets the activation_token of this AccountForgotPasswordVerify.

        Activation token  # noqa: E501

        :param activation_token: The activation_token of this AccountForgotPasswordVerify.  # noqa: E501
        :type: str
        """
        if activation_token is None:
            raise ValueError("Invalid value for `activation_token`, must not be `None`")  # noqa: E501

        self._activation_token = activation_token

    @property
    def password(self):
        """Gets the password of this AccountForgotPasswordVerify.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this AccountForgotPasswordVerify.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccountForgotPasswordVerify.

        Password  # noqa: E501

        :param password: The password of this AccountForgotPasswordVerify.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if issubclass(AccountForgotPasswordVerify, dict):
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
        if not isinstance(other, AccountForgotPasswordVerify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
