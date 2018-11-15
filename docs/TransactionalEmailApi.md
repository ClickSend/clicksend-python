# clicksend_client.TransactionalEmailApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_history_export_get**](TransactionalEmailApi.md#email_history_export_get) | **GET** /email/history/export | Export all Transactional Email history
[**email_history_get**](TransactionalEmailApi.md#email_history_get) | **GET** /email/history | Get all transactional email history
[**email_price_post**](TransactionalEmailApi.md#email_price_post) | **POST** /email/price | Get transactional email price
[**email_send_post**](TransactionalEmailApi.md#email_send_post) | **POST** /email/send | Send transactional email


# **email_history_export_get**
> str email_history_export_get(filename, date_from=date_from, date_to=date_to)

Export all Transactional Email history

Export all Transactional Email history

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
api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
filename = 'filename_example' # str | Filename to download history as
date_from = 56 # int | Start date (optional)
date_to = 56 # int | End date (optional)

try:
    # Export all Transactional Email history
    api_response = api_instance.email_history_export_get(filename, date_from=date_from, date_to=date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailApi->email_history_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename to download history as | 
 **date_from** | **int**| Start date | [optional] 
 **date_to** | **int**| End date | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_history_get**
> str email_history_get(date_from=date_from, date_to=date_to, page=page, limit=limit)

Get all transactional email history

Get all transactional email history

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
api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
date_from = 56 # int | Start date (optional)
date_to = 56 # int | End date (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all transactional email history
    api_response = api_instance.email_history_get(date_from=date_from, date_to=date_to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailApi->email_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **int**| Start date | [optional] 
 **date_to** | **int**| End date | [optional] 
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

# **email_price_post**
> str email_price_post(email)

Get transactional email price

Get transactional email price

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
api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
email = clicksend_client.Email() # Email | Email model

try:
    # Get transactional email price
    api_response = api_instance.email_price_post(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailApi->email_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email**](Email.md)| Email model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_send_post**
> str email_send_post(email)

Send transactional email

Send transactional email

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
api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
email = clicksend_client.Email() # Email | Email model

try:
    # Send transactional email
    api_response = api_instance.email_send_post(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email**](Email.md)| Email model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

