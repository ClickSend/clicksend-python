# clicksend_client.InboundSMSRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_inbound_automation_delete**](InboundSMSRulesApi.md#sms_inbound_automation_delete) | **DELETE** /automations/sms/inbound/{inbound_rule_id} | Delete inbound sms automation
[**sms_inbound_automation_get**](InboundSMSRulesApi.md#sms_inbound_automation_get) | **GET** /automations/sms/inbound/{inbound_rule_id} | Get specific inbound sms automation
[**sms_inbound_automation_post**](InboundSMSRulesApi.md#sms_inbound_automation_post) | **POST** /automations/sms/inbound | Create new inbound sms automation
[**sms_inbound_automation_put**](InboundSMSRulesApi.md#sms_inbound_automation_put) | **PUT** /automations/sms/inbound/{inbound_rule_id} | Update inbound sms automation
[**sms_inbound_automations_get**](InboundSMSRulesApi.md#sms_inbound_automations_get) | **GET** /automations/sms/inbound | Get all inbound sms automations


# **sms_inbound_automation_delete**
> str sms_inbound_automation_delete(inbound_rule_id)

Delete inbound sms automation

Delete inbound sms automation

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
api_instance = clicksend_client.InboundSMSRulesApi(clicksend_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id

try:
    # Delete inbound sms automation
    api_response = api_instance.sms_inbound_automation_delete(inbound_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundSMSRulesApi->sms_inbound_automation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_rule_id** | **int**| Inbound rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_inbound_automation_get**
> str sms_inbound_automation_get(inbound_rule_id)

Get specific inbound sms automation

Get specific inbound sms automation

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
api_instance = clicksend_client.InboundSMSRulesApi(clicksend_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id

try:
    # Get specific inbound sms automation
    api_response = api_instance.sms_inbound_automation_get(inbound_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundSMSRulesApi->sms_inbound_automation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_rule_id** | **int**| Inbound rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_inbound_automation_post**
> str sms_inbound_automation_post(inbound_sms_rule)

Create new inbound sms automation

Create new inbound sms automation

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
api_instance = clicksend_client.InboundSMSRulesApi(clicksend_client.ApiClient(configuration))
inbound_sms_rule = clicksend_client.InboundSMSRule() # InboundSMSRule | Inbound sms rule model

try:
    # Create new inbound sms automation
    api_response = api_instance.sms_inbound_automation_post(inbound_sms_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundSMSRulesApi->sms_inbound_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_sms_rule** | [**InboundSMSRule**](InboundSMSRule.md)| Inbound sms rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_inbound_automation_put**
> str sms_inbound_automation_put(inbound_rule_id, inbound_sms_rule)

Update inbound sms automation

Update inbound sms automation

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
api_instance = clicksend_client.InboundSMSRulesApi(clicksend_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id
inbound_sms_rule = clicksend_client.InboundSMSRule() # InboundSMSRule | Inbound sms rule model

try:
    # Update inbound sms automation
    api_response = api_instance.sms_inbound_automation_put(inbound_rule_id, inbound_sms_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundSMSRulesApi->sms_inbound_automation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_rule_id** | **int**| Inbound rule id | 
 **inbound_sms_rule** | [**InboundSMSRule**](InboundSMSRule.md)| Inbound sms rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_inbound_automations_get**
> str sms_inbound_automations_get(q=q, page=page, limit=limit)

Get all inbound sms automations

Get all inbound sms automations

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
api_instance = clicksend_client.InboundSMSRulesApi(clicksend_client.ApiClient(configuration))
q = 'q_example' # str | Your keyword or query. (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all inbound sms automations
    api_response = api_instance.sms_inbound_automations_get(q=q, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundSMSRulesApi->sms_inbound_automations_get: %s\n" % e)
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

