# swagger_client.ResellerAccountApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reseller_accounts_by_client_user_id_get**](ResellerAccountApi.md#reseller_accounts_by_client_user_id_get) | **GET** /reseller/accounts/{client_user_id} | Get Reseller clients Account
[**reseller_accounts_by_client_user_id_put**](ResellerAccountApi.md#reseller_accounts_by_client_user_id_put) | **PUT** /reseller/accounts/{client_user_id} | Update Reseller clients Account
[**reseller_accounts_get**](ResellerAccountApi.md#reseller_accounts_get) | **GET** /reseller/accounts | Get list of reseller accounts
[**reseller_accounts_post**](ResellerAccountApi.md#reseller_accounts_post) | **POST** /reseller/accounts | Create reseller account


# **reseller_accounts_by_client_user_id_get**
> str reseller_accounts_by_client_user_id_get(client_user_id)

Get Reseller clients Account

Get Reseller clients Account

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
api_instance = swagger_client.ResellerAccountApi(swagger_client.ApiClient(configuration))
client_user_id = 56 # int | User ID of client

try:
    # Get Reseller clients Account
    api_response = api_instance.reseller_accounts_by_client_user_id_get(client_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAccountApi->reseller_accounts_by_client_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_user_id** | **int**| User ID of client | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reseller_accounts_by_client_user_id_put**
> str reseller_accounts_by_client_user_id_put(client_user_id, reseller_account)

Update Reseller clients Account

Update Reseller clients Account

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
api_instance = swagger_client.ResellerAccountApi(swagger_client.ApiClient(configuration))
client_user_id = 56 # int | User ID of client
reseller_account = swagger_client.ResellerAccount() # ResellerAccount | ResellerAccount model

try:
    # Update Reseller clients Account
    api_response = api_instance.reseller_accounts_by_client_user_id_put(client_user_id, reseller_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAccountApi->reseller_accounts_by_client_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_user_id** | **int**| User ID of client | 
 **reseller_account** | [**ResellerAccount**](ResellerAccount.md)| ResellerAccount model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reseller_accounts_get**
> str reseller_accounts_get(page=page, limit=limit)

Get list of reseller accounts

Get list of reseller accounts

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
api_instance = swagger_client.ResellerAccountApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of reseller accounts
    api_response = api_instance.reseller_accounts_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAccountApi->reseller_accounts_get: %s\n" % e)
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

# **reseller_accounts_post**
> str reseller_accounts_post(reseller_account)

Create reseller account

Create reseller account

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
api_instance = swagger_client.ResellerAccountApi(swagger_client.ApiClient(configuration))
reseller_account = swagger_client.ResellerAccount() # ResellerAccount | ResellerAccount model

try:
    # Create reseller account
    api_response = api_instance.reseller_accounts_post(reseller_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAccountApi->reseller_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_account** | [**ResellerAccount**](ResellerAccount.md)| ResellerAccount model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

