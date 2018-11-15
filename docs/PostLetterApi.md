# clicksend_client.PostLetterApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_letters_export_get**](PostLetterApi.md#post_letters_export_get) | **GET** /post/letters/export | export post letter history
[**post_letters_history_get**](PostLetterApi.md#post_letters_history_get) | **GET** /post/letters/history | Get all post letter history
[**post_letters_price_post**](PostLetterApi.md#post_letters_price_post) | **POST** /post/letters/price | Calculate post letter price
[**post_letters_send_post**](PostLetterApi.md#post_letters_send_post) | **POST** /post/letters/send | Send post letter


# **post_letters_export_get**
> file post_letters_export_get(filename)

export post letter history

export post letter history

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
api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
filename = 'filename_example' # str | Filename to export to

try:
    # export post letter history
    api_response = api_instance.post_letters_export_get(filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostLetterApi->post_letters_export_get: %s\n" % e)
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

# **post_letters_history_get**
> str post_letters_history_get(page=page, limit=limit)

Get all post letter history

Get all post letter history

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
api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all post letter history
    api_response = api_instance.post_letters_history_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostLetterApi->post_letters_history_get: %s\n" % e)
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

# **post_letters_price_post**
> str post_letters_price_post(post_letter)

Calculate post letter price

Calculate post letter price

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
api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
post_letter = clicksend_client.PostLetter() # PostLetter | PostLetter model

try:
    # Calculate post letter price
    api_response = api_instance.post_letters_price_post(post_letter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostLetterApi->post_letters_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_letter** | [**PostLetter**](PostLetter.md)| PostLetter model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_letters_send_post**
> str post_letters_send_post(post_letter)

Send post letter

Send post letter

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
api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
post_letter = clicksend_client.PostLetter() # PostLetter | PostLetter model

try:
    # Send post letter
    api_response = api_instance.post_letters_send_post(post_letter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostLetterApi->post_letters_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_letter** | [**PostLetter**](PostLetter.md)| PostLetter model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

