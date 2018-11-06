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
from clicksend.api.email_marketing_api import EmailMarketingApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestEmailMarketingApi(unittest.TestCase):
    """EmailMarketingApi unit test stubs"""

    def setUp(self):
        self.api = clicksend.api.email_marketing_api.EmailMarketingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allowed_email_address_get(self):
        """Test case for allowed_email_address_get

        Get all email addresses  # noqa: E501
        """
        pass

    def test_allowed_email_address_post(self):
        """Test case for allowed_email_address_post

        Create allowed Email Address  # noqa: E501
        """
        pass

    def test_cancel_email_campaign_put(self):
        """Test case for cancel_email_campaign_put

        Cancel email campaign  # noqa: E501
        """
        pass

    def test_email_campaign_get(self):
        """Test case for email_campaign_get

        Get specific email campaign  # noqa: E501
        """
        pass

    def test_email_campaign_history_export_get(self):
        """Test case for email_campaign_history_export_get

        Export specific email campaign history  # noqa: E501
        """
        pass

    def test_email_campaign_history_get(self):
        """Test case for email_campaign_history_get

        Get specific email campaign history  # noqa: E501
        """
        pass

    def test_email_campaign_post(self):
        """Test case for email_campaign_post

        Send email campaign  # noqa: E501
        """
        pass

    def test_email_campaign_price_post(self):
        """Test case for email_campaign_price_post

        Calculate email campaign price  # noqa: E501
        """
        pass

    def test_email_campaign_put(self):
        """Test case for email_campaign_put

        Edit email campaign  # noqa: E501
        """
        pass

    def test_email_campaigns_get(self):
        """Test case for email_campaigns_get

        Get all email campaigns  # noqa: E501
        """
        pass

    def test_send_verification_token_get(self):
        """Test case for send_verification_token_get

        Send verification token  # noqa: E501
        """
        pass

    def test_specific_allowed_email_address_delete(self):
        """Test case for specific_allowed_email_address_delete

        Delete specific email address  # noqa: E501
        """
        pass

    def test_specific_allowed_email_address_get(self):
        """Test case for specific_allowed_email_address_get

        Get specific email address  # noqa: E501
        """
        pass

    def test_verify_allowed_email_address_get(self):
        """Test case for verify_allowed_email_address_get

        Verify email address using verification token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
