# clicksend_client.MasterEmailTemplatesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**master_email_template_categories_get**](MasterEmailTemplatesApi.md#master_email_template_categories_get) | **GET** /email/master-templates-categories | Get all master email template categories
[**master_email_template_category_get**](MasterEmailTemplatesApi.md#master_email_template_category_get) | **GET** /email/master-templates-categories/{category_id} | Get specific master email template category
[**master_email_template_get**](MasterEmailTemplatesApi.md#master_email_template_get) | **GET** /email/master-templates/{template_id} | Get specific master email template
[**master_email_templates_get**](MasterEmailTemplatesApi.md#master_email_templates_get) | **GET** /email/master-templates | Get all master email templates
[**master_email_templates_in_category_get**](MasterEmailTemplatesApi.md#master_email_templates_in_category_get) | **GET** /email/master-templates-categories/{category_id}/master-templates | Get all master email templates in a category


# **master_email_template_categories_get**
> str master_email_template_categories_get(page=page, limit=limit)

Get all master email template categories

Get all master email template categories

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
api_instance = clicksend_client.MasterEmailTemplatesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all master email template categories
    api_response = api_instance.master_email_template_categories_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterEmailTemplatesApi->master_email_template_categories_get: %s\n" % e)
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

# **master_email_template_category_get**
> str master_email_template_category_get(category_id)

Get specific master email template category

Get specific master email template category

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
api_instance = clicksend_client.MasterEmailTemplatesApi(clicksend_client.ApiClient(configuration))
category_id = 56 # int | Email category id

try:
    # Get specific master email template category
    api_response = api_instance.master_email_template_category_get(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterEmailTemplatesApi->master_email_template_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Email category id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **master_email_template_get**
> str master_email_template_get(template_id)

Get specific master email template

Get specific master email template

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
api_instance = clicksend_client.MasterEmailTemplatesApi(clicksend_client.ApiClient(configuration))
template_id = 56 # int | Email template id

try:
    # Get specific master email template
    api_response = api_instance.master_email_template_get(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterEmailTemplatesApi->master_email_template_get: %s\n" % e)
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

# **master_email_templates_get**
> str master_email_templates_get(page=page, limit=limit)

Get all master email templates

Get all master email templates

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
api_instance = clicksend_client.MasterEmailTemplatesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all master email templates
    api_response = api_instance.master_email_templates_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterEmailTemplatesApi->master_email_templates_get: %s\n" % e)
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

# **master_email_templates_in_category_get**
> str master_email_templates_in_category_get(category_id, page=page, limit=limit)

Get all master email templates in a category

Get all master email templates in a category

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
api_instance = clicksend_client.MasterEmailTemplatesApi(clicksend_client.ApiClient(configuration))
category_id = 56 # int | Email category id
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all master email templates in a category
    api_response = api_instance.master_email_templates_in_category_get(category_id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterEmailTemplatesApi->master_email_templates_in_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Email category id | 
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

