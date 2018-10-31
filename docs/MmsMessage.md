# MmsMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Recipient phone number in E.164 format | 
**body** | **str** | Your message | 
**subject** | **str** | Subject line (max 20 characters) | 
**_from** | **str** | Your sender ID | [optional] 
**country** | **str** | Recipient country | [optional] 
**source** | **str** | Your method of sending | [optional] [default to 'sdk']
**list_id** | **int** | Your list ID if sending to a whole list (can be used instead of &#39;to&#39;) | [optional] 
**schedule** | **int** | Schedule time in unix format (leave blank for immediate delivery) | [optional] [default to 0]
**custom_string** | **str** | Custom string for your reference | [optional] 
**from_email** | **str** | Email to send replies to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


