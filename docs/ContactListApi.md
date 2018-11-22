# clicksend_client.ContactListApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lists_by_list_id_delete**](ContactListApi.md#lists_by_list_id_delete) | **DELETE** /lists/{list_id} | ListsByListIdDelete
[**lists_by_list_id_get**](ContactListApi.md#lists_by_list_id_get) | **GET** /lists/{list_id} | Get specific contact list
[**lists_by_list_id_put**](ContactListApi.md#lists_by_list_id_put) | **PUT** /lists/{list_id} | Update specific contact list
[**lists_get**](ContactListApi.md#lists_get) | **GET** /lists | Get all contact lists
[**lists_import_by_list_id_post**](ContactListApi.md#lists_import_by_list_id_post) | **POST** /lists/{list_id}/import | Import contacts to list
[**lists_post**](ContactListApi.md#lists_post) | **POST** /lists | Create new contact list
[**lists_remove_duplicates_by_list_id_put**](ContactListApi.md#lists_remove_duplicates_by_list_id_put) | **PUT** /lists/{list_id}/remove-duplicates | Remove duplicate contacts


# **lists_by_list_id_delete**
> str lists_by_list_id_delete(list_id)

ListsByListIdDelete

Delete a specific contact list

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | List ID

try:
    # ListsByListIdDelete
    api_response = api_instance.lists_by_list_id_delete(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_by_list_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| List ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_list_id_get**
> str lists_by_list_id_get(list_id)

Get specific contact list

Get specific contact list

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | List ID

try:
    # Get specific contact list
    api_response = api_instance.lists_by_list_id_get(list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_by_list_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| List ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_by_list_id_put**
> str lists_by_list_id_put(list_id, list)

Update specific contact list

Update specific contact list

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Your list id
list = clicksend_client.List() # List | List model

try:
    # Update specific contact list
    api_response = api_instance.lists_by_list_id_put(list_id, list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_by_list_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Your list id | 
 **list** | [**List**](List.md)| List model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_get**
> str lists_get(page=page, limit=limit)

Get all contact lists

Get all contact lists

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all contact lists
    api_response = api_instance.lists_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_get: %s\n" % e)
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

# **lists_import_by_list_id_post**
> str lists_import_by_list_id_post(list_id, file)

Import contacts to list

Import contacts to list

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Your contact list id you want to access.
file = clicksend_client.ContactListImport() # ContactListImport | ContactListImport model

try:
    # Import contacts to list
    api_response = api_instance.lists_import_by_list_id_post(list_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_import_by_list_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Your contact list id you want to access. | 
 **file** | [**ContactListImport**](ContactListImport.md)| ContactListImport model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_post**
> str lists_post(list)

Create new contact list

Create new contact list

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list = clicksend_client.List() # List | List model

try:
    # Create new contact list
    api_response = api_instance.lists_post(list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | [**List**](List.md)| List model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_remove_duplicates_by_list_id_put**
> str lists_remove_duplicates_by_list_id_put(list_id, fields)

Remove duplicate contacts

Remove duplicate contacts

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
api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Your list id
fields = clicksend_client.Fields() # Fields | Fields model

try:
    # Remove duplicate contacts
    api_response = api_instance.lists_remove_duplicates_by_list_id_put(list_id, fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListApi->lists_remove_duplicates_by_list_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Your list id | 
 **fields** | [**Fields**](Fields.md)| Fields model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

