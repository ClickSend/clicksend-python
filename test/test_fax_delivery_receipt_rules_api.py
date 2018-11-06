# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import unittest

import clicksend_client
from clicksend.api.fax_delivery_receipt_rules_api import FAXDeliveryReceiptRulesApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestFAXDeliveryReceiptRulesApi(unittest.TestCase):
    """FAXDeliveryReceiptRulesApi unit test stubs"""

    def setUp(self):
        self.api = clicksend.api.fax_delivery_receipt_rules_api.FAXDeliveryReceiptRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fax_delivery_receipt_automation_delete(self):
        """Test case for fax_delivery_receipt_automation_delete

        Delete fax delivery receipt automation  # noqa: E501
        """
        pass

    def test_fax_delivery_receipt_automation_get(self):
        """Test case for fax_delivery_receipt_automation_get

        Get specific fax delivery receipt automation  # noqa: E501
        """
        pass

    def test_fax_delivery_receipt_automation_post(self):
        """Test case for fax_delivery_receipt_automation_post

        Create fax delivery receipt automations  # noqa: E501
        """
        pass

    def test_fax_delivery_receipt_automation_put(self):
        """Test case for fax_delivery_receipt_automation_put

        Update fax delivery receipt automation  # noqa: E501
        """
        pass

    def test_fax_delivery_receipt_automations_get(self):
        """Test case for fax_delivery_receipt_automations_get

        Get all fax delivery receipt automations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
