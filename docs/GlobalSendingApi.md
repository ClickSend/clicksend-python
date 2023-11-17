# clicksend_client.GlobalSendingApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_countries_get**](GlobalSendingApi.md#list_countries_get) | **GET** /country-list | List of countries
[**user_countries_agree_post**](GlobalSendingApi.md#user_countries_agree_post) | **POST** /user-countries/agree | Agree to rules and regulation
[**user_countries_get**](GlobalSendingApi.md#user_countries_get) | **GET** /user-countries | Get Countries for Global Sending
[**user_countries_post**](GlobalSendingApi.md#user_countries_post) | **POST** /user-countries | Select Countries for Global Sending


# **list_countries_get**
> str list_countries_get()

List of countries

List of countries with IDs that can be used in selecting countries for Global sending.

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
api_instance = clicksend_client.GlobalSendingApi(clicksend_client.ApiClient(configuration))

try:
    # List of countries
    api_response = api_instance.list_countries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalSendingApi->list_countries_get: %s\n" % e)
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

# **user_countries_agree_post**
> str user_countries_agree_post()

Agree to rules and regulation

To agree on rules and regulations of selected countries and confirm selection.

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
api_instance = clicksend_client.GlobalSendingApi(clicksend_client.ApiClient(configuration))

try:
    # Agree to rules and regulation
    api_response = api_instance.user_countries_agree_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalSendingApi->user_countries_agree_post: %s\n" % e)
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

# **user_countries_get**
> str user_countries_get()

Get Countries for Global Sending

Get the list of selected countries.

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
api_instance = clicksend_client.GlobalSendingApi(clicksend_client.ApiClient(configuration))

try:
    # Get Countries for Global Sending
    api_response = api_instance.user_countries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalSendingApi->user_countries_get: %s\n" % e)
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

# **user_countries_post**
> str user_countries_post(country_list_ids)

Select Countries for Global Sending

Use this endpoint to select countries that you intend to send sms / mms to. To remove / unselect a country, just remove the country id from the array in the payload.

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
api_instance = clicksend_client.GlobalSendingApi(clicksend_client.ApiClient(configuration))
country_list_ids = clicksend_client.CountryListIds() # CountryListIds | Id of countr(ies) you want to select, you can get them from GET /country-list response

try:
    # Select Countries for Global Sending
    api_response = api_instance.user_countries_post(country_list_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalSendingApi->user_countries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_list_ids** | [**CountryListIds**](CountryListIds.md)| Id of countr(ies) you want to select, you can get them from GET /country-list response | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

