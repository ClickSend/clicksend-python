# clicksend_client.FAXDeliveryReceiptRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_delivery_receipt_automation_delete**](FAXDeliveryReceiptRulesApi.md#fax_delivery_receipt_automation_delete) | **DELETE** /automations/fax/receipts/{receipt_rule_id} | Delete fax delivery receipt automation
[**fax_delivery_receipt_automation_get**](FAXDeliveryReceiptRulesApi.md#fax_delivery_receipt_automation_get) | **GET** /automations/fax/receipts/{receipt_rule_id} | Get specific fax delivery receipt automation
[**fax_delivery_receipt_automation_post**](FAXDeliveryReceiptRulesApi.md#fax_delivery_receipt_automation_post) | **POST** /automations/fax/receipts | Create fax delivery receipt automations
[**fax_delivery_receipt_automation_put**](FAXDeliveryReceiptRulesApi.md#fax_delivery_receipt_automation_put) | **PUT** /automations/fax/receipts/{receipt_rule_id} | Update fax delivery receipt automation
[**fax_delivery_receipt_automations_get**](FAXDeliveryReceiptRulesApi.md#fax_delivery_receipt_automations_get) | **GET** /automations/fax/receipts | Get all fax delivery receipt automations


# **fax_delivery_receipt_automation_delete**
> str fax_delivery_receipt_automation_delete(receipt_rule_id)

Delete fax delivery receipt automation

Delete fax delivery receipt automation

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
api_instance = clicksend_client.FAXDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Delete fax delivery receipt automation
    api_response = api_instance.fax_delivery_receipt_automation_delete(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXDeliveryReceiptRulesApi->fax_delivery_receipt_automation_delete: %s\n" % e)
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

# **fax_delivery_receipt_automation_get**
> str fax_delivery_receipt_automation_get(receipt_rule_id)

Get specific fax delivery receipt automation

Get specific fax delivery receipt automation

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
api_instance = clicksend_client.FAXDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Get specific fax delivery receipt automation
    api_response = api_instance.fax_delivery_receipt_automation_get(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXDeliveryReceiptRulesApi->fax_delivery_receipt_automation_get: %s\n" % e)
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

# **fax_delivery_receipt_automation_post**
> str fax_delivery_receipt_automation_post(delivery_receipt_rule)

Create fax delivery receipt automations

Create fax delivery receipt automations

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
api_instance = clicksend_client.FAXDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
delivery_receipt_rule = clicksend_client.DeliveryReceiptRule() # DeliveryReceiptRule | fax delivery receipt rule model

try:
    # Create fax delivery receipt automations
    api_response = api_instance.fax_delivery_receipt_automation_post(delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXDeliveryReceiptRulesApi->fax_delivery_receipt_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| fax delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_delivery_receipt_automation_put**
> str fax_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)

Update fax delivery receipt automation

Update fax delivery receipt automation

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
api_instance = clicksend_client.FAXDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id
delivery_receipt_rule = clicksend_client.DeliveryReceiptRule() # DeliveryReceiptRule | Delivery receipt rule model

try:
    # Update fax delivery receipt automation
    api_response = api_instance.fax_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXDeliveryReceiptRulesApi->fax_delivery_receipt_automation_put: %s\n" % e)
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

# **fax_delivery_receipt_automations_get**
> str fax_delivery_receipt_automations_get(page=page, limit=limit)

Get all fax delivery receipt automations

Get all fax delivery receipt automations

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
api_instance = clicksend_client.FAXDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all fax delivery receipt automations
    api_response = api_instance.fax_delivery_receipt_automations_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FAXDeliveryReceiptRulesApi->fax_delivery_receipt_automations_get: %s\n" % e)
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

