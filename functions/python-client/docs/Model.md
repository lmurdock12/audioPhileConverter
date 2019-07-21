# Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of this entity | 
**base_model** | [**Model**](Model.md) | The base model used for adaptation | [optional] 
**datasets** | [**list[Dataset]**](Dataset.md) | Datasets used for adaptation | [optional] 
**model_kind** | **str** | The kind of this model (e.g. acoustic, language ...) | 
**name** | **str** | The name of the object | 
**description** | **str** | The description of the object | [optional] 
**properties** | **dict(str, str)** | The custom properties of this entity | [optional] 
**locale** | **str** | The locale of the contained data | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created | 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered | 
**status** | **str** | The status of the object | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


