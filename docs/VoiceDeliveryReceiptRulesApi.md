# swagger_client.VoiceDeliveryReceiptRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voice_delivery_receipt_automation_delete**](VoiceDeliveryReceiptRulesApi.md#voice_delivery_receipt_automation_delete) | **DELETE** /automations/voice/receipts/{receipt_rule_id} | Delete voice delivery receipt automation
[**voice_delivery_receipt_automation_get**](VoiceDeliveryReceiptRulesApi.md#voice_delivery_receipt_automation_get) | **GET** /automations/voice/receipts/{receipt_rule_id} | Get specific voice delivery receipt automation
[**voice_delivery_receipt_automation_post**](VoiceDeliveryReceiptRulesApi.md#voice_delivery_receipt_automation_post) | **POST** /automations/voice/receipts | Create voice delivery receipt automations
[**voice_delivery_receipt_automation_put**](VoiceDeliveryReceiptRulesApi.md#voice_delivery_receipt_automation_put) | **PUT** /automations/voice/receipts/{receipt_rule_id} | Update voice delivery receipt automation
[**voice_delivery_receipt_automations_get**](VoiceDeliveryReceiptRulesApi.md#voice_delivery_receipt_automations_get) | **GET** /automations/voice/receipts | Get all voice delivery receipt automations


# **voice_delivery_receipt_automation_delete**
> str voice_delivery_receipt_automation_delete(receipt_rule_id)

Delete voice delivery receipt automation

Delete voice delivery receipt automation

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
api_instance = swagger_client.VoiceDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Delete voice delivery receipt automation
    api_response = api_instance.voice_delivery_receipt_automation_delete(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceDeliveryReceiptRulesApi->voice_delivery_receipt_automation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_delivery_receipt_automation_get**
> str voice_delivery_receipt_automation_get(receipt_rule_id)

Get specific voice delivery receipt automation

Get specific voice delivery receipt automation

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
api_instance = swagger_client.VoiceDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Get specific voice delivery receipt automation
    api_response = api_instance.voice_delivery_receipt_automation_get(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceDeliveryReceiptRulesApi->voice_delivery_receipt_automation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_delivery_receipt_automation_post**
> str voice_delivery_receipt_automation_post(delivery_receipt_rule)

Create voice delivery receipt automations

Create voice delivery receipt automations

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
api_instance = swagger_client.VoiceDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
delivery_receipt_rule = swagger_client.DeliveryReceiptRule() # DeliveryReceiptRule | voice delivery receipt rule model

try:
    # Create voice delivery receipt automations
    api_response = api_instance.voice_delivery_receipt_automation_post(delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceDeliveryReceiptRulesApi->voice_delivery_receipt_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| voice delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_delivery_receipt_automation_put**
> str voice_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)

Update voice delivery receipt automation

Update voice delivery receipt automation

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
api_instance = swagger_client.VoiceDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id
delivery_receipt_rule = swagger_client.DeliveryReceiptRule() # DeliveryReceiptRule | Delivery receipt rule model

try:
    # Update voice delivery receipt automation
    api_response = api_instance.voice_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceDeliveryReceiptRulesApi->voice_delivery_receipt_automation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| Delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_delivery_receipt_automations_get**
> str voice_delivery_receipt_automations_get(page=page, limit=limit)

Get all voice delivery receipt automations

Get all voice delivery receipt automations

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
api_instance = swagger_client.VoiceDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all voice delivery receipt automations
    api_response = api_instance.voice_delivery_receipt_automations_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceDeliveryReceiptRulesApi->voice_delivery_receipt_automations_get: %s\n" % e)
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

