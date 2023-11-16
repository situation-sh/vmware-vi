# vmware_vi.SimpleCommandApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simple_command_execute_simple_command**](SimpleCommandApi.md#simple_command_execute_simple_command) | **POST** /SimpleCommand/{moId}/ExecuteSimpleCommand | The single function execution point for this simple command. 
[**simple_command_get_encoding_type**](SimpleCommandApi.md#simple_command_get_encoding_type) | **GET** /SimpleCommand/{moId}/encodingType | The encoding type used in the result. 
[**simple_command_get_entity**](SimpleCommandApi.md#simple_command_get_entity) | **GET** /SimpleCommand/{moId}/entity | A description of the service. 


# **simple_command_execute_simple_command**
> str simple_command_execute_simple_command(mo_id, execute_simple_command_request_type)

The single function execution point for this simple command. 

The single function execution point for this simple command.  The actual effects of this command depend upon the service handler registered for this instance.  ***Since:*** VI API 2.5  ***Required privileges:*** Global.ServiceManagers 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.execute_simple_command_request_type import ExecuteSimpleCommandRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.SimpleCommandApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    execute_simple_command_request_type = vmware_vi.ExecuteSimpleCommandRequestType() # ExecuteSimpleCommandRequestType | 

    try:
        # The single function execution point for this simple command. 
        api_response = api_instance.simple_command_execute_simple_command(mo_id, execute_simple_command_request_type)
        print("The response of SimpleCommandApi->simple_command_execute_simple_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleCommandApi->simple_command_execute_simple_command: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **execute_simple_command_request_type** | [**ExecuteSimpleCommandRequestType**](ExecuteSimpleCommandRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simple_command_get_encoding_type**
> SimpleCommandEncodingEnum simple_command_get_encoding_type(mo_id)

The encoding type used in the result. 

The encoding type used in the result.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.simple_command_encoding_enum import SimpleCommandEncodingEnum
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.SimpleCommandApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The encoding type used in the result. 
        api_response = api_instance.simple_command_get_encoding_type(mo_id)
        print("The response of SimpleCommandApi->simple_command_get_encoding_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleCommandApi->simple_command_get_encoding_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**SimpleCommandEncodingEnum**](SimpleCommandEncodingEnum.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simple_command_get_entity**
> ServiceManagerServiceInfo simple_command_get_entity(mo_id)

A description of the service. 

A description of the service.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.service_manager_service_info import ServiceManagerServiceInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.SimpleCommandApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A description of the service. 
        api_response = api_instance.simple_command_get_entity(mo_id)
        print("The response of SimpleCommandApi->simple_command_get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimpleCommandApi->simple_command_get_entity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ServiceManagerServiceInfo**](ServiceManagerServiceInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

