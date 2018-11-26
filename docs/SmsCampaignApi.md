# clicksend_client.SmsCampaignApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_campaign_by_sms_campaign_id_get**](SmsCampaignApi.md#sms_campaign_by_sms_campaign_id_get) | **GET** /sms-campaigns/{sms_campaign_id} | Get specific sms campaign
[**sms_campaigns_by_sms_campaign_id_put**](SmsCampaignApi.md#sms_campaigns_by_sms_campaign_id_put) | **PUT** /sms-campaigns/{sms_campaign_id} | Update sms campaign
[**sms_campaigns_cancel_by_sms_campaign_id_put**](SmsCampaignApi.md#sms_campaigns_cancel_by_sms_campaign_id_put) | **PUT** /sms-campaigns/{sms_campaign_id}/cancel | Cancel sms campaign
[**sms_campaigns_get**](SmsCampaignApi.md#sms_campaigns_get) | **GET** /sms-campaigns | Get list of sms campaigns
[**sms_campaigns_price_post**](SmsCampaignApi.md#sms_campaigns_price_post) | **POST** /sms-campaigns/price | Calculate price for sms campaign
[**sms_campaigns_send_post**](SmsCampaignApi.md#sms_campaigns_send_post) | **POST** /sms-campaigns/send | Create sms campaign


# **sms_campaign_by_sms_campaign_id_get**
> str sms_campaign_by_sms_campaign_id_get(sms_campaign_id)

Get specific sms campaign

Get specific sms campaign

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
sms_campaign_id = 56 # int | ID of SMS campaign to retrieve

try:
    # Get specific sms campaign
    api_response = api_instance.sms_campaign_by_sms_campaign_id_get(sms_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaign_by_sms_campaign_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **int**| ID of SMS campaign to retrieve | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_campaigns_by_sms_campaign_id_put**
> str sms_campaigns_by_sms_campaign_id_put(sms_campaign_id, campaign)

Update sms campaign

Update sms campaign

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
sms_campaign_id = 56 # int | ID of SMS campaign to update
campaign = clicksend_client.SmsCampaign() # SmsCampaign | SmsCampaign model

try:
    # Update sms campaign
    api_response = api_instance.sms_campaigns_by_sms_campaign_id_put(sms_campaign_id, campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaigns_by_sms_campaign_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **int**| ID of SMS campaign to update | 
 **campaign** | [**SmsCampaign**](SmsCampaign.md)| SmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_campaigns_cancel_by_sms_campaign_id_put**
> str sms_campaigns_cancel_by_sms_campaign_id_put(sms_campaign_id)

Cancel sms campaign

Cancel sms campaign

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
sms_campaign_id = 56 # int | ID of SMS Campaign to cancel

try:
    # Cancel sms campaign
    api_response = api_instance.sms_campaigns_cancel_by_sms_campaign_id_put(sms_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaigns_cancel_by_sms_campaign_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_campaign_id** | **int**| ID of SMS Campaign to cancel | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_campaigns_get**
> str sms_campaigns_get(page=page, limit=limit)

Get list of sms campaigns

Get list of sms campaigns

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of sms campaigns
    api_response = api_instance.sms_campaigns_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaigns_get: %s\n" % e)
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

# **sms_campaigns_price_post**
> str sms_campaigns_price_post(campaign)

Calculate price for sms campaign

Calculate price for sms campaign

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
campaign = clicksend_client.SmsCampaign() # SmsCampaign | SmsCampaign model

try:
    # Calculate price for sms campaign
    api_response = api_instance.sms_campaigns_price_post(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaigns_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**SmsCampaign**](SmsCampaign.md)| SmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_campaigns_send_post**
> str sms_campaigns_send_post(campaign)

Create sms campaign

Create sms campaign

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
api_instance = clicksend_client.SmsCampaignApi(clicksend_client.ApiClient(configuration))
campaign = clicksend_client.SmsCampaign() # SmsCampaign | SmsCampaign model

try:
    # Create sms campaign
    api_response = api_instance.sms_campaigns_send_post(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsCampaignApi->sms_campaigns_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**SmsCampaign**](SmsCampaign.md)| SmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

