# swagger_client.EmailMarketingApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allowed_email_address_get**](EmailMarketingApi.md#allowed_email_address_get) | **GET** /email/addresses | Get all email addresses
[**allowed_email_address_post**](EmailMarketingApi.md#allowed_email_address_post) | **POST** /email/addresses | Create allowed Email Address
[**cancel_email_campaign_put**](EmailMarketingApi.md#cancel_email_campaign_put) | **PUT** /email-campaigns/{email_campaign_id}/cancel | Cancel email campaign
[**email_campaign_get**](EmailMarketingApi.md#email_campaign_get) | **GET** /email-campaigns/{email_campaign_id} | Get specific email campaign
[**email_campaign_history_export_get**](EmailMarketingApi.md#email_campaign_history_export_get) | **GET** /email-campaigns/{email_campaign_id}/history/export | Export specific email campaign history
[**email_campaign_history_get**](EmailMarketingApi.md#email_campaign_history_get) | **GET** /email-campaigns/{email_campaign_id}/history | Get specific email campaign history
[**email_campaign_post**](EmailMarketingApi.md#email_campaign_post) | **POST** /email-campaigns/send | Send email campaign
[**email_campaign_price_post**](EmailMarketingApi.md#email_campaign_price_post) | **POST** /email-campaigns/price | Calculate email campaign price
[**email_campaign_put**](EmailMarketingApi.md#email_campaign_put) | **PUT** /email-campaigns/{email_campaign_id} | Edit email campaign
[**email_campaigns_get**](EmailMarketingApi.md#email_campaigns_get) | **GET** /email-campaigns | Get all email campaigns
[**send_verification_token_get**](EmailMarketingApi.md#send_verification_token_get) | **GET** /email/address-verify/{email_address_id}/send | Send verification token
[**specific_allowed_email_address_delete**](EmailMarketingApi.md#specific_allowed_email_address_delete) | **DELETE** /email/addresses/{email_address_id} | Delete specific email address
[**specific_allowed_email_address_get**](EmailMarketingApi.md#specific_allowed_email_address_get) | **GET** /email/addresses/{email_address_id} | Get specific email address
[**verify_allowed_email_address_get**](EmailMarketingApi.md#verify_allowed_email_address_get) | **GET** /email/address-verify/{email_address_id}/verify/{activation_token} | Verify email address using verification token


# **allowed_email_address_get**
> str allowed_email_address_get(page=page, limit=limit)

Get all email addresses

Get all email addresses

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all email addresses
    api_response = api_instance.allowed_email_address_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->allowed_email_address_get: %s\n" % e)
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

# **allowed_email_address_post**
> str allowed_email_address_post(email_address)

Create allowed Email Address

Create allowed Email Address

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_address = 'email_address_example' # str | Email to be allowed.

try:
    # Create allowed Email Address
    api_response = api_instance.allowed_email_address_post(email_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->allowed_email_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email to be allowed. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_email_campaign_put**
> str cancel_email_campaign_put(email_campaign_id)

Cancel email campaign

Cancel email campaign

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign_id = 56 # int | Allowed email campaign id

try:
    # Cancel email campaign
    api_response = api_instance.cancel_email_campaign_put(email_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->cancel_email_campaign_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_id** | **int**| Allowed email campaign id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaign_get**
> str email_campaign_get(email_campaign_id)

Get specific email campaign

Get specific email campaign

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign_id = 56 # int | Allowed email campaign id

try:
    # Get specific email campaign
    api_response = api_instance.email_campaign_get(email_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_id** | **int**| Allowed email campaign id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaign_history_export_get**
> file email_campaign_history_export_get(email_campaign_id, date_from=date_from, date_to=date_to)

Export specific email campaign history

Export specific email campaign history

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign_id = 56 # int | Allowed email campaign id
date_from = 56 # int | Start date (optional)
date_to = 56 # int | End date (optional)

try:
    # Export specific email campaign history
    api_response = api_instance.email_campaign_history_export_get(email_campaign_id, date_from=date_from, date_to=date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_history_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_id** | **int**| Allowed email campaign id | 
 **date_from** | **int**| Start date | [optional] 
 **date_to** | **int**| End date | [optional] 

### Return type

[**file**](file.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaign_history_get**
> str email_campaign_history_get(email_campaign_id, date_from=date_from, date_to=date_to, page=page, limit=limit)

Get specific email campaign history

Get specific email campaign history

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign_id = 56 # int | Allowed email campaign id
date_from = 56 # int | Start date (optional)
date_to = 56 # int | End date (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get specific email campaign history
    api_response = api_instance.email_campaign_history_get(email_campaign_id, date_from=date_from, date_to=date_to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_id** | **int**| Allowed email campaign id | 
 **date_from** | **int**| Start date | [optional] 
 **date_to** | **int**| End date | [optional] 
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

# **email_campaign_post**
> str email_campaign_post(email_campaign)

Send email campaign

Send email campaign

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign = swagger_client.EmailCampaign() # EmailCampaign | Email model

try:
    # Send email campaign
    api_response = api_instance.email_campaign_post(email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaign_price_post**
> str email_campaign_price_post(email_campaign)

Calculate email campaign price

Calculate email campaign price

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign = swagger_client.EmailCampaign() # EmailCampaign | Email model

try:
    # Calculate email campaign price
    api_response = api_instance.email_campaign_price_post(email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaign_put**
> str email_campaign_put(email_campaign_id)

Edit email campaign

Edit email campaign

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_campaign_id = 56 # int | Allowed email campaign id

try:
    # Edit email campaign
    api_response = api_instance.email_campaign_put(email_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaign_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_id** | **int**| Allowed email campaign id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_campaigns_get**
> str email_campaigns_get(page=page, limit=limit)

Get all email campaigns

Get all email campaigns

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all email campaigns
    api_response = api_instance.email_campaigns_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->email_campaigns_get: %s\n" % e)
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

# **send_verification_token_get**
> str send_verification_token_get(email_address_id)

Send verification token

Send verification token

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_address_id = 56 # int | Allowed email address id

try:
    # Send verification token
    api_response = api_instance.send_verification_token_get(email_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->send_verification_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **int**| Allowed email address id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specific_allowed_email_address_delete**
> str specific_allowed_email_address_delete(email_address_id)

Delete specific email address

Delete specific email address

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_address_id = 56 # int | Allowed email address id

try:
    # Delete specific email address
    api_response = api_instance.specific_allowed_email_address_delete(email_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->specific_allowed_email_address_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **int**| Allowed email address id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specific_allowed_email_address_get**
> str specific_allowed_email_address_get(email_address_id)

Get specific email address

Get specific email address

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_address_id = 56 # int | Allowed email address id

try:
    # Get specific email address
    api_response = api_instance.specific_allowed_email_address_get(email_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->specific_allowed_email_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **int**| Allowed email address id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_allowed_email_address_get**
> str verify_allowed_email_address_get(email_address_id, activation_token)

Verify email address using verification token

Verify email address using verification token

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
api_instance = swagger_client.EmailMarketingApi(swagger_client.ApiClient(configuration))
email_address_id = 56 # int | Allowed email address id
activation_token = 'activation_token_example' # str | Your activation token.

try:
    # Verify email address using verification token
    api_response = api_instance.verify_allowed_email_address_get(email_address_id, activation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailMarketingApi->verify_allowed_email_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **int**| Allowed email address id | 
 **activation_token** | **str**| Your activation token. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

