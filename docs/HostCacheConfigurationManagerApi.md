# vmware_vi.HostCacheConfigurationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_cache_configuration_manager_configure_host_cache_task**](HostCacheConfigurationManagerApi.md#host_cache_configuration_manager_configure_host_cache_task) | **POST** /HostCacheConfigurationManager/{moId}/ConfigureHostCache_Task | Configure host cache/swap performance enhancement. 
[**host_cache_configuration_manager_get_cache_configuration_info**](HostCacheConfigurationManagerApi.md#host_cache_configuration_manager_get_cache_configuration_info) | **GET** /HostCacheConfigurationManager/{moId}/cacheConfigurationInfo | The swap performance configuration for the ESX host. 


# **host_cache_configuration_manager_configure_host_cache_task**
> ManagedObjectReference host_cache_configuration_manager_configure_host_cache_task(mo_id, configure_host_cache_request_type)

Configure host cache/swap performance enhancement. 

Configure host cache/swap performance enhancement.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.AdvancedConfig 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_host_cache_request_type import ConfigureHostCacheRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
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
    api_instance = vmware_vi.HostCacheConfigurationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_host_cache_request_type = vmware_vi.ConfigureHostCacheRequestType() # ConfigureHostCacheRequestType | 

    try:
        # Configure host cache/swap performance enhancement. 
        api_response = api_instance.host_cache_configuration_manager_configure_host_cache_task(mo_id, configure_host_cache_request_type)
        print("The response of HostCacheConfigurationManagerApi->host_cache_configuration_manager_configure_host_cache_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCacheConfigurationManagerApi->host_cache_configuration_manager_configure_host_cache_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_host_cache_request_type** | [**ConfigureHostCacheRequestType**](ConfigureHostCacheRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_cache_configuration_manager_get_cache_configuration_info**
> List[HostCacheConfigurationInfo] host_cache_configuration_manager_get_cache_configuration_info(mo_id)

The swap performance configuration for the ESX host. 

The swap performance configuration for the ESX host.  This includes configuration information for each datastore enabled for this purpose.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.AdvancedConfig 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_cache_configuration_info import HostCacheConfigurationInfo
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
    api_instance = vmware_vi.HostCacheConfigurationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The swap performance configuration for the ESX host. 
        api_response = api_instance.host_cache_configuration_manager_get_cache_configuration_info(mo_id)
        print("The response of HostCacheConfigurationManagerApi->host_cache_configuration_manager_get_cache_configuration_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostCacheConfigurationManagerApi->host_cache_configuration_manager_get_cache_configuration_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostCacheConfigurationInfo]**](HostCacheConfigurationInfo.md)

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

