# clicksend_client.UploadApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploads_post**](UploadApi.md#uploads_post) | **POST** /uploads | Upload File


# **uploads_post**
> str uploads_post(convert, upload_file=upload_file)

Upload File

Upload File

### Example
```python
from __future__ import print_function
import time
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = clicksend_client.UploadApi(clicksend_client.ApiClient(configuration))
convert = 'convert_example' # str | 
upload_file = clicksend_client.UploadFile() # UploadFile |  (optional)

try:
    # Upload File
    api_response = api_instance.uploads_post(convert, upload_file=upload_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->uploads_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert** | **str**|  | 
 **upload_file** | [**UploadFile**](UploadFile.md)|  | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

