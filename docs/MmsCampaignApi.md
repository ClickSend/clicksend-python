# clicksend_client.MmsCampaignApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mms_campaign_by_mms_campaign_id_get**](MmsCampaignApi.md#mms_campaign_by_mms_campaign_id_get) | **GET** /mms-campaign/{mms_campaign_id} | Get specific mms campaign
[**mms_campaigns_by_mms_campaign_id_put**](MmsCampaignApi.md#mms_campaigns_by_mms_campaign_id_put) | **PUT** /mms-campaigns/{mms_campaign_id} | Update mms campaign
[**mms_campaigns_cancel_by_mms_campaign_id_put**](MmsCampaignApi.md#mms_campaigns_cancel_by_mms_campaign_id_put) | **PUT** /mms-campaigns/{mms_campaign_id}/cancel | Cancel mms campaign
[**mms_campaigns_get**](MmsCampaignApi.md#mms_campaigns_get) | **GET** /mms-campaigns | Get list of mms campaigns
[**mms_campaigns_price_post**](MmsCampaignApi.md#mms_campaigns_price_post) | **POST** /mms-campaigns/price | Calculate price for mms campaign
[**mms_campaigns_send_post**](MmsCampaignApi.md#mms_campaigns_send_post) | **POST** /mms-campaigns/send | Create mms campaign


# **mms_campaign_by_mms_campaign_id_get**
> str mms_campaign_by_mms_campaign_id_get(mms_campaign_id)

Get specific mms campaign

Get specific mms campaign

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
mms_campaign_id = 56 # int | ID of MMS campaign to retrieve

try:
    # Get specific mms campaign
    api_response = api_instance.mms_campaign_by_mms_campaign_id_get(mms_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaign_by_mms_campaign_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mms_campaign_id** | **int**| ID of MMS campaign to retrieve | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mms_campaigns_by_mms_campaign_id_put**
> str mms_campaigns_by_mms_campaign_id_put(mms_campaign_id, campaign)

Update mms campaign

Update mms campaign

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
mms_campaign_id = 56 # int | ID of MMS campaign to update
campaign = clicksend_client.MmsCampaign() # MmsCampaign | MmsCampaign model

try:
    # Update mms campaign
    api_response = api_instance.mms_campaigns_by_mms_campaign_id_put(mms_campaign_id, campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaigns_by_mms_campaign_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mms_campaign_id** | **int**| ID of MMS campaign to update | 
 **campaign** | [**MmsCampaign**](MmsCampaign.md)| MmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mms_campaigns_cancel_by_mms_campaign_id_put**
> str mms_campaigns_cancel_by_mms_campaign_id_put(mms_campaign_id)

Cancel mms campaign

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
mms_campaign_id = 56 # int | ID of MMS Campaign to cancel

try:
    # Cancel mms campaign
    api_response = api_instance.mms_campaigns_cancel_by_mms_campaign_id_put(mms_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaigns_cancel_by_mms_campaign_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mms_campaign_id** | **int**| ID of MMS Campaign to cancel | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mms_campaigns_get**
> str mms_campaigns_get(page=page, limit=limit)

Get list of mms campaigns

Get list of mms campaigns

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get list of mms campaigns
    api_response = api_instance.mms_campaigns_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaigns_get: %s\n" % e)
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

# **mms_campaigns_price_post**
> str mms_campaigns_price_post(campaign)

Calculate price for mms campaign

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
campaign = clicksend_client.MmsCampaign() # MmsCampaign | MmsCampaign model

try:
    # Calculate price for mms campaign
    api_response = api_instance.mms_campaigns_price_post(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaigns_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**MmsCampaign**](MmsCampaign.md)| MmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mms_campaigns_send_post**
> str mms_campaigns_send_post(campaign)

Create mms campaign

Create mms campaign

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
api_instance = clicksend_client.MmsCampaignApi(clicksend_client.ApiClient(configuration))
campaign = clicksend_client.MmsCampaign() # MmsCampaign | MmsCampaign model

try:
    # Create mms campaign
    api_response = api_instance.mms_campaigns_send_post(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MmsCampaignApi->mms_campaigns_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**MmsCampaign**](MmsCampaign.md)| MmsCampaign model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

