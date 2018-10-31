# swagger_client.AccountApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get**](AccountApi.md#account_get) | **GET** /account | Get account information
[**account_post**](AccountApi.md#account_post) | **POST** /account | Create a new account
[**account_verify_send_put**](AccountApi.md#account_verify_send_put) | **PUT** /account-verify/send | Send account activation token
[**account_verify_verify_by_activation_token_put**](AccountApi.md#account_verify_verify_by_activation_token_put) | **PUT** /account-verify/verify/{activation_token} | Verify new account
[**forgot_password_put**](AccountApi.md#forgot_password_put) | **PUT** /forgot-password | Forgot password
[**forgot_password_verify_put**](AccountApi.md#forgot_password_verify_put) | **PUT** /forgot-password/verify | Verify forgot password
[**forgot_username_put**](AccountApi.md#forgot_username_put) | **PUT** /forgot-username | Forgot username


# **account_get**
> str account_get()

Get account information

Get account details

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get account information
    api_response = api_instance.account_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get: %s\n" % e)
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

# **account_post**
> str account_post(account)

Create a new account

Create An Account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account = swagger_client.Account() # Account | Account model

try:
    # Create a new account
    api_response = api_instance.account_post(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](Account.md)| Account model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_verify_send_put**
> str account_verify_send_put(account_verify)

Send account activation token

Send account activation token

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_verify = swagger_client.AccountVerify() # AccountVerify | Account details

try:
    # Send account activation token
    api_response = api_instance.account_verify_send_put(account_verify)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_verify_send_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_verify** | [**AccountVerify**](AccountVerify.md)| Account details | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_verify_verify_by_activation_token_put**
> str account_verify_verify_by_activation_token_put(activation_token)

Verify new account

Verify new account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
activation_token = 56 # int | 

try:
    # Verify new account
    api_response = api_instance.account_verify_verify_by_activation_token_put(activation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_verify_verify_by_activation_token_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_token** | **int**|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_put**
> str forgot_password_put(username)

Forgot password

Forgot password

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | Username belonging to account

try:
    # Forgot password
    api_response = api_instance.forgot_password_put(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->forgot_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username belonging to account | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_verify_put**
> str forgot_password_verify_put(verify_password)

Verify forgot password

Verify forgot password

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
verify_password = swagger_client.AccountForgotPasswordVerify() # AccountForgotPasswordVerify | verifyPassword data

try:
    # Verify forgot password
    api_response = api_instance.forgot_password_verify_put(verify_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->forgot_password_verify_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_password** | [**AccountForgotPasswordVerify**](AccountForgotPasswordVerify.md)| verifyPassword data | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_username_put**
> str forgot_username_put(email)

Forgot username

Forgot username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
email = 'email_example' # str | Email belonging to account

try:
    # Forgot username
    api_response = api_instance.forgot_username_put(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->forgot_username_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email belonging to account | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

