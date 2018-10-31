# swagger_client.DetectAddressApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detect_address_post**](DetectAddressApi.md#detect_address_post) | **POST** /post/letters/detect-address | Detects address in uploaded file.


# **detect_address_post**
> str detect_address_post(content)

Detects address in uploaded file.

Detects address in uploaded file.

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
api_instance = swagger_client.DetectAddressApi(swagger_client.ApiClient(configuration))
content = 'content_example' # str | Base64-encoded file contents

try:
    # Detects address in uploaded file.
    api_response = api_instance.detect_address_post(content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DetectAddressApi->detect_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| Base64-encoded file contents | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

