# swagger_client.SearchApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_contacts_lists_get**](SearchApi.md#search_contacts_lists_get) | **GET** /search/contacts-lists | Get list of searched contact list


# **search_contacts_lists_get**
> str search_contacts_lists_get(q, page=page, limit=limit)

Get list of searched contact list

Get list of searched contact list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Your keyword or query.
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of searched contact list
    api_response = api_instance.search_contacts_lists_get(q, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_contacts_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Your keyword or query. | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Number of records per page | [optional] [default to 10]

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

