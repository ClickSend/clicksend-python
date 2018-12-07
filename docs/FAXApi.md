# clicksend_client.FAXApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_receipts_get**](FAXApi.md#fax_receipts_get) | **GET** /fax/receipts | Get all delivery receipts
[**fax_receipts_post**](FAXApi.md#fax_receipts_post) | **POST** /fax/receipts | Add a delivery receipt
[**fax_receipts_read_put**](FAXApi.md#fax_receipts_read_put) | **PUT** /fax/receipts-read | Mark delivery receipts as read


# **fax_receipts_get**
> str fax_receipts_get(page=page, limit=limit)

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
api_instance = clicksend_client.FAXApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all delivery receipts
    api_response = api_instance.fax_receipts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXApi->fax_receipts_get: %s\n" % e)
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

# **fax_receipts_post**
> str fax_receipts_post(url)

Add a delivery receipt

Add a delivery receipt

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
api_instance = clicksend_client.FAXApi(clicksend_client.ApiClient(configuration))
url = clicksend_client.Url() # Url | Url model

try:
    # Add a delivery receipt
    api_response = api_instance.fax_receipts_post(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXApi->fax_receipts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**Url**](Url.md)| Url model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_receipts_read_put**
> str fax_receipts_read_put(date_before=date_before)

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
api_instance = clicksend_client.FAXApi(clicksend_client.ApiClient(configuration))
date_before = clicksend_client.DateBefore() # DateBefore | DateBefore model (optional)

try:
    # Mark delivery receipts as read
    api_response = api_instance.fax_receipts_read_put(date_before=date_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXApi->fax_receipts_read_put: %s\n" % e)
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

