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


class EmailCampaign(object):
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
        'subject': 'str',
        'body': 'str',
        'from_email_address_id': 'float',
        'from_name': 'str',
        'template_id': 'float',
        'list_id': 'float',
        'schedule': 'int'
    }

    attribute_map = {
        'name': 'name',
        'subject': 'subject',
        'body': 'body',
        'from_email_address_id': 'from_email_address_id',
        'from_name': 'from_name',
        'template_id': 'template_id',
        'list_id': 'list_id',
        'schedule': 'schedule'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, name=None, subject=None, body=None, from_email_address_id=None, from_name=None, template_id=None, list_id=None, schedule=0):  # noqa: E501
        """EmailCampaign - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._subject = None
        self._body = None
        self._from_email_address_id = None
        self._from_name = None
        self._template_id = None
        self._list_id = None
        self._schedule = None
        self.discriminator = 'classType'

        self.name = name
        self.subject = subject
        self.body = body
        self.from_email_address_id = from_email_address_id
        self.from_name = from_name
        if template_id is not None:
            self.template_id = template_id
        self.list_id = list_id
        if schedule is not None:
            self.schedule = schedule

    @property
    def name(self):
        """Gets the name of this EmailCampaign.  # noqa: E501

        Your campaign name.  # noqa: E501

        :return: The name of this EmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailCampaign.

        Your campaign name.  # noqa: E501

        :param name: The name of this EmailCampaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this EmailCampaign.  # noqa: E501

        Your campaign subject.  # noqa: E501

        :return: The subject of this EmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailCampaign.

        Your campaign subject.  # noqa: E501

        :param subject: The subject of this EmailCampaign.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this EmailCampaign.  # noqa: E501

        Your campaign message.  # noqa: E501

        :return: The body of this EmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EmailCampaign.

        Your campaign message.  # noqa: E501

        :param body: The body of this EmailCampaign.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def from_email_address_id(self):
        """Gets the from_email_address_id of this EmailCampaign.  # noqa: E501

        The allowed email address id.  # noqa: E501

        :return: The from_email_address_id of this EmailCampaign.  # noqa: E501
        :rtype: float
        """
        return self._from_email_address_id

    @from_email_address_id.setter
    def from_email_address_id(self, from_email_address_id):
        """Sets the from_email_address_id of this EmailCampaign.

        The allowed email address id.  # noqa: E501

        :param from_email_address_id: The from_email_address_id of this EmailCampaign.  # noqa: E501
        :type: float
        """
        if from_email_address_id is None:
            raise ValueError("Invalid value for `from_email_address_id`, must not be `None`")  # noqa: E501

        self._from_email_address_id = from_email_address_id

    @property
    def from_name(self):
        """Gets the from_name of this EmailCampaign.  # noqa: E501

        Your name or business name.  # noqa: E501

        :return: The from_name of this EmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EmailCampaign.

        Your name or business name.  # noqa: E501

        :param from_name: The from_name of this EmailCampaign.  # noqa: E501
        :type: str
        """
        if from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")  # noqa: E501

        self._from_name = from_name

    @property
    def template_id(self):
        """Gets the template_id of this EmailCampaign.  # noqa: E501

        Your template id.  # noqa: E501

        :return: The template_id of this EmailCampaign.  # noqa: E501
        :rtype: float
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this EmailCampaign.

        Your template id.  # noqa: E501

        :param template_id: The template_id of this EmailCampaign.  # noqa: E501
        :type: float
        """

        self._template_id = template_id

    @property
    def list_id(self):
        """Gets the list_id of this EmailCampaign.  # noqa: E501

        Your contact list id.  # noqa: E501

        :return: The list_id of this EmailCampaign.  # noqa: E501
        :rtype: float
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this EmailCampaign.

        Your contact list id.  # noqa: E501

        :param list_id: The list_id of this EmailCampaign.  # noqa: E501
        :type: float
        """
        if list_id is None:
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def schedule(self):
        """Gets the schedule of this EmailCampaign.  # noqa: E501

        Your schedule timestamp.  # noqa: E501

        :return: The schedule of this EmailCampaign.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this EmailCampaign.

        Your schedule timestamp.  # noqa: E501

        :param schedule: The schedule of this EmailCampaign.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

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
        if issubclass(EmailCampaign, dict):
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
        if not isinstance(other, EmailCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
