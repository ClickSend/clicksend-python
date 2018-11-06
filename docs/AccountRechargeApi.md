# clicksend_client.AccountRechargeApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recharge_credit_card_get**](AccountRechargeApi.md#recharge_credit_card_get) | **GET** /recharge/credit-card | Get Credit Card info
[**recharge_credit_card_put**](AccountRechargeApi.md#recharge_credit_card_put) | **PUT** /recharge/credit-card | Update credit card info
[**recharge_packages_get**](AccountRechargeApi.md#recharge_packages_get) | **GET** /recharge/packages | Get list of all packages
[**recharge_purchase_by_package_id_put**](AccountRechargeApi.md#recharge_purchase_by_package_id_put) | **PUT** /recharge/purchase/{package_id} | Purchase a package
[**recharge_transactions_by_transaction_id_get**](AccountRechargeApi.md#recharge_transactions_by_transaction_id_get) | **GET** /recharge/transactions/{transaction_id} | Get specific Transaction
[**recharge_transactions_get**](AccountRechargeApi.md#recharge_transactions_get) | **GET** /recharge/transactions | Purchase a package


# **recharge_credit_card_get**
> str recharge_credit_card_get()

Get Credit Card info

Get Credit Card info

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))

try:
    # Get Credit Card info
    api_response = api_instance.recharge_credit_card_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_credit_card_get: %s\n" % e)
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

# **recharge_credit_card_put**
> str recharge_credit_card_put(credit_card)

Update credit card info

Update credit card info

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))
credit_card = clicksend_client.CreditCard() # CreditCard | CreditCard model

try:
    # Update credit card info
    api_response = api_instance.recharge_credit_card_put(credit_card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_credit_card_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card** | [**CreditCard**](CreditCard.md)| CreditCard model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recharge_packages_get**
> str recharge_packages_get(country=country)

Get list of all packages

Get list of all packages

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))
country = 'country_example' # str | Country code (optional)

try:
    # Get list of all packages
    api_response = api_instance.recharge_packages_get(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_packages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country code | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recharge_purchase_by_package_id_put**
> str recharge_purchase_by_package_id_put(package_id)

Purchase a package

Purchase a package

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))
package_id = 56 # int | ID of package to purchase

try:
    # Purchase a package
    api_response = api_instance.recharge_purchase_by_package_id_put(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_purchase_by_package_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **int**| ID of package to purchase | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recharge_transactions_by_transaction_id_get**
> str recharge_transactions_by_transaction_id_get(transaction_id)

Get specific Transaction

Get specific Transaction

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | ID of transaction to retrieve

try:
    # Get specific Transaction
    api_response = api_instance.recharge_transactions_by_transaction_id_get(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_transactions_by_transaction_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of transaction to retrieve | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recharge_transactions_get**
> str recharge_transactions_get(page=page, limit=limit)

Purchase a package

Get all transactions

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
api_instance = clicksend_client.AccountRechargeApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Purchase a package
    api_response = api_instance.recharge_transactions_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountRechargeApi->recharge_transactions_get: %s\n" % e)
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

