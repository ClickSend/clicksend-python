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
from clicksend.api.transfer_credit_api import TransferCreditApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestTransferCreditApi(unittest.TestCase):
    """TransferCreditApi unit test stubs"""

    def setUp(self):
        self.api = clicksend.api.transfer_credit_api.TransferCreditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reseller_transfer_credit_put(self):
        """Test case for reseller_transfer_credit_put

        Transfer Credit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
