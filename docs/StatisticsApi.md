# clicksend_client.StatisticsApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_mms_get**](StatisticsApi.md#statistics_mms_get) | **GET** /statistics/mms | Get mms statistics
[**statistics_sms_get**](StatisticsApi.md#statistics_sms_get) | **GET** /statistics/sms | Get sms statistics
[**statistics_voice_get**](StatisticsApi.md#statistics_voice_get) | **GET** /statistics/voice | Get voice statistics


# **statistics_mms_get**
> str statistics_mms_get()

Get mms statistics

Get mms statistics

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
api_instance = clicksend_client.StatisticsApi(clicksend_client.ApiClient(configuration))

try:
    # Get mms statistics
    api_response = api_instance.statistics_mms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_mms_get: %s\n" % e)
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

# **statistics_sms_get**
> str statistics_sms_get()

Get sms statistics

Get sms statistics

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
api_instance = clicksend_client.StatisticsApi(clicksend_client.ApiClient(configuration))

try:
    # Get sms statistics
    api_response = api_instance.statistics_sms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_sms_get: %s\n" % e)
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

# **statistics_voice_get**
> str statistics_voice_get()

Get voice statistics

Get voice statistics

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
api_instance = clicksend_client.StatisticsApi(clicksend_client.ApiClient(configuration))

try:
    # Get voice statistics
    api_response = api_instance.statistics_voice_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_voice_get: %s\n" % e)
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

