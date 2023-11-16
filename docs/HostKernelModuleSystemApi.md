# vmware_vi.HostKernelModuleSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_kernel_module_system_query_configured_module_option_string**](HostKernelModuleSystemApi.md#host_kernel_module_system_query_configured_module_option_string) | **POST** /HostKernelModuleSystem/{moId}/QueryConfiguredModuleOptionString | Query the options configured to be passed to the kernel module when loaded. 
[**host_kernel_module_system_query_modules**](HostKernelModuleSystemApi.md#host_kernel_module_system_query_modules) | **POST** /HostKernelModuleSystem/{moId}/QueryModules | Query the set of modules on the host. 
[**host_kernel_module_system_update_module_option_string**](HostKernelModuleSystemApi.md#host_kernel_module_system_update_module_option_string) | **POST** /HostKernelModuleSystem/{moId}/UpdateModuleOptionString | Specifies the options to be passed to the kernel module when loaded. 


# **host_kernel_module_system_query_configured_module_option_string**
> str host_kernel_module_system_query_configured_module_option_string(mo_id, query_configured_module_option_string_request_type)

Query the options configured to be passed to the kernel module when loaded. 

Query the options configured to be passed to the kernel module when loaded.  Note that this is not necessarily the option string currently in use by the kernel module.  ***Since:*** VI API 2.5u2  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_configured_module_option_string_request_type import QueryConfiguredModuleOptionStringRequestType
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
    api_instance = vmware_vi.HostKernelModuleSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_configured_module_option_string_request_type = vmware_vi.QueryConfiguredModuleOptionStringRequestType() # QueryConfiguredModuleOptionStringRequestType | 

    try:
        # Query the options configured to be passed to the kernel module when loaded. 
        api_response = api_instance.host_kernel_module_system_query_configured_module_option_string(mo_id, query_configured_module_option_string_request_type)
        print("The response of HostKernelModuleSystemApi->host_kernel_module_system_query_configured_module_option_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostKernelModuleSystemApi->host_kernel_module_system_query_configured_module_option_string: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_configured_module_option_string_request_type** | [**QueryConfiguredModuleOptionStringRequestType**](QueryConfiguredModuleOptionStringRequestType.md)|  | 

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
**200** | Option string to be passed to the kernel module at load time.  |  -  |
**500** | ***NotFound***: if the kernel module does not exist on the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_kernel_module_system_query_modules**
> List[KernelModuleInfo] host_kernel_module_system_query_modules(mo_id)

Query the set of modules on the host. 

Query the set of modules on the host.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.kernel_module_info import KernelModuleInfo
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
    api_instance = vmware_vi.HostKernelModuleSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Query the set of modules on the host. 
        api_response = api_instance.host_kernel_module_system_query_modules(mo_id)
        print("The response of HostKernelModuleSystemApi->host_kernel_module_system_query_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostKernelModuleSystemApi->host_kernel_module_system_query_modules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[KernelModuleInfo]**](KernelModuleInfo.md)

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

# **host_kernel_module_system_update_module_option_string**
> host_kernel_module_system_update_module_option_string(mo_id, update_module_option_string_request_type)

Specifies the options to be passed to the kernel module when loaded. 

Specifies the options to be passed to the kernel module when loaded.  ***Since:*** VI API 2.5u2  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_module_option_string_request_type import UpdateModuleOptionStringRequestType
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
    api_instance = vmware_vi.HostKernelModuleSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_module_option_string_request_type = vmware_vi.UpdateModuleOptionStringRequestType() # UpdateModuleOptionStringRequestType | 

    try:
        # Specifies the options to be passed to the kernel module when loaded. 
        api_instance.host_kernel_module_system_update_module_option_string(mo_id, update_module_option_string_request_type)
    except Exception as e:
        print("Exception when calling HostKernelModuleSystemApi->host_kernel_module_system_update_module_option_string: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_module_option_string_request_type** | [**UpdateModuleOptionStringRequestType**](UpdateModuleOptionStringRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the kernel module does not exist on the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

