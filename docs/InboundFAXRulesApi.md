# swagger_client.InboundFAXRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_inbound_automation_delete**](InboundFAXRulesApi.md#fax_inbound_automation_delete) | **DELETE** /automations/fax/inbound/{inbound_rule_id} | Delete inbound fax automation
[**fax_inbound_automation_get**](InboundFAXRulesApi.md#fax_inbound_automation_get) | **GET** /automations/fax/inbound/{inbound_rule_id} | Get specific inbound fax automation
[**fax_inbound_automation_post**](InboundFAXRulesApi.md#fax_inbound_automation_post) | **POST** /automations/fax/inbound | Create new inbound fax automation
[**fax_inbound_automation_put**](InboundFAXRulesApi.md#fax_inbound_automation_put) | **PUT** /automations/fax/inbound/{inbound_rule_id} | Update inbound fax automation
[**fax_inbound_automations_get**](InboundFAXRulesApi.md#fax_inbound_automations_get) | **GET** /automations/fax/inbound | Get all inbound fax automations


# **fax_inbound_automation_delete**
> str fax_inbound_automation_delete(inbound_rule_id)

Delete inbound fax automation

Delete inbound fax automation

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
api_instance = swagger_client.InboundFAXRulesApi(swagger_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id

try:
    # Delete inbound fax automation
    api_response = api_instance.fax_inbound_automation_delete(inbound_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundFAXRulesApi->fax_inbound_automation_delete: %s\n" % e)
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

# **fax_inbound_automation_get**
> str fax_inbound_automation_get(inbound_rule_id)

Get specific inbound fax automation

Get specific inbound fax automation

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
api_instance = swagger_client.InboundFAXRulesApi(swagger_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id

try:
    # Get specific inbound fax automation
    api_response = api_instance.fax_inbound_automation_get(inbound_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundFAXRulesApi->fax_inbound_automation_get: %s\n" % e)
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

# **fax_inbound_automation_post**
> str fax_inbound_automation_post(inbound_fax_rule)

Create new inbound fax automation

Create new inbound fax automation

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
api_instance = swagger_client.InboundFAXRulesApi(swagger_client.ApiClient(configuration))
inbound_fax_rule = swagger_client.InboundFAXRule() # InboundFAXRule | Inbound fax rule model

try:
    # Create new inbound fax automation
    api_response = api_instance.fax_inbound_automation_post(inbound_fax_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundFAXRulesApi->fax_inbound_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_fax_rule** | [**InboundFAXRule**](InboundFAXRule.md)| Inbound fax rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_inbound_automation_put**
> str fax_inbound_automation_put(inbound_rule_id, inbound_fax_rule)

Update inbound fax automation

Update inbound fax automation

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
api_instance = swagger_client.InboundFAXRulesApi(swagger_client.ApiClient(configuration))
inbound_rule_id = 56 # int | Inbound rule id
inbound_fax_rule = swagger_client.InboundFAXRule() # InboundFAXRule | Inbound fax rule model

try:
    # Update inbound fax automation
    api_response = api_instance.fax_inbound_automation_put(inbound_rule_id, inbound_fax_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundFAXRulesApi->fax_inbound_automation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_rule_id** | **int**| Inbound rule id | 
 **inbound_fax_rule** | [**InboundFAXRule**](InboundFAXRule.md)| Inbound fax rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_inbound_automations_get**
> str fax_inbound_automations_get(page=page, limit=limit)

Get all inbound fax automations

Get all inbound fax automations

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
api_instance = swagger_client.InboundFAXRulesApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all inbound fax automations
    api_response = api_instance.fax_inbound_automations_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundFAXRulesApi->fax_inbound_automations_get: %s\n" % e)
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

