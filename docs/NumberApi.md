# swagger_client.NumberApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbers_buy_by_dedicated_number_post**](NumberApi.md#numbers_buy_by_dedicated_number_post) | **POST** /numbers/buy/{dedicated_number} | Buy dedicated number
[**numbers_get**](NumberApi.md#numbers_get) | **GET** /numbers | Get all availible dedicated numbers
[**numbers_search_by_country_get**](NumberApi.md#numbers_search_by_country_get) | **GET** /numbers/search/{country} | Get all dedicated numbers by country


# **numbers_buy_by_dedicated_number_post**
> str numbers_buy_by_dedicated_number_post(dedicated_number)

Buy dedicated number

Buy dedicated number

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
api_instance = swagger_client.NumberApi(swagger_client.ApiClient(configuration))
dedicated_number = 'dedicated_number_example' # str | Phone number to purchase

try:
    # Buy dedicated number
    api_response = api_instance.numbers_buy_by_dedicated_number_post(dedicated_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->numbers_buy_by_dedicated_number_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedicated_number** | **str**| Phone number to purchase | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_get**
> str numbers_get(page=page, limit=limit)

Get all availible dedicated numbers

Get all availible dedicated numbers

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
api_instance = swagger_client.NumberApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all availible dedicated numbers
    api_response = api_instance.numbers_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->numbers_get: %s\n" % e)
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

# **numbers_search_by_country_get**
> str numbers_search_by_country_get(country, search=search, search_type=search_type, page=page, limit=limit)

Get all dedicated numbers by country

Get all dedicated numbers by country

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
api_instance = swagger_client.NumberApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Country code to search
search = 'search_example' # str | Your search pattern or query. (optional)
search_type = 56 # int | Your strategy for searching, 0 = starts with, 1 = anywhere, 2 = ends with. (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all dedicated numbers by country
    api_response = api_instance.numbers_search_by_country_get(country, search=search, search_type=search_type, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->numbers_search_by_country_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country code to search | 
 **search** | **str**| Your search pattern or query. | [optional] 
 **search_type** | **int**| Your strategy for searching, 0 &#x3D; starts with, 1 &#x3D; anywhere, 2 &#x3D; ends with. | [optional] 
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

