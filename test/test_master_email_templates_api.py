# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.master_email_templates_api import MasterEmailTemplatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMasterEmailTemplatesApi(unittest.TestCase):
    """MasterEmailTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.master_email_templates_api.MasterEmailTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_master_email_template_categories_get(self):
        """Test case for master_email_template_categories_get

        Get all master email template categories  # noqa: E501
        """
        pass

    def test_master_email_template_category_get(self):
        """Test case for master_email_template_category_get

        Get specific master email template category  # noqa: E501
        """
        pass

    def test_master_email_template_get(self):
        """Test case for master_email_template_get

        Get specific master email template  # noqa: E501
        """
        pass

    def test_master_email_templates_get(self):
        """Test case for master_email_templates_get

        Get all master email templates  # noqa: E501
        """
        pass

    def test_master_email_templates_in_category_get(self):
        """Test case for master_email_templates_in_category_get

        Get all master email templates in a category  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
