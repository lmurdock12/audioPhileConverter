# swagger_client.LanguageGenerationEndpointsApi

All URIs are relative to *https://southcentralus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_language_generation_endpoint**](LanguageGenerationEndpointsApi.md#create_language_generation_endpoint) | **POST** /api/languagegeneration/v2.0/Endpoints | Creates a new language generation endpoint.
[**delete_language_generation_endpoint**](LanguageGenerationEndpointsApi.md#delete_language_generation_endpoint) | **DELETE** /api/languagegeneration/v2.0/Endpoints/{id} | Deletes the language generation model endpoint with the given id.
[**get_language_generation_endpoint**](LanguageGenerationEndpointsApi.md#get_language_generation_endpoint) | **GET** /api/languagegeneration/v2.0/Endpoints/{id} | Gets the specified deployed language generation endpoint.
[**get_language_generation_endpoints**](LanguageGenerationEndpointsApi.md#get_language_generation_endpoints) | **GET** /api/languagegeneration/v2.0/Endpoints | Gets all language generation endpoint of a subscription.
[**get_supported_locales_for_language_generation_endpoints**](LanguageGenerationEndpointsApi.md#get_supported_locales_for_language_generation_endpoints) | **GET** /api/languagegeneration/v2.0/Endpoints/locales | Gets a list of supported locales for language generation endpoint creation.
[**update_language_generation_endpoint**](LanguageGenerationEndpointsApi.md#update_language_generation_endpoint) | **PATCH** /api/languagegeneration/v2.0/Endpoints/{id} | Updates the mutable details of the language generation endpoint identified by its id.


# **create_language_generation_endpoint**
> create_language_generation_endpoint(endpoint_definition)

Creates a new language generation endpoint.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_definition = swagger_client.EndpointDefinition() # EndpointDefinition | 

try:
    # Creates a new language generation endpoint.
    api_instance.create_language_generation_endpoint(endpoint_definition)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->create_language_generation_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_definition** | [**EndpointDefinition**](EndpointDefinition.md)|  | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_language_generation_endpoint**
> delete_language_generation_endpoint(id)

Deletes the language generation model endpoint with the given id.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the language generation model endpoint.

try:
    # Deletes the language generation model endpoint with the given id.
    api_instance.delete_language_generation_endpoint(id)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->delete_language_generation_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the language generation model endpoint. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_language_generation_endpoint**
> Endpoint get_language_generation_endpoint(id)

Gets the specified deployed language generation endpoint.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets the specified deployed language generation endpoint.
    api_response = api_instance.get_language_generation_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->get_language_generation_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_language_generation_endpoints**
> list[Endpoint] get_language_generation_endpoints()

Gets all language generation endpoint of a subscription.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Gets all language generation endpoint of a subscription.
    api_response = api_instance.get_language_generation_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->get_language_generation_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Endpoint]**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_language_generation_endpoints**
> list[str] get_supported_locales_for_language_generation_endpoints()

Gets a list of supported locales for language generation endpoint creation.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for language generation endpoint creation.
    api_response = api_instance.get_supported_locales_for_language_generation_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->get_supported_locales_for_language_generation_endpoints: %s\n" % e)
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

# **update_language_generation_endpoint**
> Endpoint update_language_generation_endpoint(id, endpoint_update)

Updates the mutable details of the language generation endpoint identified by its id.

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
api_instance = swagger_client.LanguageGenerationEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the language generation model endpoint.
endpoint_update = swagger_client.EndpointMetadataUpdate() # EndpointMetadataUpdate | The object contains the updated fields of the endpoint.

try:
    # Updates the mutable details of the language generation endpoint identified by its id.
    api_response = api_instance.update_language_generation_endpoint(id, endpoint_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageGenerationEndpointsApi->update_language_generation_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the language generation model endpoint. | 
 **endpoint_update** | [**EndpointMetadataUpdate**](EndpointMetadataUpdate.md)| The object contains the updated fields of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

