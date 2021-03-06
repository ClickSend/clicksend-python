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
from clicksend_client.api.delivery_issues_api import DeliveryIssuesApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestDeliveryIssuesApi(unittest.TestCase):
    """DeliveryIssuesApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.delivery_issues_api.DeliveryIssuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delivery_issues_get(self):
        """Test case for delivery_issues_get

        Get all delivery issues  # noqa: E501
        """
        pass

    def test_delivery_issues_post(self):
        """Test case for delivery_issues_post

        Create delivery Issue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
