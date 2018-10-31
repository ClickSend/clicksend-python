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


class ResellerAccountTransferCredit(object):
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
        'client_user_id': 'int',
        'balance': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'client_user_id': 'client_user_id',
        'balance': 'balance',
        'currency': 'currency'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, client_user_id=None, balance=None, currency=None):  # noqa: E501
        """ResellerAccountTransferCredit - a model defined in Swagger"""  # noqa: E501

        self._client_user_id = None
        self._balance = None
        self._currency = None
        self.discriminator = 'classType'

        self.client_user_id = client_user_id
        self.balance = balance
        self.currency = currency

    @property
    def client_user_id(self):
        """Gets the client_user_id of this ResellerAccountTransferCredit.  # noqa: E501

        User ID of client  # noqa: E501

        :return: The client_user_id of this ResellerAccountTransferCredit.  # noqa: E501
        :rtype: int
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this ResellerAccountTransferCredit.

        User ID of client  # noqa: E501

        :param client_user_id: The client_user_id of this ResellerAccountTransferCredit.  # noqa: E501
        :type: int
        """
        if client_user_id is None:
            raise ValueError("Invalid value for `client_user_id`, must not be `None`")  # noqa: E501

        self._client_user_id = client_user_id

    @property
    def balance(self):
        """Gets the balance of this ResellerAccountTransferCredit.  # noqa: E501

        Balance to transfer  # noqa: E501

        :return: The balance of this ResellerAccountTransferCredit.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ResellerAccountTransferCredit.

        Balance to transfer  # noqa: E501

        :param balance: The balance of this ResellerAccountTransferCredit.  # noqa: E501
        :type: int
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this ResellerAccountTransferCredit.  # noqa: E501

        Currency of balance to transfer  # noqa: E501

        :return: The currency of this ResellerAccountTransferCredit.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ResellerAccountTransferCredit.

        Currency of balance to transfer  # noqa: E501

        :param currency: The currency of this ResellerAccountTransferCredit.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if issubclass(ResellerAccountTransferCredit, dict):
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
        if not isinstance(other, ResellerAccountTransferCredit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
