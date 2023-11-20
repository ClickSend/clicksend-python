# clicksend_client.ContactApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lists_contacts_by_list_id_and_contact_id_delete**](ContactApi.md#lists_contacts_by_list_id_and_contact_id_delete) | **DELETE** /lists/{list_id}/contacts/{contact_id} | Delete a contact
[**lists_contacts_by_list_id_and_contact_id_get**](ContactApi.md#lists_contacts_by_list_id_and_contact_id_get) | **GET** /lists/{list_id}/contacts/{contact_id} | Get a specific contact
[**lists_contacts_by_list_id_and_contact_id_put**](ContactApi.md#lists_contacts_by_list_id_and_contact_id_put) | **PUT** /lists/{list_id}/contacts/{contact_id} | Update specific contact
[**lists_contacts_by_list_id_get**](ContactApi.md#lists_contacts_by_list_id_get) | **GET** /lists/{list_id}/contacts | Get all contacts in a list
[**lists_contacts_by_list_id_post**](ContactApi.md#lists_contacts_by_list_id_post) | **POST** /lists/{list_id}/contacts | Create new contact
[**lists_copy_contact_put**](ContactApi.md#lists_copy_contact_put) | **PUT** /lists/{from_list_id}/contacts/{contact_id}/copy/{to_list_id} | Copy contact to another list
[**lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put**](ContactApi.md#lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put) | **PUT** /lists/{list_id}/remove-opted-out-contacts/{opt_out_list_id} | Remove all opted out contacts
[**lists_transfer_contact_put**](ContactApi.md#lists_transfer_contact_put) | **PUT** /lists/{from_list_id}/contacts/{contact_id}/transfer/{to_list_id} | Transfer contact to another list


# **lists_contacts_by_list_id_and_contact_id_delete**
> str lists_contacts_by_list_id_and_contact_id_delete(list_id, contact_id)

Delete a contact

Delete a contact

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | List ID
contact_id = 56 # int | Contact ID

try:
    # Delete a contact
    api_response = api_instance.lists_contacts_by_list_id_and_contact_id_delete(list_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_contacts_by_list_id_and_contact_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| List ID | 
 **contact_id** | **int**| Contact ID | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_contacts_by_list_id_and_contact_id_get**
> str lists_contacts_by_list_id_and_contact_id_get(list_id, contact_id)

Get a specific contact

Get a specific contact

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Your contact list id you want to access.
contact_id = 56 # int | Your contact id you want to access.

try:
    # Get a specific contact
    api_response = api_instance.lists_contacts_by_list_id_and_contact_id_get(list_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_contacts_by_list_id_and_contact_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Your contact list id you want to access. | 
 **contact_id** | **int**| Your contact id you want to access. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_contacts_by_list_id_and_contact_id_put**
> str lists_contacts_by_list_id_and_contact_id_put(list_id, contact_id, contact)

Update specific contact

Update specific contact

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Contact list id
contact_id = 56 # int | Contact ID
contact = clicksend_client.Contact() # Contact | Contact model

try:
    # Update specific contact
    api_response = api_instance.lists_contacts_by_list_id_and_contact_id_put(list_id, contact_id, contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_contacts_by_list_id_and_contact_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Contact list id | 
 **contact_id** | **int**| Contact ID | 
 **contact** | [**Contact**](Contact.md)| Contact model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_contacts_by_list_id_get**
> str lists_contacts_by_list_id_get(list_id, page=page, limit=limit, updated_after=updated_after)

Get all contacts in a list

Get all contacts in a list

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Contact list ID
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)
updated_after = 10 # int | Get all contacts updated after a given timestamp. (optional) (default to 10)

try:
    # Get all contacts in a list
    api_response = api_instance.lists_contacts_by_list_id_get(list_id, page=page, limit=limit, updated_after=updated_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_contacts_by_list_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Contact list ID | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Number of records per page | [optional] [default to 10]
 **updated_after** | **int**| Get all contacts updated after a given timestamp. | [optional] [default to 10]

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_contacts_by_list_id_post**
> str lists_contacts_by_list_id_post(contact, list_id)

Create new contact

Create new contact

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
contact = clicksend_client.Contact() # Contact | Contact model
list_id = 56 # int | List id

try:
    # Create new contact
    api_response = api_instance.lists_contacts_by_list_id_post(contact, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_contacts_by_list_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)| Contact model | 
 **list_id** | **int**| List id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_copy_contact_put**
> str lists_copy_contact_put(from_list_id, contact_id, to_list_id)

Copy contact to another list

Copy contact to another list

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
from_list_id = 56 # int | List ID for list that contains contact.
contact_id = 56 # int | Contact ID
to_list_id = 56 # int | List ID for list you want to copy the contact to.

try:
    # Copy contact to another list
    api_response = api_instance.lists_copy_contact_put(from_list_id, contact_id, to_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_copy_contact_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_list_id** | **int**| List ID for list that contains contact. | 
 **contact_id** | **int**| Contact ID | 
 **to_list_id** | **int**| List ID for list you want to copy the contact to. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put**
> str lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put(list_id, opt_out_list_id)

Remove all opted out contacts

Remove all opted out contacts

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
list_id = 56 # int | Your list id
opt_out_list_id = 56 # int | Your opt out list id

try:
    # Remove all opted out contacts
    api_response = api_instance.lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put(list_id, opt_out_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| Your list id | 
 **opt_out_list_id** | **int**| Your opt out list id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_transfer_contact_put**
> str lists_transfer_contact_put(from_list_id, contact_id, to_list_id)

Transfer contact to another list

Transfer contact to another list

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
api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
from_list_id = 56 # int | List ID for list that contains contact.
contact_id = 56 # int | Contact ID
to_list_id = 56 # int | List ID for list you want to transfer contact to.

try:
    # Transfer contact to another list
    api_response = api_instance.lists_transfer_contact_put(from_list_id, contact_id, to_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->lists_transfer_contact_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_list_id** | **int**| List ID for list that contains contact. | 
 **contact_id** | **int**| Contact ID | 
 **to_list_id** | **int**| List ID for list you want to transfer contact to. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

