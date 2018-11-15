# clicksend_client.VoiceApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voice_cancel_all_put**](VoiceApi.md#voice_cancel_all_put) | **PUT** /voice/cancel-all | Update all voice messages as cancelled
[**voice_cancel_by_message_id_put**](VoiceApi.md#voice_cancel_by_message_id_put) | **PUT** /voice/{message_id}/cancel | Update voice message status as cancelled
[**voice_history_export_get**](VoiceApi.md#voice_history_export_get) | **GET** /voice/history/export | Export voice history
[**voice_history_get**](VoiceApi.md#voice_history_get) | **GET** /voice/history | Get all voice history
[**voice_lang_get**](VoiceApi.md#voice_lang_get) | **GET** /voice/lang | Get all voice languages
[**voice_price_post**](VoiceApi.md#voice_price_post) | **POST** /voice/price | Calculate voice price
[**voice_receipts_get**](VoiceApi.md#voice_receipts_get) | **GET** /voice/receipts | Get all voice receipts
[**voice_send_post**](VoiceApi.md#voice_send_post) | **POST** /voice/send | Send voice message(s)


# **voice_cancel_all_put**
> str voice_cancel_all_put()

Update all voice messages as cancelled

Update all voice messages as cancelled

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))

try:
    # Update all voice messages as cancelled
    api_response = api_instance.voice_cancel_all_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_cancel_all_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_cancel_by_message_id_put**
> str voice_cancel_by_message_id_put(message_id)

Update voice message status as cancelled

Update voice message status as cancelled

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Your voice message id

try:
    # Update voice message status as cancelled
    api_response = api_instance.voice_cancel_by_message_id_put(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_cancel_by_message_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Your voice message id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_history_export_get**
> file voice_history_export_get(filename)

Export voice history

Export voice history

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
filename = 'filename_example' # str | Filename to export to

try:
    # Export voice history
    api_response = api_instance.voice_history_export_get(filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_history_export_get: %s\n" % e)
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

# **voice_history_get**
> str voice_history_get(date_from=date_from, date_to=date_to, page=page, limit=limit)

Get all voice history

Get all voice history

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
date_from = 56 # int | Timestamp (from) used to show records by date. (optional)
date_to = 56 # int | Timestamp (to) used to show records by date (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all voice history
    api_response = api_instance.voice_history_get(date_from=date_from, date_to=date_to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **int**| Timestamp (from) used to show records by date. | [optional] 
 **date_to** | **int**| Timestamp (to) used to show records by date | [optional] 
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

# **voice_lang_get**
> str voice_lang_get()

Get all voice languages

Get all voice languages

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))

try:
    # Get all voice languages
    api_response = api_instance.voice_lang_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_lang_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_price_post**
> str voice_price_post(voice_messages)

Calculate voice price

Calculate voice price

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
voice_messages = clicksend_client.VoiceMessageCollection() # VoiceMessageCollection | VoiceMessageCollection model

try:
    # Calculate voice price
    api_response = api_instance.voice_price_post(voice_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_messages** | [**VoiceMessageCollection**](VoiceMessageCollection.md)| VoiceMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_receipts_get**
> str voice_receipts_get(page=page, limit=limit)

Get all voice receipts

Get all voice receipts

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all voice receipts
    api_response = api_instance.voice_receipts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_receipts_get: %s\n" % e)
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

# **voice_send_post**
> str voice_send_post(voice_messages)

Send voice message(s)

Send a voice call

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
api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
voice_messages = clicksend_client.VoiceMessageCollection() # VoiceMessageCollection | VoiceMessageCollection model

try:
    # Send voice message(s)
    api_response = api_instance.voice_send_post(voice_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_messages** | [**VoiceMessageCollection**](VoiceMessageCollection.md)| VoiceMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

