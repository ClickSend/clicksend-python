# clicksend_client.FaxApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_history_get**](FaxApi.md#fax_history_get) | **GET** /fax/history | Get a list of Fax History.
[**fax_price_post**](FaxApi.md#fax_price_post) | **POST** /fax/price | Calculate Total Price for Fax Messages sent
[**fax_receipts_by_message_id_get**](FaxApi.md#fax_receipts_by_message_id_get) | **GET** /fax/receipts/{message_id} | Get a single fax receipt based on message id.
[**fax_receipts_get**](FaxApi.md#fax_receipts_get) | **GET** /fax/receipts | Get List of Fax Receipts
[**fax_send_post**](FaxApi.md#fax_send_post) | **POST** /fax/send | Send a fax using supplied supported file-types.


# **fax_history_get**
> str fax_history_get(date_from=date_from, date_to=date_to, q=q, order=order, page=page, limit=limit)

Get a list of Fax History.

Get a list of Fax History.

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
api_instance = clicksend_client.FaxApi(clicksend_client.ApiClient(configuration))
date_from = 56 # int | Customize result by setting from date (timestsamp) Example: 1457572619. (optional)
date_to = 56 # int | Customize result by setting to date (timestamp) Example: 1457573000. (optional)
q = 'q_example' # str | Custom query Example: status:Sent,status_code:201. (optional)
order = 'order_example' # str | Order result by Example: date_added:desc,list_id:desc. (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get a list of Fax History.
    api_response = api_instance.fax_history_get(date_from=date_from, date_to=date_to, q=q, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->fax_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **int**| Customize result by setting from date (timestsamp) Example: 1457572619. | [optional] 
 **date_to** | **int**| Customize result by setting to date (timestamp) Example: 1457573000. | [optional] 
 **q** | **str**| Custom query Example: status:Sent,status_code:201. | [optional] 
 **order** | **str**| Order result by Example: date_added:desc,list_id:desc. | [optional] 
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

# **fax_price_post**
> str fax_price_post(fax_message)

Calculate Total Price for Fax Messages sent

Calculate Total Price for Fax Messages sent

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
api_instance = clicksend_client.FaxApi(clicksend_client.ApiClient(configuration))
fax_message = clicksend_client.FaxMessageCollection() # FaxMessageCollection | FaxMessageCollection model

try:
    # Calculate Total Price for Fax Messages sent
    api_response = api_instance.fax_price_post(fax_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->fax_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_message** | [**FaxMessageCollection**](FaxMessageCollection.md)| FaxMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_receipts_by_message_id_get**
> str fax_receipts_by_message_id_get(message_id)

Get a single fax receipt based on message id.

Get a single fax receipt based on message id.

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
api_instance = clicksend_client.FaxApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | ID of the message receipt to retrieve

try:
    # Get a single fax receipt based on message id.
    api_response = api_instance.fax_receipts_by_message_id_get(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->fax_receipts_by_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| ID of the message receipt to retrieve | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_receipts_get**
> str fax_receipts_get(q, page=page, limit=limit)

Get List of Fax Receipts

Get List of Fax Receipts

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
api_instance = clicksend_client.FaxApi(clicksend_client.ApiClient(configuration))
q = 'q_example' # str | Your keyword or query.
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get List of Fax Receipts
    api_response = api_instance.fax_receipts_get(q, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->fax_receipts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Your keyword or query. | 
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

# **fax_send_post**
> str fax_send_post(fax_message)

Send a fax using supplied supported file-types.

Send a fax using supplied supported file-types.

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
api_instance = clicksend_client.FaxApi(clicksend_client.ApiClient(configuration))
fax_message = clicksend_client.FaxMessageCollection() # FaxMessageCollection | FaxMessageCollection model

try:
    # Send a fax using supplied supported file-types.
    api_response = api_instance.fax_send_post(fax_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxApi->fax_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_message** | [**FaxMessageCollection**](FaxMessageCollection.md)| FaxMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

