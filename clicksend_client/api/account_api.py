# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clicksend_client.api_client import ApiClient


class AccountApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_get(self, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        Get account details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        Get account details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_post(self, account, **kwargs):  # noqa: E501
        """Create a new account  # noqa: E501

        Create An Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_post(account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account account: Account model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_post_with_http_info(account, **kwargs)  # noqa: E501
        else:
            (data) = self.account_post_with_http_info(account, **kwargs)  # noqa: E501
            return data

    def account_post_with_http_info(self, account, **kwargs):  # noqa: E501
        """Create a new account  # noqa: E501

        Create An Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_post_with_http_info(account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account account: Account model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account' is set
        if self.api_client.client_side_validation and ('account' not in params or
                                                       params['account'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account` when calling `account_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account' in params:
            body_params = params['account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_useage_by_subaccount_get(self, year, month, **kwargs):  # noqa: E501
        """Get account useage by subaccount  # noqa: E501

        Get account useage by subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_useage_by_subaccount_get(year, month, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year to filter by (yyyy) (required)
        :param int month: Month to filter by (mm) (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_useage_by_subaccount_get_with_http_info(year, month, **kwargs)  # noqa: E501
        else:
            (data) = self.account_useage_by_subaccount_get_with_http_info(year, month, **kwargs)  # noqa: E501
            return data

    def account_useage_by_subaccount_get_with_http_info(self, year, month, **kwargs):  # noqa: E501
        """Get account useage by subaccount  # noqa: E501

        Get account useage by subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_useage_by_subaccount_get_with_http_info(year, month, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year to filter by (yyyy) (required)
        :param int month: Month to filter by (mm) (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'month']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_useage_by_subaccount_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `account_useage_by_subaccount_get`")  # noqa: E501
        # verify the required parameter 'month' is set
        if self.api_client.client_side_validation and ('month' not in params or
                                                       params['month'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `month` when calling `account_useage_by_subaccount_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
        if 'month' in params:
            path_params['month'] = params['month']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/usage/{year}/{month}/subaccount', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_verify_send_put(self, account_verify, **kwargs):  # noqa: E501
        """Send account activation token  # noqa: E501

        Send account activation token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_send_put(account_verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountVerify account_verify: Account details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_verify_send_put_with_http_info(account_verify, **kwargs)  # noqa: E501
        else:
            (data) = self.account_verify_send_put_with_http_info(account_verify, **kwargs)  # noqa: E501
            return data

    def account_verify_send_put_with_http_info(self, account_verify, **kwargs):  # noqa: E501
        """Send account activation token  # noqa: E501

        Send account activation token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_send_put_with_http_info(account_verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountVerify account_verify: Account details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_verify']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_verify_send_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_verify' is set
        if self.api_client.client_side_validation and ('account_verify' not in params or
                                                       params['account_verify'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_verify` when calling `account_verify_send_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_verify' in params:
            body_params = params['account_verify']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account-verify/send', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_verify_verify_by_activation_token_put(self, activation_token, **kwargs):  # noqa: E501
        """Verify new account  # noqa: E501

        Verify new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_verify_by_activation_token_put(activation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activation_token:  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_verify_verify_by_activation_token_put_with_http_info(activation_token, **kwargs)  # noqa: E501
        else:
            (data) = self.account_verify_verify_by_activation_token_put_with_http_info(activation_token, **kwargs)  # noqa: E501
            return data

    def account_verify_verify_by_activation_token_put_with_http_info(self, activation_token, **kwargs):  # noqa: E501
        """Verify new account  # noqa: E501

        Verify new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_verify_by_activation_token_put_with_http_info(activation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activation_token:  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_verify_verify_by_activation_token_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activation_token' is set
        if self.api_client.client_side_validation and ('activation_token' not in params or
                                                       params['activation_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `activation_token` when calling `account_verify_verify_by_activation_token_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activation_token' in params:
            path_params['activation_token'] = params['activation_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account-verify/verify/{activation_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def forgot_password_put(self, **kwargs):  # noqa: E501
        """Forgot password  # noqa: E501

        Forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPassword forgot_password:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_password_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.forgot_password_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def forgot_password_put_with_http_info(self, **kwargs):  # noqa: E501
        """Forgot password  # noqa: E501

        Forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPassword forgot_password:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_password_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_password' in params:
            body_params = params['forgot_password']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/forgot-password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def forgot_password_verify_put(self, verify_password, **kwargs):  # noqa: E501
        """Verify forgot password  # noqa: E501

        Verify forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_verify_put(verify_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountForgotPasswordVerify verify_password: verifyPassword data (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_password_verify_put_with_http_info(verify_password, **kwargs)  # noqa: E501
        else:
            (data) = self.forgot_password_verify_put_with_http_info(verify_password, **kwargs)  # noqa: E501
            return data

    def forgot_password_verify_put_with_http_info(self, verify_password, **kwargs):  # noqa: E501
        """Verify forgot password  # noqa: E501

        Verify forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_verify_put_with_http_info(verify_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountForgotPasswordVerify verify_password: verifyPassword data (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verify_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_password_verify_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verify_password' is set
        if self.api_client.client_side_validation and ('verify_password' not in params or
                                                       params['verify_password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `verify_password` when calling `forgot_password_verify_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'verify_password' in params:
            body_params = params['verify_password']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/forgot-password/verify', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def forgot_username_put(self, **kwargs):  # noqa: E501
        """Forgot username  # noqa: E501

        Forgot username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_username_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotUsername forgot_username:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_username_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.forgot_username_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def forgot_username_put_with_http_info(self, **kwargs):  # noqa: E501
        """Forgot username  # noqa: E501

        Forgot username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_username_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotUsername forgot_username:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_username_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_username' in params:
            body_params = params['forgot_username']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forgot-username', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
