# vmware_vi.HostVFlashManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_v_flash_manager_configure_v_flash_resource_ex_task**](HostVFlashManagerApi.md#host_v_flash_manager_configure_v_flash_resource_ex_task) | **POST** /HostVFlashManager/{moId}/ConfigureVFlashResourceEx_Task | Configure vFlash resource on a list of SSD disks. 
[**host_v_flash_manager_get_v_flash_config_info**](HostVFlashManagerApi.md#host_v_flash_manager_get_v_flash_config_info) | **GET** /HostVFlashManager/{moId}/vFlashConfigInfo | Host vFlash configuration information. 
[**host_v_flash_manager_host_config_v_flash_cache**](HostVFlashManagerApi.md#host_v_flash_manager_host_config_v_flash_cache) | **POST** /HostVFlashManager/{moId}/HostConfigVFlashCache | Configure vFlash cache on the host. 
[**host_v_flash_manager_host_configure_v_flash_resource**](HostVFlashManagerApi.md#host_v_flash_manager_host_configure_v_flash_resource) | **POST** /HostVFlashManager/{moId}/HostConfigureVFlashResource | Configure vFlash resource on the host by attaching to a backend VFFS volume. 
[**host_v_flash_manager_host_get_v_flash_module_default_config**](HostVFlashManagerApi.md#host_v_flash_manager_host_get_v_flash_module_default_config) | **POST** /HostVFlashManager/{moId}/HostGetVFlashModuleDefaultConfig | Retrieve the default supported configuration for a given vFlash module 
[**host_v_flash_manager_host_remove_v_flash_resource**](HostVFlashManagerApi.md#host_v_flash_manager_host_remove_v_flash_resource) | **POST** /HostVFlashManager/{moId}/HostRemoveVFlashResource | Remove vFlash resource on the host by destroying the contained VFFS volume. 


# **host_v_flash_manager_configure_v_flash_resource_ex_task**
> ManagedObjectReference host_v_flash_manager_configure_v_flash_resource_ex_task(mo_id, configure_v_flash_resource_ex_request_type)

Configure vFlash resource on a list of SSD disks. 

Configure vFlash resource on a list of SSD disks.  If the host does not have a VFFS volume, host will format the volume first and then extend the volume on the rest of the SSDs; otherwise host will extend the existing VFFS volume on the passed SSDs. Finally host will configure the vFlash resource on the VFFS volume.  It will return *HostVFlashResourceConfigurationResult* describing success or failure associated with each device.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_v_flash_resource_ex_request_type import ConfigureVFlashResourceExRequestType
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_v_flash_resource_ex_request_type = vmware_vi.ConfigureVFlashResourceExRequestType() # ConfigureVFlashResourceExRequestType | 

    try:
        # Configure vFlash resource on a list of SSD disks. 
        api_response = api_instance.host_v_flash_manager_configure_v_flash_resource_ex_task(mo_id, configure_v_flash_resource_ex_request_type)
        print("The response of HostVFlashManagerApi->host_v_flash_manager_configure_v_flash_resource_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_configure_v_flash_resource_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_v_flash_resource_ex_request_type** | [**ConfigureVFlashResourceExRequestType**](ConfigureVFlashResourceExRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains *HostVFlashResourceConfigurationResult* describing success or failure associated with each device.  Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: if batch operation fails on the host. Because the returned VFlashResourceConfigurationResult contains the configuration success or fault for each device, as of vSphere API 5.x, we won&#39;t throw fault when batch operation fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_flash_manager_get_v_flash_config_info**
> HostVFlashManagerVFlashConfigInfo host_v_flash_manager_get_v_flash_config_info(mo_id)

Host vFlash configuration information. 

Host vFlash configuration information.  ***Since:*** vSphere API 5.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_flash_manager_v_flash_config_info import HostVFlashManagerVFlashConfigInfo
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Host vFlash configuration information. 
        api_response = api_instance.host_v_flash_manager_get_v_flash_config_info(mo_id)
        print("The response of HostVFlashManagerApi->host_v_flash_manager_get_v_flash_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_get_v_flash_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostVFlashManagerVFlashConfigInfo**](HostVFlashManagerVFlashConfigInfo.md)

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

# **host_v_flash_manager_host_config_v_flash_cache**
> host_v_flash_manager_host_config_v_flash_cache(mo_id, host_config_v_flash_cache_request_type)

Configure vFlash cache on the host. 

Configure vFlash cache on the host.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.AdvancedConfig 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_config_v_flash_cache_request_type import HostConfigVFlashCacheRequestType
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_config_v_flash_cache_request_type = vmware_vi.HostConfigVFlashCacheRequestType() # HostConfigVFlashCacheRequestType | 

    try:
        # Configure vFlash cache on the host. 
        api_instance.host_v_flash_manager_host_config_v_flash_cache(mo_id, host_config_v_flash_cache_request_type)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_host_config_v_flash_cache: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_config_v_flash_cache_request_type** | [**HostConfigVFlashCacheRequestType**](HostConfigVFlashCacheRequestType.md)|  | 

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
**500** | ***HostConfigFault***: If the swap cache cannot be configured on the host.  ***InaccessibleVFlashSource***: vFlash resource is not accessible.  ***ResourceInUse***: The contained VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_flash_manager_host_configure_v_flash_resource**
> host_v_flash_manager_host_configure_v_flash_resource(mo_id, host_configure_v_flash_resource_request_type)

Configure vFlash resource on the host by attaching to a backend VFFS volume. 

Configure vFlash resource on the host by attaching to a backend VFFS volume.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_configure_v_flash_resource_request_type import HostConfigureVFlashResourceRequestType
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_configure_v_flash_resource_request_type = vmware_vi.HostConfigureVFlashResourceRequestType() # HostConfigureVFlashResourceRequestType | 

    try:
        # Configure vFlash resource on the host by attaching to a backend VFFS volume. 
        api_instance.host_v_flash_manager_host_configure_v_flash_resource(mo_id, host_configure_v_flash_resource_request_type)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_host_configure_v_flash_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_configure_v_flash_resource_request_type** | [**HostConfigureVFlashResourceRequestType**](HostConfigureVFlashResourceRequestType.md)|  | 

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
**500** | ***HostConfigFault***: If vFlash resource cannot be configured on the host  ***ResourceInUse***: The contained VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_flash_manager_host_get_v_flash_module_default_config**
> VirtualDiskVFlashCacheConfigInfo host_v_flash_manager_host_get_v_flash_module_default_config(mo_id, host_get_v_flash_module_default_config_request_type)

Retrieve the default supported configuration for a given vFlash module 

Retrieve the default supported configuration for a given vFlash module  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.AdvancedConfig 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_get_v_flash_module_default_config_request_type import HostGetVFlashModuleDefaultConfigRequestType
from vmware_vi.models.virtual_disk_v_flash_cache_config_info import VirtualDiskVFlashCacheConfigInfo
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_get_v_flash_module_default_config_request_type = vmware_vi.HostGetVFlashModuleDefaultConfigRequestType() # HostGetVFlashModuleDefaultConfigRequestType | 

    try:
        # Retrieve the default supported configuration for a given vFlash module 
        api_response = api_instance.host_v_flash_manager_host_get_v_flash_module_default_config(mo_id, host_get_v_flash_module_default_config_request_type)
        print("The response of HostVFlashManagerApi->host_v_flash_manager_host_get_v_flash_module_default_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_host_get_v_flash_module_default_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_get_v_flash_module_default_config_request_type** | [**HostGetVFlashModuleDefaultConfigRequestType**](HostGetVFlashModuleDefaultConfigRequestType.md)|  | 

### Return type

[**VirtualDiskVFlashCacheConfigInfo**](VirtualDiskVFlashCacheConfigInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The supported default vFlash cache configuration  |  -  |
**500** | ***NotFound***: If vFlash resource is not configured or the contained VFFS volume cannot be found on the host.  ***HostConfigFault***: If the default vFlash module configuration option cannot be retrieved.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_flash_manager_host_remove_v_flash_resource**
> host_v_flash_manager_host_remove_v_flash_resource(mo_id)

Remove vFlash resource on the host by destroying the contained VFFS volume. 

Remove vFlash resource on the host by destroying the contained VFFS volume.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.HostVFlashManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Remove vFlash resource on the host by destroying the contained VFFS volume. 
        api_instance.host_v_flash_manager_host_remove_v_flash_resource(mo_id)
    except Exception as e:
        print("Exception when calling HostVFlashManagerApi->host_v_flash_manager_host_remove_v_flash_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: If vFlash resource is not configured or the contained VFFS volume cannot be found on the host.  ***HostConfigFault***: If vFlash resource or the contained VFFS volume cannot be removed from the host.  ***ResourceInUse***: The contained VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

