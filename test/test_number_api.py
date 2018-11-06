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
from clicksend.api.number_api import NumberApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestNumberApi(unittest.TestCase):
    """NumberApi unit test stubs"""

    def setUp(self):
        self.api = clicksend.api.number_api.NumberApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_numbers_buy_by_dedicated_number_post(self):
        """Test case for numbers_buy_by_dedicated_number_post

        Buy dedicated number  # noqa: E501
        """
        pass

    def test_numbers_get(self):
        """Test case for numbers_get

        Get all availible dedicated numbers  # noqa: E501
        """
        pass

    def test_numbers_search_by_country_get(self):
        """Test case for numbers_search_by_country_get

        Get all dedicated numbers by country  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
