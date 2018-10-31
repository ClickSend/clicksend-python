# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PostDirectMailApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_direct_mail_campaigns_get(self, **kwargs):  # noqa: E501
        """Get direct mail campaigns  # noqa: E501

        Get direct mail campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_get(async_req=True)
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
            return self.post_direct_mail_campaigns_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_direct_mail_campaigns_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_direct_mail_campaigns_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get direct mail campaigns  # noqa: E501

        Get direct mail campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_get_with_http_info(async_req=True)
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
                    " to method post_direct_mail_campaigns_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `post_direct_mail_campaigns_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `post_direct_mail_campaigns_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/post/direct-mail/campaigns', 'GET',
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

    def post_direct_mail_campaigns_price_post(self, post_direct_mail, **kwargs):  # noqa: E501
        """Calculate direct mail campaign price  # noqa: E501

        Calculate direct mail campaign price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_price_post(post_direct_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectMail post_direct_mail: PostDirectMail model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_direct_mail_campaigns_price_post_with_http_info(post_direct_mail, **kwargs)  # noqa: E501
        else:
            (data) = self.post_direct_mail_campaigns_price_post_with_http_info(post_direct_mail, **kwargs)  # noqa: E501
            return data

    def post_direct_mail_campaigns_price_post_with_http_info(self, post_direct_mail, **kwargs):  # noqa: E501
        """Calculate direct mail campaign price  # noqa: E501

        Calculate direct mail campaign price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_price_post_with_http_info(post_direct_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectMail post_direct_mail: PostDirectMail model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_direct_mail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_direct_mail_campaigns_price_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_direct_mail' is set
        if ('post_direct_mail' not in params or
                params['post_direct_mail'] is None):
            raise ValueError("Missing the required parameter `post_direct_mail` when calling `post_direct_mail_campaigns_price_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_direct_mail' in params:
            body_params = params['post_direct_mail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/post/direct-mail/campaigns/price', 'POST',
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

    def post_direct_mail_campaigns_send_post(self, post_direct_mail, **kwargs):  # noqa: E501
        """Send direct mail campaign  # noqa: E501

        Send direct mail campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_send_post(post_direct_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectMail post_direct_mail: PostDirectMail model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_direct_mail_campaigns_send_post_with_http_info(post_direct_mail, **kwargs)  # noqa: E501
        else:
            (data) = self.post_direct_mail_campaigns_send_post_with_http_info(post_direct_mail, **kwargs)  # noqa: E501
            return data

    def post_direct_mail_campaigns_send_post_with_http_info(self, post_direct_mail, **kwargs):  # noqa: E501
        """Send direct mail campaign  # noqa: E501

        Send direct mail campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_campaigns_send_post_with_http_info(post_direct_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectMail post_direct_mail: PostDirectMail model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_direct_mail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_direct_mail_campaigns_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_direct_mail' is set
        if ('post_direct_mail' not in params or
                params['post_direct_mail'] is None):
            raise ValueError("Missing the required parameter `post_direct_mail` when calling `post_direct_mail_campaigns_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_direct_mail' in params:
            body_params = params['post_direct_mail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/post/direct-mail/campaigns/send', 'POST',
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

    def post_direct_mail_locations_search_by_country_get(self, country, q, **kwargs):  # noqa: E501
        """Search for a location  # noqa: E501

        Search for a location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_locations_search_by_country_get(country, q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Country Code to search (required)
        :param str q: Search term (e.g. post code, city name) (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_direct_mail_locations_search_by_country_get_with_http_info(country, q, **kwargs)  # noqa: E501
        else:
            (data) = self.post_direct_mail_locations_search_by_country_get_with_http_info(country, q, **kwargs)  # noqa: E501
            return data

    def post_direct_mail_locations_search_by_country_get_with_http_info(self, country, q, **kwargs):  # noqa: E501
        """Search for a location  # noqa: E501

        Search for a location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_direct_mail_locations_search_by_country_get_with_http_info(country, q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Country Code to search (required)
        :param str q: Search term (e.g. post code, city name) (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country', 'q', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_direct_mail_locations_search_by_country_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country' is set
        if ('country' not in params or
                params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `post_direct_mail_locations_search_by_country_get`")  # noqa: E501
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `post_direct_mail_locations_search_by_country_get`")  # noqa: E501

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `post_direct_mail_locations_search_by_country_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `post_direct_mail_locations_search_by_country_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'country' in params:
            path_params['country'] = params['country']  # noqa: E501

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
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
            '/post/direct-mail/locations/search/{country}', 'GET',
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
