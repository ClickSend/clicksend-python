# clicksend_client.SMSApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_cancel_all_put**](SMSApi.md#sms_cancel_all_put) | **PUT** /sms/cancel-all | Update all scheduled message as cancelled
[**sms_cancel_by_message_id_put**](SMSApi.md#sms_cancel_by_message_id_put) | **PUT** /sms/{message_id}/cancel | Update scheduled message as cancelled
[**sms_history_export_get**](SMSApi.md#sms_history_export_get) | **GET** /sms/history/export | Export all sms history
[**sms_history_get**](SMSApi.md#sms_history_get) | **GET** /sms/history | Get all sms history
[**sms_inbound_get**](SMSApi.md#sms_inbound_get) | **GET** /sms/inbound | Get all inbound sms
[**sms_inbound_post**](SMSApi.md#sms_inbound_post) | **POST** /sms/inbound | Create inbound sms
[**sms_inbound_read_by_message_id_put**](SMSApi.md#sms_inbound_read_by_message_id_put) | **PUT** /sms/inbound-read/{message_id} | Mark inbound SMS as read
[**sms_inbound_read_put**](SMSApi.md#sms_inbound_read_put) | **PUT** /sms/inbound-read | Mark inbound SMS as read
[**sms_price_post**](SMSApi.md#sms_price_post) | **POST** /sms/price | Calculate sms price
[**sms_receipt_read_by_message_id_put**](SMSApi.md#sms_receipt_read_by_message_id_put) | **PUT** /sms/receipts-read/{message_id} | Mark specific delivery receipt as read
[**sms_receipts_by_message_id_get**](SMSApi.md#sms_receipts_by_message_id_get) | **GET** /sms/receipts/{message_id} | Get a Specific Delivery Receipt
[**sms_receipts_get**](SMSApi.md#sms_receipts_get) | **GET** /sms/receipts | Get all delivery receipts
[**sms_receipts_post**](SMSApi.md#sms_receipts_post) | **POST** /sms/receipts | Add a delivery receipt
[**sms_receipts_read_put**](SMSApi.md#sms_receipts_read_put) | **PUT** /sms/receipts-read | Mark delivery receipts as read
[**sms_send_post**](SMSApi.md#sms_send_post) | **POST** /sms/send | Send sms message(s)
[**sms_templates_by_template_id_delete**](SMSApi.md#sms_templates_by_template_id_delete) | **DELETE** /sms/templates/{template_id} | Delete sms template
[**sms_templates_by_template_id_put**](SMSApi.md#sms_templates_by_template_id_put) | **PUT** /sms/templates/{template_id} | Update sms template
[**sms_templates_get**](SMSApi.md#sms_templates_get) | **GET** /sms/templates | Get lists of all sms templates
[**sms_templates_post**](SMSApi.md#sms_templates_post) | **POST** /sms/templates | Create sms template


# **sms_cancel_all_put**
> str sms_cancel_all_put()

Update all scheduled message as cancelled

Update all scheduled message as cancelled

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

try:
    # Update all scheduled message as cancelled
    api_response = api_instance.sms_cancel_all_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_cancel_all_put: %s\n" % e)
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

# **sms_cancel_by_message_id_put**
> str sms_cancel_by_message_id_put(message_id)

Update scheduled message as cancelled

Update scheduled message as cancelled

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | The message ID you want to cancel

try:
    # Update scheduled message as cancelled
    api_response = api_instance.sms_cancel_by_message_id_put(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_cancel_by_message_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The message ID you want to cancel | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_history_export_get**
> str sms_history_export_get(filename)

Export all sms history

Export all sms history

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
filename = 'filename_example' # str | Filename to download history as

try:
    # Export all sms history
    api_response = api_instance.sms_history_export_get(filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_history_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename to download history as | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_history_get**
> str sms_history_get(q=q, date_from=date_from, date_to=date_to, page=page, limit=limit)

Get all sms history

Get all sms history

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
q = 'q_example' # str | Custom query Example: from:{number},status_code:201. (optional)
date_from = 56 # int | Start date (optional)
date_to = 56 # int | End date (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all sms history
    api_response = api_instance.sms_history_get(q=q, date_from=date_from, date_to=date_to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Custom query Example: from:{number},status_code:201. | [optional] 
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

# **sms_inbound_get**
> str sms_inbound_get(q=q, page=page, limit=limit)

Get all inbound sms

Get all inbound sms

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
q = 'q_example' # str | Your keyword or query. (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all inbound sms
    api_response = api_instance.sms_inbound_get(q=q, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_inbound_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Your keyword or query. | [optional] 
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

# **sms_inbound_post**
> str sms_inbound_post(url)

Create inbound sms

Create inbound sms

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
url = clicksend_client.Url() # Url | Url model

try:
    # Create inbound sms
    api_response = api_instance.sms_inbound_post(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_inbound_post: %s\n" % e)
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

# **sms_inbound_read_by_message_id_put**
> str sms_inbound_read_by_message_id_put(message_id)

Mark inbound SMS as read

Mark specific inbound SMS as read

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Message ID

try:
    # Mark inbound SMS as read
    api_response = api_instance.sms_inbound_read_by_message_id_put(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_inbound_read_by_message_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_inbound_read_put**
> str sms_inbound_read_put(date_before=date_before)

Mark inbound SMS as read

Mark all inbound SMS as read optionally before a certain date

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
date_before = clicksend_client.DateBefore() # DateBefore | DateBefore model (optional)

try:
    # Mark inbound SMS as read
    api_response = api_instance.sms_inbound_read_put(date_before=date_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_inbound_read_put: %s\n" % e)
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

# **sms_price_post**
> str sms_price_post(sms_messages)

Calculate sms price

Calculate sms price

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
sms_messages = clicksend_client.SmsMessageCollection() # SmsMessageCollection | SmsMessageCollection model

try:
    # Calculate sms price
    api_response = api_instance.sms_price_post(sms_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_messages** | [**SmsMessageCollection**](SmsMessageCollection.md)| SmsMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_receipt_read_by_message_id_put**
> str sms_receipt_read_by_message_id_put(message_id)

Mark specific delivery receipt as read

Mark specific delivery receipt as read

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | The message ID you want to mark as read

try:
    # Mark specific delivery receipt as read
    api_response = api_instance.sms_receipt_read_by_message_id_put(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_receipt_read_by_message_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The message ID you want to mark as read | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_receipts_by_message_id_get**
> str sms_receipts_by_message_id_get(message_id)

Get a Specific Delivery Receipt

Get a Specific Delivery Receipt

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Message ID

try:
    # Get a Specific Delivery Receipt
    api_response = api_instance.sms_receipts_by_message_id_get(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_receipts_by_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_receipts_get**
> str sms_receipts_get(page=page, limit=limit)

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all delivery receipts
    api_response = api_instance.sms_receipts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_receipts_get: %s\n" % e)
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

# **sms_receipts_post**
> str sms_receipts_post(url)

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
url = clicksend_client.Url() # Url | Url model

try:
    # Add a delivery receipt
    api_response = api_instance.sms_receipts_post(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_receipts_post: %s\n" % e)
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

# **sms_receipts_read_put**
> str sms_receipts_read_put(date_before=date_before)

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
date_before = clicksend_client.DateBefore() # DateBefore | DateBefore model (optional)

try:
    # Mark delivery receipts as read
    api_response = api_instance.sms_receipts_read_put(date_before=date_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_receipts_read_put: %s\n" % e)
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

# **sms_send_post**
> str sms_send_post(sms_messages)

Send sms message(s)

 # Send one or more SMS messages  You can post up to 1000 messages with each API call. You can send to a mix of contacts and contact lists, as long as the total number of recipients is up to 1000.  The response contains status and details for each recipient.  *Refer to [Application Status Codes](https://dashboard.clicksend.com/#/signup/step1/) for the possible response message status strings.* 

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
sms_messages = clicksend_client.SmsMessageCollection() # SmsMessageCollection | SmsMessageCollection model

try:
    # Send sms message(s)
    api_response = api_instance.sms_send_post(sms_messages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_messages** | [**SmsMessageCollection**](SmsMessageCollection.md)| SmsMessageCollection model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_templates_by_template_id_delete**
> str sms_templates_by_template_id_delete(template_id)

Delete sms template

Delete sms template

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Template id

try:
    # Delete sms template
    api_response = api_instance.sms_templates_by_template_id_delete(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_templates_by_template_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_templates_by_template_id_put**
> str sms_templates_by_template_id_put(template_id, sms_template)

Update sms template

Update sms template

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Template id
sms_template = clicksend_client.SmsTemplate() # SmsTemplate | Template item

try:
    # Update sms template
    api_response = api_instance.sms_templates_by_template_id_put(template_id, sms_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_templates_by_template_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template id | 
 **sms_template** | [**SmsTemplate**](SmsTemplate.md)| Template item | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_templates_get**
> str sms_templates_get(page=page, limit=limit)

Get lists of all sms templates

Get lists of all sms templates

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get lists of all sms templates
    api_response = api_instance.sms_templates_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_templates_get: %s\n" % e)
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

# **sms_templates_post**
> str sms_templates_post(sms_template)

Create sms template

Create sms template

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
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
sms_template = clicksend_client.SmsTemplate() # SmsTemplate | SmsTemplate model

try:
    # Create sms template
    api_response = api_instance.sms_templates_post(sms_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->sms_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_template** | [**SmsTemplate**](SmsTemplate.md)| SmsTemplate model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

