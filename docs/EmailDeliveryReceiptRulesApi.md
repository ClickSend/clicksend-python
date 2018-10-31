# swagger_client.EmailDeliveryReceiptRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_delivery_receipt_automation_delete**](EmailDeliveryReceiptRulesApi.md#email_delivery_receipt_automation_delete) | **DELETE** /automations/email/receipts/{receipt_rule_id} | Delete email delivery receipt automation
[**email_delivery_receipt_automation_get**](EmailDeliveryReceiptRulesApi.md#email_delivery_receipt_automation_get) | **GET** /automations/email/receipts/{receipt_rule_id} | Get specific email delivery receipt automation
[**email_delivery_receipt_automation_post**](EmailDeliveryReceiptRulesApi.md#email_delivery_receipt_automation_post) | **POST** /automations/email/receipts | Create email delivery receipt automations
[**email_delivery_receipt_automation_put**](EmailDeliveryReceiptRulesApi.md#email_delivery_receipt_automation_put) | **PUT** /automations/email/receipts/{receipt_rule_id} | Update email delivery receipt automation
[**email_delivery_receipt_automations_get**](EmailDeliveryReceiptRulesApi.md#email_delivery_receipt_automations_get) | **GET** /automations/email/receipts | Get all email delivery receipt automations


# **email_delivery_receipt_automation_delete**
> str email_delivery_receipt_automation_delete(receipt_rule_id)

Delete email delivery receipt automation

Delete email delivery receipt automation

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
api_instance = swagger_client.EmailDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Delete email delivery receipt automation
    api_response = api_instance.email_delivery_receipt_automation_delete(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailDeliveryReceiptRulesApi->email_delivery_receipt_automation_delete: %s\n" % e)
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

# **email_delivery_receipt_automation_get**
> str email_delivery_receipt_automation_get(receipt_rule_id)

Get specific email delivery receipt automation

Get specific email delivery receipt automation

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
api_instance = swagger_client.EmailDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Get specific email delivery receipt automation
    api_response = api_instance.email_delivery_receipt_automation_get(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailDeliveryReceiptRulesApi->email_delivery_receipt_automation_get: %s\n" % e)
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

# **email_delivery_receipt_automation_post**
> str email_delivery_receipt_automation_post(delivery_receipt_rule)

Create email delivery receipt automations

Create email delivery receipt automations

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
api_instance = swagger_client.EmailDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
delivery_receipt_rule = swagger_client.DeliveryReceiptRule() # DeliveryReceiptRule | Email delivery receipt rule model

try:
    # Create email delivery receipt automations
    api_response = api_instance.email_delivery_receipt_automation_post(delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailDeliveryReceiptRulesApi->email_delivery_receipt_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| Email delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_delivery_receipt_automation_put**
> str email_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)

Update email delivery receipt automation

Update email delivery receipt automation

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
api_instance = swagger_client.EmailDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id
delivery_receipt_rule = swagger_client.DeliveryReceiptRule() # DeliveryReceiptRule | Delivery receipt rule model

try:
    # Update email delivery receipt automation
    api_response = api_instance.email_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailDeliveryReceiptRulesApi->email_delivery_receipt_automation_put: %s\n" % e)
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

# **email_delivery_receipt_automations_get**
> str email_delivery_receipt_automations_get(page=page, limit=limit)

Get all email delivery receipt automations

Get all email delivery receipt automations

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
api_instance = swagger_client.EmailDeliveryReceiptRulesApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all email delivery receipt automations
    api_response = api_instance.email_delivery_receipt_automations_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailDeliveryReceiptRulesApi->email_delivery_receipt_automations_get: %s\n" % e)
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

