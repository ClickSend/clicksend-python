# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import unittest

import clicksend_client
from clicksend_client.api.inbound_sms_rules_api import InboundSMSRulesApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestInboundSMSRulesApi(unittest.TestCase):
    """InboundSMSRulesApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.inbound_sms_rules_api.InboundSMSRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sms_inbound_automation_delete(self):
        """Test case for sms_inbound_automation_delete

        Delete inbound sms automation  # noqa: E501
        """
        pass

    def test_sms_inbound_automation_get(self):
        """Test case for sms_inbound_automation_get

        Get specific inbound sms automation  # noqa: E501
        """
        pass

    def test_sms_inbound_automation_post(self):
        """Test case for sms_inbound_automation_post

        Create new inbound sms automation  # noqa: E501
        """
        pass

    def test_sms_inbound_automation_put(self):
        """Test case for sms_inbound_automation_put

        Update inbound sms automation  # noqa: E501
        """
        pass

    def test_sms_inbound_automations_get(self):
        """Test case for sms_inbound_automations_get

        Get all inbound sms automations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
