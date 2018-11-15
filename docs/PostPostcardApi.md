# clicksend_client.PostPostcardApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_postcards_history_export_get**](PostPostcardApi.md#post_postcards_history_export_get) | **GET** /post/postcards/history/export | Export postcard history to a CSV file
[**post_postcards_history_get**](PostPostcardApi.md#post_postcards_history_get) | **GET** /post/postcards/history | Retrieve the history of postcards sent or scheduled
[**post_postcards_price_post**](PostPostcardApi.md#post_postcards_price_post) | **POST** /post/postcards/price | Calculate price for sending one or more postcards
[**post_postcards_send_post**](PostPostcardApi.md#post_postcards_send_post) | **POST** /post/postcards/send | Send one or more postcards


# **post_postcards_history_export_get**
> file post_postcards_history_export_get(filename)

Export postcard history to a CSV file

Export postcard history to a CSV file

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
api_instance = clicksend_client.PostPostcardApi(clicksend_client.ApiClient(configuration))
filename = 'filename_example' # str | Filename to export to

try:
    # Export postcard history to a CSV file
    api_response = api_instance.post_postcards_history_export_get(filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostPostcardApi->post_postcards_history_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename to export to | 

### Return type

[**file**](file.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_postcards_history_get**
> str post_postcards_history_get(page=page, limit=limit)

Retrieve the history of postcards sent or scheduled

Retrieve the history of postcards sent or scheduled

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
api_instance = clicksend_client.PostPostcardApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Retrieve the history of postcards sent or scheduled
    api_response = api_instance.post_postcards_history_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostPostcardApi->post_postcards_history_get: %s\n" % e)
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

# **post_postcards_price_post**
> str post_postcards_price_post(post_postcards)

Calculate price for sending one or more postcards

Calculate price for sending one or more postcards

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
api_instance = clicksend_client.PostPostcardApi(clicksend_client.ApiClient(configuration))
post_postcards = clicksend_client.PostPostcard() # PostPostcard | PostPostcard model

try:
    # Calculate price for sending one or more postcards
    api_response = api_instance.post_postcards_price_post(post_postcards)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostPostcardApi->post_postcards_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_postcards** | [**PostPostcard**](PostPostcard.md)| PostPostcard model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_postcards_send_post**
> str post_postcards_send_post(post_postcards)

Send one or more postcards

Send one or more postcards

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
api_instance = clicksend_client.PostPostcardApi(clicksend_client.ApiClient(configuration))
post_postcards = clicksend_client.PostPostcard() # PostPostcard | PostPostcard model

try:
    # Send one or more postcards
    api_response = api_instance.post_postcards_send_post(post_postcards)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostPostcardApi->post_postcards_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_postcards** | [**PostPostcard**](PostPostcard.md)| PostPostcard model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

