# clicksend_client.PostReturnAddressApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_return_addresses_by_return_address_id_delete**](PostReturnAddressApi.md#post_return_addresses_by_return_address_id_delete) | **DELETE** /post/return-addresses/{return_address_id} | Delete specific post return address
[**post_return_addresses_by_return_address_id_get**](PostReturnAddressApi.md#post_return_addresses_by_return_address_id_get) | **GET** /post/return-addresses/{return_address_id} | Get specific post return address
[**post_return_addresses_by_return_address_id_put**](PostReturnAddressApi.md#post_return_addresses_by_return_address_id_put) | **PUT** /post/return-addresses/{return_address_id} | Update post return address
[**post_return_addresses_get**](PostReturnAddressApi.md#post_return_addresses_get) | **GET** /post/return-addresses | Get list of post return addresses
[**post_return_addresses_post**](PostReturnAddressApi.md#post_return_addresses_post) | **POST** /post/return-addresses | Create post return address


# **post_return_addresses_by_return_address_id_delete**
> str post_return_addresses_by_return_address_id_delete(return_address_id)

Delete specific post return address

Delete specific post return address

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
api_instance = clicksend_client.PostReturnAddressApi(clicksend_client.ApiClient(configuration))
return_address_id = 56 # int | Return address ID

try:
    # Delete specific post return address
    api_response = api_instance.post_return_addresses_by_return_address_id_delete(return_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReturnAddressApi->post_return_addresses_by_return_address_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_address_id** | **int**| Return address ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_return_addresses_by_return_address_id_get**
> str post_return_addresses_by_return_address_id_get(return_address_id)

Get specific post return address

Get specific post return address

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
api_instance = clicksend_client.PostReturnAddressApi(clicksend_client.ApiClient(configuration))
return_address_id = 56 # int | Return address ID

try:
    # Get specific post return address
    api_response = api_instance.post_return_addresses_by_return_address_id_get(return_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReturnAddressApi->post_return_addresses_by_return_address_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_address_id** | **int**| Return address ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_return_addresses_by_return_address_id_put**
> str post_return_addresses_by_return_address_id_put(return_address_id, return_address)

Update post return address

Update post return address

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
api_instance = clicksend_client.PostReturnAddressApi(clicksend_client.ApiClient(configuration))
return_address_id = 56 # int | Return address ID
return_address = clicksend_client.Address() # Address | Address model

try:
    # Update post return address
    api_response = api_instance.post_return_addresses_by_return_address_id_put(return_address_id, return_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReturnAddressApi->post_return_addresses_by_return_address_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_address_id** | **int**| Return address ID | 
 **return_address** | [**Address**](Address.md)| Address model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_return_addresses_get**
> str post_return_addresses_get(page=page, limit=limit)

Get list of post return addresses

Get list of post return addresses

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
api_instance = clicksend_client.PostReturnAddressApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of post return addresses
    api_response = api_instance.post_return_addresses_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReturnAddressApi->post_return_addresses_get: %s\n" % e)
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

# **post_return_addresses_post**
> str post_return_addresses_post(return_address)

Create post return address

Create post return address

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
api_instance = clicksend_client.PostReturnAddressApi(clicksend_client.ApiClient(configuration))
return_address = clicksend_client.Address() # Address | Address model

try:
    # Create post return address
    api_response = api_instance.post_return_addresses_post(return_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReturnAddressApi->post_return_addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_address** | [**Address**](Address.md)| Address model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

