# WebHookUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**WebHookConfigurationSecret**](WebHookConfigurationSecret.md) | The configuration of the web hook registration.                If the property secret is omitted or contains an empty string in a POST or PATCH request,  no signature hash will be calculated.                When retrieving web hook registration information from the service, the secret is always omitted | 
**active** | **bool** | A value indicating whether callbacks to the registered URL are made or not | 
**name** | **str** | The name of the object | 
**description** | **str** | The description of the object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


