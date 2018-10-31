# swagger_client.SubaccountApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccounts_by_subaccount_id_delete**](SubaccountApi.md#subaccounts_by_subaccount_id_delete) | **DELETE** /subaccounts/{subaccount_id} | Delete a subaccount
[**subaccounts_by_subaccount_id_get**](SubaccountApi.md#subaccounts_by_subaccount_id_get) | **GET** /subaccounts/{subaccount_id} | Get specific subaccount
[**subaccounts_by_subaccount_id_put**](SubaccountApi.md#subaccounts_by_subaccount_id_put) | **PUT** /subaccounts/{subaccount_id} | Update subaccount
[**subaccounts_get**](SubaccountApi.md#subaccounts_get) | **GET** /subaccounts | Get all subaccounts
[**subaccounts_post**](SubaccountApi.md#subaccounts_post) | **POST** /subaccounts | Create new subaccount
[**subaccounts_regen_api_key_by_subaccount_id_put**](SubaccountApi.md#subaccounts_regen_api_key_by_subaccount_id_put) | **PUT** /subaccounts/{subaccount_id}/regen-api-key | Regenerate an API Key


# **subaccounts_by_subaccount_id_delete**
> str subaccounts_by_subaccount_id_delete(subaccount_id)

Delete a subaccount

Delete a subaccount

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
subaccount_id = 56 # int | ID of subaccount to delete

try:
    # Delete a subaccount
    api_response = api_instance.subaccounts_by_subaccount_id_delete(subaccount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_by_subaccount_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **int**| ID of subaccount to delete | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccounts_by_subaccount_id_get**
> str subaccounts_by_subaccount_id_get(subaccount_id)

Get specific subaccount

Get specific subaccount

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
subaccount_id = 56 # int | ID of subaccount to get

try:
    # Get specific subaccount
    api_response = api_instance.subaccounts_by_subaccount_id_get(subaccount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_by_subaccount_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **int**| ID of subaccount to get | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccounts_by_subaccount_id_put**
> str subaccounts_by_subaccount_id_put(subaccount_id, subaccount)

Update subaccount

Update subaccount

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
subaccount_id = 56 # int | ID of subaccount to update
subaccount = swagger_client.Subaccount() # Subaccount | Subaccount model

try:
    # Update subaccount
    api_response = api_instance.subaccounts_by_subaccount_id_put(subaccount_id, subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_by_subaccount_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **int**| ID of subaccount to update | 
 **subaccount** | [**Subaccount**](Subaccount.md)| Subaccount model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccounts_get**
> str subaccounts_get(page=page, limit=limit)

Get all subaccounts

Get all subaccounts

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all subaccounts
    api_response = api_instance.subaccounts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_get: %s\n" % e)
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

# **subaccounts_post**
> str subaccounts_post(subaccount)

Create new subaccount

Create new subaccount

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
subaccount = swagger_client.Subaccount() # Subaccount | Subaccount model

try:
    # Create new subaccount
    api_response = api_instance.subaccounts_post(subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount** | [**Subaccount**](Subaccount.md)| Subaccount model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subaccounts_regen_api_key_by_subaccount_id_put**
> str subaccounts_regen_api_key_by_subaccount_id_put(subaccount_id)

Regenerate an API Key

Regenerate an API Key

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
api_instance = swagger_client.SubaccountApi(swagger_client.ApiClient(configuration))
subaccount_id = 56 # int | ID of subaccount to regenerate API key for

try:
    # Regenerate an API Key
    api_response = api_instance.subaccounts_regen_api_key_by_subaccount_id_put(subaccount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountApi->subaccounts_regen_api_key_by_subaccount_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **int**| ID of subaccount to regenerate API key for | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

