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


class Account(object):
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
        'username': 'str',
        'password': 'str',
        'user_phone': 'str',
        'user_email': 'str',
        'user_first_name': 'str',
        'user_last_name': 'str',
        'account_name': 'str',
        'country': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'user_phone': 'user_phone',
        'user_email': 'user_email',
        'user_first_name': 'user_first_name',
        'user_last_name': 'user_last_name',
        'account_name': 'account_name',
        'country': 'country'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, username=None, password=None, user_phone=None, user_email=None, user_first_name=None, user_last_name=None, account_name=None, country=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._user_phone = None
        self._user_email = None
        self._user_first_name = None
        self._user_last_name = None
        self._account_name = None
        self._country = None
        self.discriminator = 'classType'

        self.username = username
        self.password = password
        self.user_phone = user_phone
        self.user_email = user_email
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.account_name = account_name
        self.country = country

    @property
    def username(self):
        """Gets the username of this Account.  # noqa: E501

        Your username  # noqa: E501

        :return: The username of this Account.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Account.

        Your username  # noqa: E501

        :param username: The username of this Account.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this Account.  # noqa: E501

        Your password  # noqa: E501

        :return: The password of this Account.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Account.

        Your password  # noqa: E501

        :param password: The password of this Account.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def user_phone(self):
        """Gets the user_phone of this Account.  # noqa: E501

        Your phone number in E.164 format.  # noqa: E501

        :return: The user_phone of this Account.  # noqa: E501
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        """Sets the user_phone of this Account.

        Your phone number in E.164 format.  # noqa: E501

        :param user_phone: The user_phone of this Account.  # noqa: E501
        :type: str
        """
        if user_phone is None:
            raise ValueError("Invalid value for `user_phone`, must not be `None`")  # noqa: E501

        self._user_phone = user_phone

    @property
    def user_email(self):
        """Gets the user_email of this Account.  # noqa: E501

        Your email  # noqa: E501

        :return: The user_email of this Account.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this Account.

        Your email  # noqa: E501

        :param user_email: The user_email of this Account.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_first_name(self):
        """Gets the user_first_name of this Account.  # noqa: E501

        Your first name  # noqa: E501

        :return: The user_first_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._user_first_name

    @user_first_name.setter
    def user_first_name(self, user_first_name):
        """Sets the user_first_name of this Account.

        Your first name  # noqa: E501

        :param user_first_name: The user_first_name of this Account.  # noqa: E501
        :type: str
        """
        if user_first_name is None:
            raise ValueError("Invalid value for `user_first_name`, must not be `None`")  # noqa: E501

        self._user_first_name = user_first_name

    @property
    def user_last_name(self):
        """Gets the user_last_name of this Account.  # noqa: E501

        Your last name  # noqa: E501

        :return: The user_last_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._user_last_name

    @user_last_name.setter
    def user_last_name(self, user_last_name):
        """Sets the user_last_name of this Account.

        Your last name  # noqa: E501

        :param user_last_name: The user_last_name of this Account.  # noqa: E501
        :type: str
        """
        if user_last_name is None:
            raise ValueError("Invalid value for `user_last_name`, must not be `None`")  # noqa: E501

        self._user_last_name = user_last_name

    @property
    def account_name(self):
        """Gets the account_name of this Account.  # noqa: E501

        Your delivery to value.  # noqa: E501

        :return: The account_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this Account.

        Your delivery to value.  # noqa: E501

        :param account_name: The account_name of this Account.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def country(self):
        """Gets the country of this Account.  # noqa: E501

        Your country  # noqa: E501

        :return: The country of this Account.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Account.

        Your country  # noqa: E501

        :param country: The country of this Account.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
