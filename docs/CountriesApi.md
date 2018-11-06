# clicksend_client.CountriesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_get**](CountriesApi.md#countries_get) | **GET** /countries | Get all country codes


# **countries_get**
> str countries_get()

Get all country codes

Get all countries

### Example
```python
from __future__ import print_function
import time
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clicksend_client.CountriesApi()

try:
    # Get all country codes
    api_response = api_instance.countries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->countries_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

