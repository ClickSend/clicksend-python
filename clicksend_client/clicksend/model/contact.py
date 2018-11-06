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


class Contact(object):
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
        'phone_number': 'str',
        'custom_1': 'str',
        'email': 'str',
        'fax_number': 'str',
        'first_name': 'str',
        'address_line_1': 'str',
        'address_line_2': 'str',
        'address_city': 'str',
        'address_state': 'str',
        'address_postal_code': 'str',
        'address_country': 'str',
        'organization_name': 'str',
        'custom_2': 'str',
        'custom_3': 'str',
        'custom_4': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'phone_number': 'phone_number',
        'custom_1': 'custom_1',
        'email': 'email',
        'fax_number': 'fax_number',
        'first_name': 'first_name',
        'address_line_1': 'address_line_1',
        'address_line_2': 'address_line_2',
        'address_city': 'address_city',
        'address_state': 'address_state',
        'address_postal_code': 'address_postal_code',
        'address_country': 'address_country',
        'organization_name': 'organization_name',
        'custom_2': 'custom_2',
        'custom_3': 'custom_3',
        'custom_4': 'custom_4',
        'last_name': 'last_name'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, phone_number=None, custom_1=None, email=None, fax_number=None, first_name=None, address_line_1=None, address_line_2=None, address_city=None, address_state=None, address_postal_code=None, address_country=None, organization_name=None, custom_2=None, custom_3=None, custom_4=None, last_name=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._phone_number = None
        self._custom_1 = None
        self._email = None
        self._fax_number = None
        self._first_name = None
        self._address_line_1 = None
        self._address_line_2 = None
        self._address_city = None
        self._address_state = None
        self._address_postal_code = None
        self._address_country = None
        self._organization_name = None
        self._custom_2 = None
        self._custom_3 = None
        self._custom_4 = None
        self._last_name = None
        self.discriminator = 'classType'

        self.phone_number = phone_number
        self.custom_1 = custom_1
        if email is not None:
            self.email = email
        if fax_number is not None:
            self.fax_number = fax_number
        if first_name is not None:
            self.first_name = first_name
        if address_line_1 is not None:
            self.address_line_1 = address_line_1
        if address_line_2 is not None:
            self.address_line_2 = address_line_2
        if address_city is not None:
            self.address_city = address_city
        if address_state is not None:
            self.address_state = address_state
        if address_postal_code is not None:
            self.address_postal_code = address_postal_code
        if address_country is not None:
            self.address_country = address_country
        if organization_name is not None:
            self.organization_name = organization_name
        if custom_2 is not None:
            self.custom_2 = custom_2
        if custom_3 is not None:
            self.custom_3 = custom_3
        if custom_4 is not None:
            self.custom_4 = custom_4
        if last_name is not None:
            self.last_name = last_name

    @property
    def phone_number(self):
        """Gets the phone_number of this Contact.  # noqa: E501

        Your phone number in E.164 format. Must be provided if no fax number or email.  # noqa: E501

        :return: The phone_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Contact.

        Your phone number in E.164 format. Must be provided if no fax number or email.  # noqa: E501

        :param phone_number: The phone_number of this Contact.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def custom_1(self):
        """Gets the custom_1 of this Contact.  # noqa: E501

          # noqa: E501

        :return: The custom_1 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._custom_1

    @custom_1.setter
    def custom_1(self, custom_1):
        """Sets the custom_1 of this Contact.

          # noqa: E501

        :param custom_1: The custom_1 of this Contact.  # noqa: E501
        :type: str
        """
        if custom_1 is None:
            raise ValueError("Invalid value for `custom_1`, must not be `None`")  # noqa: E501

        self._custom_1 = custom_1

    @property
    def email(self):
        """Gets the email of this Contact.  # noqa: E501

        Your email. Must be provided if no phone number or fax number.  # noqa: E501

        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.

        Your email. Must be provided if no phone number or fax number.  # noqa: E501

        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fax_number(self):
        """Gets the fax_number of this Contact.  # noqa: E501

        Your fax number. Must be provided if no phone number or email.  # noqa: E501

        :return: The fax_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this Contact.

        Your fax number. Must be provided if no phone number or email.  # noqa: E501

        :param fax_number: The fax_number of this Contact.  # noqa: E501
        :type: str
        """

        self._fax_number = fax_number

    @property
    def first_name(self):
        """Gets the first_name of this Contact.  # noqa: E501

        Your first name.  # noqa: E501

        :return: The first_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Contact.

        Your first name.  # noqa: E501

        :param first_name: The first_name of this Contact.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def address_line_1(self):
        """Gets the address_line_1 of this Contact.  # noqa: E501

        Your street address  # noqa: E501

        :return: The address_line_1 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1):
        """Sets the address_line_1 of this Contact.

        Your street address  # noqa: E501

        :param address_line_1: The address_line_1 of this Contact.  # noqa: E501
        :type: str
        """

        self._address_line_1 = address_line_1

    @property
    def address_line_2(self):
        """Gets the address_line_2 of this Contact.  # noqa: E501

          # noqa: E501

        :return: The address_line_2 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2):
        """Sets the address_line_2 of this Contact.

          # noqa: E501

        :param address_line_2: The address_line_2 of this Contact.  # noqa: E501
        :type: str
        """

        self._address_line_2 = address_line_2

    @property
    def address_city(self):
        """Gets the address_city of this Contact.  # noqa: E501

        Your nearest city  # noqa: E501

        :return: The address_city of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this Contact.

        Your nearest city  # noqa: E501

        :param address_city: The address_city of this Contact.  # noqa: E501
        :type: str
        """

        self._address_city = address_city

    @property
    def address_state(self):
        """Gets the address_state of this Contact.  # noqa: E501

        Your current state  # noqa: E501

        :return: The address_state of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """Sets the address_state of this Contact.

        Your current state  # noqa: E501

        :param address_state: The address_state of this Contact.  # noqa: E501
        :type: str
        """

        self._address_state = address_state

    @property
    def address_postal_code(self):
        """Gets the address_postal_code of this Contact.  # noqa: E501

        Your current postcode  # noqa: E501

        :return: The address_postal_code of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_postal_code

    @address_postal_code.setter
    def address_postal_code(self, address_postal_code):
        """Sets the address_postal_code of this Contact.

        Your current postcode  # noqa: E501

        :param address_postal_code: The address_postal_code of this Contact.  # noqa: E501
        :type: str
        """

        self._address_postal_code = address_postal_code

    @property
    def address_country(self):
        """Gets the address_country of this Contact.  # noqa: E501

        Your current country  # noqa: E501

        :return: The address_country of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this Contact.

        Your current country  # noqa: E501

        :param address_country: The address_country of this Contact.  # noqa: E501
        :type: str
        """

        self._address_country = address_country

    @property
    def organization_name(self):
        """Gets the organization_name of this Contact.  # noqa: E501

        Your organisation name  # noqa: E501

        :return: The organization_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this Contact.

        Your organisation name  # noqa: E501

        :param organization_name: The organization_name of this Contact.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def custom_2(self):
        """Gets the custom_2 of this Contact.  # noqa: E501

          # noqa: E501

        :return: The custom_2 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._custom_2

    @custom_2.setter
    def custom_2(self, custom_2):
        """Sets the custom_2 of this Contact.

          # noqa: E501

        :param custom_2: The custom_2 of this Contact.  # noqa: E501
        :type: str
        """

        self._custom_2 = custom_2

    @property
    def custom_3(self):
        """Gets the custom_3 of this Contact.  # noqa: E501

          # noqa: E501

        :return: The custom_3 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._custom_3

    @custom_3.setter
    def custom_3(self, custom_3):
        """Sets the custom_3 of this Contact.

          # noqa: E501

        :param custom_3: The custom_3 of this Contact.  # noqa: E501
        :type: str
        """

        self._custom_3 = custom_3

    @property
    def custom_4(self):
        """Gets the custom_4 of this Contact.  # noqa: E501

          # noqa: E501

        :return: The custom_4 of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._custom_4

    @custom_4.setter
    def custom_4(self, custom_4):
        """Sets the custom_4 of this Contact.

          # noqa: E501

        :param custom_4: The custom_4 of this Contact.  # noqa: E501
        :type: str
        """

        self._custom_4 = custom_4

    @property
    def last_name(self):
        """Gets the last_name of this Contact.  # noqa: E501

        Your last name  # noqa: E501

        :return: The last_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Contact.

        Your last name  # noqa: E501

        :param last_name: The last_name of this Contact.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
