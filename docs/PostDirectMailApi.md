# swagger_client.PostDirectMailApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_direct_mail_campaigns_get**](PostDirectMailApi.md#post_direct_mail_campaigns_get) | **GET** /post/direct-mail/campaigns | Get direct mail campaigns
[**post_direct_mail_campaigns_price_post**](PostDirectMailApi.md#post_direct_mail_campaigns_price_post) | **POST** /post/direct-mail/campaigns/price | Calculate direct mail campaign price
[**post_direct_mail_campaigns_send_post**](PostDirectMailApi.md#post_direct_mail_campaigns_send_post) | **POST** /post/direct-mail/campaigns/send | Send direct mail campaign
[**post_direct_mail_locations_search_by_country_get**](PostDirectMailApi.md#post_direct_mail_locations_search_by_country_get) | **GET** /post/direct-mail/locations/search/{country} | Search for a location


# **post_direct_mail_campaigns_get**
> str post_direct_mail_campaigns_get(page=page, limit=limit)

Get direct mail campaigns

Get direct mail campaigns

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
api_instance = swagger_client.PostDirectMailApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get direct mail campaigns
    api_response = api_instance.post_direct_mail_campaigns_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostDirectMailApi->post_direct_mail_campaigns_get: %s\n" % e)
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

# **post_direct_mail_campaigns_price_post**
> str post_direct_mail_campaigns_price_post(post_direct_mail)

Calculate direct mail campaign price

Calculate direct mail campaign price

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
api_instance = swagger_client.PostDirectMailApi(swagger_client.ApiClient(configuration))
post_direct_mail = swagger_client.PostDirectMail() # PostDirectMail | PostDirectMail model

try:
    # Calculate direct mail campaign price
    api_response = api_instance.post_direct_mail_campaigns_price_post(post_direct_mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostDirectMailApi->post_direct_mail_campaigns_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_direct_mail** | [**PostDirectMail**](PostDirectMail.md)| PostDirectMail model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_direct_mail_campaigns_send_post**
> str post_direct_mail_campaigns_send_post(post_direct_mail)

Send direct mail campaign

Send direct mail campaign

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
api_instance = swagger_client.PostDirectMailApi(swagger_client.ApiClient(configuration))
post_direct_mail = swagger_client.PostDirectMail() # PostDirectMail | PostDirectMail model

try:
    # Send direct mail campaign
    api_response = api_instance.post_direct_mail_campaigns_send_post(post_direct_mail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostDirectMailApi->post_direct_mail_campaigns_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_direct_mail** | [**PostDirectMail**](PostDirectMail.md)| PostDirectMail model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_direct_mail_locations_search_by_country_get**
> str post_direct_mail_locations_search_by_country_get(country, q, page=page, limit=limit)

Search for a location

Search for a location

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
api_instance = swagger_client.PostDirectMailApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Country Code to search
q = 'q_example' # str | Search term (e.g. post code, city name)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Search for a location
    api_response = api_instance.post_direct_mail_locations_search_by_country_get(country, q, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostDirectMailApi->post_direct_mail_locations_search_by_country_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country Code to search | 
 **q** | **str**| Search term (e.g. post code, city name) | 
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

