# clicksend_client.EmailToSmsApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_email_sms_get**](EmailToSmsApi.md#sms_email_sms_get) | **GET** /sms/email-sms | Get list of email to sms allowed addresses
[**sms_email_sms_post**](EmailToSmsApi.md#sms_email_sms_post) | **POST** /sms/email-sms | Create email to sms allowed address
[**sms_email_sms_stripped_string_delete**](EmailToSmsApi.md#sms_email_sms_stripped_string_delete) | **DELETE** /sms/email-sms-stripped-strings/{rule_id} | Delete email to sms stripped string rule
[**sms_email_sms_stripped_string_get**](EmailToSmsApi.md#sms_email_sms_stripped_string_get) | **GET** /sms/email-sms-stripped-strings/{rule_id} | Get email to sms stripped string rule
[**sms_email_sms_stripped_string_post**](EmailToSmsApi.md#sms_email_sms_stripped_string_post) | **POST** /sms/email-sms-stripped-strings | Create email to sms stripped string rule
[**sms_email_sms_stripped_string_put**](EmailToSmsApi.md#sms_email_sms_stripped_string_put) | **PUT** /sms/email-sms-stripped-strings/{rule_id} | Update email to sms stripped string rule
[**sms_email_sms_stripped_strings_get**](EmailToSmsApi.md#sms_email_sms_stripped_strings_get) | **GET** /sms/email-sms-stripped-strings | Get list of email to sms stripped string rules


# **sms_email_sms_get**
> str sms_email_sms_get(page=page, limit=limit)

Get list of email to sms allowed addresses

Get list of email to sms allowed addresses

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of email to sms allowed addresses
    api_response = api_instance.sms_email_sms_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_get: %s\n" % e)
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

# **sms_email_sms_post**
> str sms_email_sms_post(email_sms_address)

Create email to sms allowed address

Create email to sms allowed address

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
email_sms_address = clicksend_client.EmailSMSAddress() # EmailSMSAddress | EmailSMSAddress model

try:
    # Create email to sms allowed address
    api_response = api_instance.sms_email_sms_post(email_sms_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_sms_address** | [**EmailSMSAddress**](EmailSMSAddress.md)| EmailSMSAddress model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_email_sms_stripped_string_delete**
> str sms_email_sms_stripped_string_delete(rule_id)

Delete email to sms stripped string rule

Delete email to sms stripped string rule

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
rule_id = 56 # int | Your rule id

try:
    # Delete email to sms stripped string rule
    api_response = api_instance.sms_email_sms_stripped_string_delete(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_stripped_string_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| Your rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_email_sms_stripped_string_get**
> str sms_email_sms_stripped_string_get(rule_id)

Get email to sms stripped string rule

Get email to sms stripped string rule

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
rule_id = 56 # int | Your rule id

try:
    # Get email to sms stripped string rule
    api_response = api_instance.sms_email_sms_stripped_string_get(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_stripped_string_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| Your rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_email_sms_stripped_string_post**
> str sms_email_sms_stripped_string_post(stripped_string)

Create email to sms stripped string rule

Create email to sms stripped string rules

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
stripped_string = clicksend_client.StrippedString() # StrippedString | StrippedString model

try:
    # Create email to sms stripped string rule
    api_response = api_instance.sms_email_sms_stripped_string_post(stripped_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_stripped_string_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripped_string** | [**StrippedString**](StrippedString.md)| StrippedString model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_email_sms_stripped_string_put**
> str sms_email_sms_stripped_string_put(stripped_string, rule_id)

Update email to sms stripped string rule

Update email to sms stripped string rule

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
stripped_string = clicksend_client.StrippedString() # StrippedString | StrippedString model
rule_id = 56 # int | Your rule id

try:
    # Update email to sms stripped string rule
    api_response = api_instance.sms_email_sms_stripped_string_put(stripped_string, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_stripped_string_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripped_string** | [**StrippedString**](StrippedString.md)| StrippedString model | 
 **rule_id** | **int**| Your rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_email_sms_stripped_strings_get**
> str sms_email_sms_stripped_strings_get(page=page, limit=limit)

Get list of email to sms stripped string rules

Get list of email to sms stripped string rules

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
api_instance = clicksend_client.EmailToSmsApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of email to sms stripped string rules
    api_response = api_instance.sms_email_sms_stripped_strings_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailToSmsApi->sms_email_sms_stripped_strings_get: %s\n" % e)
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

