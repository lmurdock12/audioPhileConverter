# swagger_client.LanguageGenerationModelsApi

All URIs are relative to *https://southcentralus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_language_generation_model**](LanguageGenerationModelsApi.md#create_language_generation_model) | **POST** /api/languagegeneration/v2.0/Models | Creates a new language generation model.
[**delete_language_generation_model**](LanguageGenerationModelsApi.md#delete_language_generation_model) | **DELETE** /api/languagegeneration/v2.0/Models/{id} | Deletes the language generation model with the given id.
[**get_language_generation_model**](LanguageGenerationModelsApi.md#get_language_generation_model) | **GET** /api/languagegeneration/v2.0/Models/{id} | Gets the specified language generation model.
[**get_language_generation_models**](LanguageGenerationModelsApi.md#get_language_generation_models) | **GET** /api/languagegeneration/v2.0/Models | Gets all language generation model of a subscription.
[**get_supported_locales_for_language_generation_models**](LanguageGenerationModelsApi.md#get_supported_locales_for_language_generation_models) | **GET** /api/languagegeneration/v2.0/Models/locales | Gets a list of supported locales for language generation model creation.
[**update_language_generation_model**](LanguageGenerationModelsApi.md#update_language_generation_model) | **PATCH** /api/languagegeneration/v2.0/Models/{id} | Updates the mutable details of the language generation model identified by its id.


# **create_language_generation_model**
> create_language_generation_model(model_definition)

Creates a new language generation model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))
model_definition = swagger_client.ModelDefinition() # ModelDefinition | 

try:
    # Creates a new language generation model.
    api_instance.create_language_generation_model(model_definition)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->create_language_generation_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_definition** | [**ModelDefinition**](ModelDefinition.md)|  | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_language_generation_model**
> delete_language_generation_model(id)

Deletes the language generation model with the given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the language generation model.

try:
    # Deletes the language generation model with the given id.
    api_instance.delete_language_generation_model(id)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->delete_language_generation_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the language generation model. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_language_generation_model**
> Model get_language_generation_model(id)

Gets the specified language generation model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets the specified language generation model.
    api_response = api_instance.get_language_generation_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->get_language_generation_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_language_generation_models**
> list[Model] get_language_generation_models()

Gets all language generation model of a subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))

try:
    # Gets all language generation model of a subscription.
    api_response = api_instance.get_language_generation_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->get_language_generation_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model]**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_language_generation_models**
> list[str] get_supported_locales_for_language_generation_models()

Gets a list of supported locales for language generation model creation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for language generation model creation.
    api_response = api_instance.get_supported_locales_for_language_generation_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->get_supported_locales_for_language_generation_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_language_generation_model**
> Model update_language_generation_model(id, model_update)

Updates the mutable details of the language generation model identified by its id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LanguageGenerationModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The route parameter identifies the language generation model to change.
model_update = swagger_client.ModelUpdate() # ModelUpdate | The object contains the updated fields of the model.

try:
    # Updates the mutable details of the language generation model identified by its id.
    api_response = api_instance.update_language_generation_model(id, model_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationModelsApi->update_language_generation_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The route parameter identifies the language generation model to change. | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)| The object contains the updated fields of the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

