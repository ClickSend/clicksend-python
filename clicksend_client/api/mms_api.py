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


class MMSApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def mms_price_post(self, mms_messages, **kwargs):  # noqa: E501
        """Get Price for MMS sent  # noqa: E501

        Get Price for MMS sent  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mms_price_post(mms_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MmsMessageCollection mms_messages: MmsMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mms_price_post_with_http_info(mms_messages, **kwargs)  # noqa: E501
        else:
            (data) = self.mms_price_post_with_http_info(mms_messages, **kwargs)  # noqa: E501
            return data

    def mms_price_post_with_http_info(self, mms_messages, **kwargs):  # noqa: E501
        """Get Price for MMS sent  # noqa: E501

        Get Price for MMS sent  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mms_price_post_with_http_info(mms_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MmsMessageCollection mms_messages: MmsMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mms_messages']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mms_price_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mms_messages' is set
        if ('mms_messages' not in params or
                params['mms_messages'] is None):
            raise ValueError("Missing the required parameter `mms_messages` when calling `mms_price_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mms_messages' in params:
            body_params = params['mms_messages']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mms/price', 'POST',
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

    def mms_send_post(self, mms_messages, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mms_send_post(mms_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MmsMessageCollection mms_messages: MmsMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mms_send_post_with_http_info(mms_messages, **kwargs)  # noqa: E501
        else:
            (data) = self.mms_send_post_with_http_info(mms_messages, **kwargs)  # noqa: E501
            return data

    def mms_send_post_with_http_info(self, mms_messages, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mms_send_post_with_http_info(mms_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MmsMessageCollection mms_messages: MmsMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mms_messages']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mms_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mms_messages' is set
        if ('mms_messages' not in params or
                params['mms_messages'] is None):
            raise ValueError("Missing the required parameter `mms_messages` when calling `mms_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mms_messages' in params:
            body_params = params['mms_messages']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mms/send', 'POST',
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
