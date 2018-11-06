# clicksend_client.TransferCreditApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reseller_transfer_credit_put**](TransferCreditApi.md#reseller_transfer_credit_put) | **PUT** /reseller/transfer-credit | Transfer Credit


# **reseller_transfer_credit_put**
> str reseller_transfer_credit_put(reseller_account_transfer_credit)

Transfer Credit

Transfer Credit

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
api_instance = clicksend_client.TransferCreditApi(clicksend_client.ApiClient(configuration))
reseller_account_transfer_credit = clicksend_client.ResellerAccountTransferCredit() # ResellerAccountTransferCredit | ResellerAccountTransferCredit model

try:
    # Transfer Credit
    api_response = api_instance.reseller_transfer_credit_put(reseller_account_transfer_credit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferCreditApi->reseller_transfer_credit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_account_transfer_credit** | [**ResellerAccountTransferCredit**](ResellerAccountTransferCredit.md)| ResellerAccountTransferCredit model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

