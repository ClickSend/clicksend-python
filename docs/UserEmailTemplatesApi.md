# clicksend_client.UserEmailTemplatesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_template_delete**](UserEmailTemplatesApi.md#email_template_delete) | **DELETE** /email/templates/{template_id} | Delete user email template
[**email_template_get**](UserEmailTemplatesApi.md#email_template_get) | **GET** /email/templates/{template_id} | Get specific user email template
[**email_template_post**](UserEmailTemplatesApi.md#email_template_post) | **POST** /email/templates | Create email template
[**email_template_put**](UserEmailTemplatesApi.md#email_template_put) | **PUT** /email/templates/{template_id} | Update email template
[**email_templates_get**](UserEmailTemplatesApi.md#email_templates_get) | **GET** /email/templates | Get all user email templates


# **email_template_delete**
> str email_template_delete(template_id)

Delete user email template

Delete user email template

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
api_instance = clicksend_client.UserEmailTemplatesApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Email template id

try:
    # Delete user email template
    api_response = api_instance.email_template_delete(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserEmailTemplatesApi->email_template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Email template id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_template_get**
> str email_template_get(template_id)

Get specific user email template

Get specific user email templates

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
api_instance = clicksend_client.UserEmailTemplatesApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Email template id

try:
    # Get specific user email template
    api_response = api_instance.email_template_get(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserEmailTemplatesApi->email_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Email template id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_template_post**
> str email_template_post(email_template)

Create email template

Create email template

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
api_instance = clicksend_client.UserEmailTemplatesApi(clicksend_client.ApiClient(configuration))
email_template = clicksend_client.EmailTemplateNew() # EmailTemplateNew | Email template model

try:
    # Create email template
    api_response = api_instance.email_template_post(email_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserEmailTemplatesApi->email_template_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template** | [**EmailTemplateNew**](EmailTemplateNew.md)| Email template model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_template_put**
> str email_template_put(template_id, email_template)

Update email template

Update email template

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
api_instance = clicksend_client.UserEmailTemplatesApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Email template id
email_template = clicksend_client.EmailTemplateUpdate() # EmailTemplateUpdate | Email template model

try:
    # Update email template
    api_response = api_instance.email_template_put(template_id, email_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserEmailTemplatesApi->email_template_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Email template id | 
 **email_template** | [**EmailTemplateUpdate**](EmailTemplateUpdate.md)| Email template model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_templates_get**
> str email_templates_get(page=page, limit=limit)

Get all user email templates

Get all user email templates

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
api_instance = clicksend_client.UserEmailTemplatesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all user email templates
    api_response = api_instance.email_templates_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserEmailTemplatesApi->email_templates_get: %s\n" % e)
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

