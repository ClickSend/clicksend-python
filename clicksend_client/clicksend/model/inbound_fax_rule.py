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


class InboundFAXRule(object):
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
        'dedicated_number': 'str',
        'rule_name': 'str',
        'action': 'str',
        'action_address': 'str',
        'enabled': 'float'
    }

    attribute_map = {
        'dedicated_number': 'dedicated_number',
        'rule_name': 'rule_name',
        'action': 'action',
        'action_address': 'action_address',
        'enabled': 'enabled'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, dedicated_number=None, rule_name=None, action=None, action_address=None, enabled=None):  # noqa: E501
        """InboundFAXRule - a model defined in Swagger"""  # noqa: E501

        self._dedicated_number = None
        self._rule_name = None
        self._action = None
        self._action_address = None
        self._enabled = None
        self.discriminator = 'classType'

        self.dedicated_number = dedicated_number
        self.rule_name = rule_name
        self.action = action
        self.action_address = action_address
        self.enabled = enabled

    @property
    def dedicated_number(self):
        """Gets the dedicated_number of this InboundFAXRule.  # noqa: E501

        Dedicated Number. Can be '*' to apply to all numbers.  # noqa: E501

        :return: The dedicated_number of this InboundFAXRule.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_number

    @dedicated_number.setter
    def dedicated_number(self, dedicated_number):
        """Sets the dedicated_number of this InboundFAXRule.

        Dedicated Number. Can be '*' to apply to all numbers.  # noqa: E501

        :param dedicated_number: The dedicated_number of this InboundFAXRule.  # noqa: E501
        :type: str
        """
        if dedicated_number is None:
            raise ValueError("Invalid value for `dedicated_number`, must not be `None`")  # noqa: E501

        self._dedicated_number = dedicated_number

    @property
    def rule_name(self):
        """Gets the rule_name of this InboundFAXRule.  # noqa: E501

        Rule Name.  # noqa: E501

        :return: The rule_name of this InboundFAXRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this InboundFAXRule.

        Rule Name.  # noqa: E501

        :param rule_name: The rule_name of this InboundFAXRule.  # noqa: E501
        :type: str
        """
        if rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def action(self):
        """Gets the action of this InboundFAXRule.  # noqa: E501

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :return: The action of this InboundFAXRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InboundFAXRule.

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :param action: The action of this InboundFAXRule.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def action_address(self):
        """Gets the action_address of this InboundFAXRule.  # noqa: E501

        Action address.  # noqa: E501

        :return: The action_address of this InboundFAXRule.  # noqa: E501
        :rtype: str
        """
        return self._action_address

    @action_address.setter
    def action_address(self, action_address):
        """Sets the action_address of this InboundFAXRule.

        Action address.  # noqa: E501

        :param action_address: The action_address of this InboundFAXRule.  # noqa: E501
        :type: str
        """
        if action_address is None:
            raise ValueError("Invalid value for `action_address`, must not be `None`")  # noqa: E501

        self._action_address = action_address

    @property
    def enabled(self):
        """Gets the enabled of this InboundFAXRule.  # noqa: E501

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :return: The enabled of this InboundFAXRule.  # noqa: E501
        :rtype: float
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InboundFAXRule.

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :param enabled: The enabled of this InboundFAXRule.  # noqa: E501
        :type: float
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if issubclass(InboundFAXRule, dict):
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
        if not isinstance(other, InboundFAXRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
