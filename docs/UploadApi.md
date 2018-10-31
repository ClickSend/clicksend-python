# swagger_client.UploadApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploads_post**](UploadApi.md#uploads_post) | **POST** /uploads | Upload File


# **uploads_post**
> str uploads_post(content, convert)

Upload File

Upload File

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
api_instance = swagger_client.UploadApi(swagger_client.ApiClient(configuration))
content = 'content_example' # str | Base64-encoded file contents
convert = 'convert_example' # str | 

try:
    # Upload File
    api_response = api_instance.uploads_post(content, convert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->uploads_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| Base64-encoded file contents | 
 **convert** | **str**|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

