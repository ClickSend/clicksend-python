# clicksend_client.MMSApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mms_price_post**](MMSApi.md#mms_price_post) | **POST** /mms/price | Get Price for MMS sent
[**mms_receipts_get**](MMSApi.md#mms_receipts_get) | **GET** /mms/receipts | Get all delivery receipts
[**mms_receipts_read_put**](MMSApi.md#mms_receipts_read_put) | **PUT** /mms/receipts-read | Mark delivery receipts as read
[**mms_send_post**](MMSApi.md#mms_send_post) | **POST** /mms/send | Send MMS


# **mms_price_post**
> str mms_price_post(mms_messages)

Get Price for MMS sent

Get Price for MMS sent

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
api_instance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))
mms_messages = clicksend_client.MmsMessageCollection() # MmsMessageCollection | MmsMessageCollection model

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

# **mms_receipts_get**
> str mms_receipts_get(page=page, limit=limit)

Get all delivery receipts

Get all delivery receipts

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
api_instance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all delivery receipts
    api_response = api_instance.mms_receipts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMSApi->mms_receipts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **mms_receipts_read_put**
> str mms_receipts_read_put(date_before=date_before)

Mark delivery receipts as read

Mark delivery receipts as read

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
api_instance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))
date_before = clicksend_client.DateBefore() # DateBefore | DateBefore model (optional)

try:
    # Mark delivery receipts as read
    api_response = api_instance.mms_receipts_read_put(date_before=date_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MMSApi->mms_receipts_read_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_before** | [**DateBefore**](DateBefore.md)| DateBefore model | [optional] 

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
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))
mms_messages = clicksend_client.MmsMessageCollection() # MmsMessageCollection | MmsMessageCollection model

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

