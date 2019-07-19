# SmsMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | Your sender id - more info: http://help.clicksend.com/SMS/what-is-a-sender-id-or-sender-number. | [optional] 
**body** | **str** | Your message. | 
**to** | **str** | Recipient phone number in E.164 format. | [optional] 
**source** | **str** | Your method of sending e.g. &#39;wordpress&#39;, &#39;php&#39;, &#39;c#&#39;. | [optional] [default to 'sdk']
**schedule** | **int** | Leave blank for immediate delivery. Your schedule time in unix format http://help.clicksend.com/what-is-a-unix-timestamp | [optional] [default to 0]
**custom_string** | **str** | Your reference. Will be passed back with all replies and delivery reports. | [optional] 
**list_id** | **int** | Your list ID if sending to a whole list. Can be used instead of &#39;to&#39;. | [optional] 
**country** | **str** | Recipient country. | [optional] 
**from_email** | **str** | An email address where the reply should be emailed to. If omitted, the reply will be emailed back to the user who sent the outgoing SMS. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


