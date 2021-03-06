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


class SubaccountApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def subaccounts_by_subaccount_id_delete(self, subaccount_id, **kwargs):  # noqa: E501
        """Delete a subaccount  # noqa: E501

        Delete a subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_delete(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to delete (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_by_subaccount_id_delete_with_http_info(subaccount_id, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_by_subaccount_id_delete_with_http_info(subaccount_id, **kwargs)  # noqa: E501
            return data

    def subaccounts_by_subaccount_id_delete_with_http_info(self, subaccount_id, **kwargs):  # noqa: E501
        """Delete a subaccount  # noqa: E501

        Delete a subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_delete_with_http_info(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to delete (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subaccount_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_by_subaccount_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subaccount_id' is set
        if self.api_client.client_side_validation and ('subaccount_id' not in params or
                                                       params['subaccount_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount_id` when calling `subaccounts_by_subaccount_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subaccount_id' in params:
            path_params['subaccount_id'] = params['subaccount_id']  # noqa: E501

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
            '/subaccounts/{subaccount_id}', 'DELETE',
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

    def subaccounts_by_subaccount_id_get(self, subaccount_id, **kwargs):  # noqa: E501
        """Get specific subaccount  # noqa: E501

        Get specific subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_get(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to get (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_by_subaccount_id_get_with_http_info(subaccount_id, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_by_subaccount_id_get_with_http_info(subaccount_id, **kwargs)  # noqa: E501
            return data

    def subaccounts_by_subaccount_id_get_with_http_info(self, subaccount_id, **kwargs):  # noqa: E501
        """Get specific subaccount  # noqa: E501

        Get specific subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_get_with_http_info(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to get (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subaccount_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_by_subaccount_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subaccount_id' is set
        if self.api_client.client_side_validation and ('subaccount_id' not in params or
                                                       params['subaccount_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount_id` when calling `subaccounts_by_subaccount_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subaccount_id' in params:
            path_params['subaccount_id'] = params['subaccount_id']  # noqa: E501

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
            '/subaccounts/{subaccount_id}', 'GET',
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

    def subaccounts_by_subaccount_id_put(self, subaccount_id, subaccount, **kwargs):  # noqa: E501
        """Update subaccount  # noqa: E501

        Update subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_put(subaccount_id, subaccount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to update (required)
        :param Subaccount subaccount: Subaccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_by_subaccount_id_put_with_http_info(subaccount_id, subaccount, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_by_subaccount_id_put_with_http_info(subaccount_id, subaccount, **kwargs)  # noqa: E501
            return data

    def subaccounts_by_subaccount_id_put_with_http_info(self, subaccount_id, subaccount, **kwargs):  # noqa: E501
        """Update subaccount  # noqa: E501

        Update subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_by_subaccount_id_put_with_http_info(subaccount_id, subaccount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to update (required)
        :param Subaccount subaccount: Subaccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subaccount_id', 'subaccount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_by_subaccount_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subaccount_id' is set
        if self.api_client.client_side_validation and ('subaccount_id' not in params or
                                                       params['subaccount_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount_id` when calling `subaccounts_by_subaccount_id_put`")  # noqa: E501
        # verify the required parameter 'subaccount' is set
        if self.api_client.client_side_validation and ('subaccount' not in params or
                                                       params['subaccount'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount` when calling `subaccounts_by_subaccount_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subaccount_id' in params:
            path_params['subaccount_id'] = params['subaccount_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subaccount' in params:
            body_params = params['subaccount']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subaccounts/{subaccount_id}', 'PUT',
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

    def subaccounts_get(self, **kwargs):  # noqa: E501
        """Get all subaccounts  # noqa: E501

        Get all subaccounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def subaccounts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all subaccounts  # noqa: E501

        Get all subaccounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `subaccounts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `subaccounts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/subaccounts', 'GET',
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

    def subaccounts_post(self, subaccount, **kwargs):  # noqa: E501
        """Create new subaccount  # noqa: E501

        Create new subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_post(subaccount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Subaccount subaccount: Subaccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_post_with_http_info(subaccount, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_post_with_http_info(subaccount, **kwargs)  # noqa: E501
            return data

    def subaccounts_post_with_http_info(self, subaccount, **kwargs):  # noqa: E501
        """Create new subaccount  # noqa: E501

        Create new subaccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_post_with_http_info(subaccount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Subaccount subaccount: Subaccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subaccount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subaccount' is set
        if self.api_client.client_side_validation and ('subaccount' not in params or
                                                       params['subaccount'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount` when calling `subaccounts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subaccount' in params:
            body_params = params['subaccount']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subaccounts', 'POST',
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

    def subaccounts_regen_api_key_by_subaccount_id_put(self, subaccount_id, **kwargs):  # noqa: E501
        """Regenerate an API Key  # noqa: E501

        Regenerate an API Key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_regen_api_key_by_subaccount_id_put(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to regenerate API key for (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subaccounts_regen_api_key_by_subaccount_id_put_with_http_info(subaccount_id, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccounts_regen_api_key_by_subaccount_id_put_with_http_info(subaccount_id, **kwargs)  # noqa: E501
            return data

    def subaccounts_regen_api_key_by_subaccount_id_put_with_http_info(self, subaccount_id, **kwargs):  # noqa: E501
        """Regenerate an API Key  # noqa: E501

        Regenerate an API Key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subaccounts_regen_api_key_by_subaccount_id_put_with_http_info(subaccount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subaccount_id: ID of subaccount to regenerate API key for (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subaccount_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccounts_regen_api_key_by_subaccount_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subaccount_id' is set
        if self.api_client.client_side_validation and ('subaccount_id' not in params or
                                                       params['subaccount_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subaccount_id` when calling `subaccounts_regen_api_key_by_subaccount_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subaccount_id' in params:
            path_params['subaccount_id'] = params['subaccount_id']  # noqa: E501

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
            '/subaccounts/{subaccount_id}/regen-api-key', 'PUT',
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
