# swagger_client.MMSApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mms_price_post**](MMSApi.md#mms_price_post) | **POST** /mms/price | Get Price for MMS sent
[**mms_send_post**](MMSApi.md#mms_send_post) | **POST** /mms/send | Send MMS


# **mms_price_post**
> str mms_price_post(mms_messages)

Get Price for MMS sent

Get Price for MMS sent

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
api_instance = swagger_client.MMSApi(swagger_client.ApiClient(configuration))
mms_messages = swagger_client.MmsMessageCollection() # MmsMessageCollection | MmsMessageCollection model

try:
    # Get Price for MMS sent
    api_response = api_instance.mms_price_post(mms_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMSApi->mms_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mms_messages** | [**MmsMessageCollection**](MmsMessageCollection.md)| MmsMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mms_send_post**
> str mms_send_post(mms_messages)

Send MMS

Send MMS

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
api_instance = swagger_client.MMSApi(swagger_client.ApiClient(configuration))
mms_messages = swagger_client.MmsMessageCollection() # MmsMessageCollection | MmsMessageCollection model

try:
    # Send MMS
    api_response = api_instance.mms_send_post(mms_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMSApi->mms_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mms_messages** | [**MmsMessageCollection**](MmsMessageCollection.md)| MmsMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

