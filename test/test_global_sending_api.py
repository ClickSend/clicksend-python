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
from clicksend_client.api.global_sending_api import GlobalSendingApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestGlobalSendingApi(unittest.TestCase):
    """GlobalSendingApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.global_sending_api.GlobalSendingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_countries_get(self):
        """Test case for list_countries_get

        List of countries  # noqa: E501
        """
        pass

    def test_user_countries_agree_post(self):
        """Test case for user_countries_agree_post

        Agree to rules and regulation  # noqa: E501
        """
        pass

    def test_user_countries_get(self):
        """Test case for user_countries_get

        Get Countries for Global Sending  # noqa: E501
        """
        pass

    def test_user_countries_post(self):
        """Test case for user_countries_post

        Select Countries for Global Sending  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
