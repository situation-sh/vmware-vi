# vmware_vi.HostAssignableHardwareManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_assignable_hardware_manager_download_description_tree**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_download_description_tree) | **POST** /HostAssignableHardwareManager/{moId}/DownloadDescriptionTree | Download Assignable Hardware description tree. 
[**host_assignable_hardware_manager_get_binding**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_get_binding) | **GET** /HostAssignableHardwareManager/{moId}/binding | Assignable Hardware bindings 
[**host_assignable_hardware_manager_get_config**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_get_config) | **GET** /HostAssignableHardwareManager/{moId}/config | Assignable Hardware configuration 
[**host_assignable_hardware_manager_retrieve_dynamic_passthrough_info**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_retrieve_dynamic_passthrough_info) | **POST** /HostAssignableHardwareManager/{moId}/RetrieveDynamicPassthroughInfo | Retrieve PCI Dynamic Passthrough info. 
[**host_assignable_hardware_manager_retrieve_vendor_device_group_info**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_retrieve_vendor_device_group_info) | **POST** /HostAssignableHardwareManager/{moId}/RetrieveVendorDeviceGroupInfo | Retrieve VendorDeviceGroup info. 
[**host_assignable_hardware_manager_update_assignable_hardware_config**](HostAssignableHardwareManagerApi.md#host_assignable_hardware_manager_update_assignable_hardware_config) | **POST** /HostAssignableHardwareManager/{moId}/UpdateAssignableHardwareConfig | Update Assignable Hardware configuration. 


# **host_assignable_hardware_manager_download_description_tree**
> bytearray host_assignable_hardware_manager_download_description_tree(mo_id)

Download Assignable Hardware description tree. 

Download Assignable Hardware description tree.  The size of the downloaded description tree is dependent on the type and number of assignable devices found on the host. As a rough estimate, each device might require approximate 256 bytes to represent. The number of assignable devices on a host may vary from none to 60 or more. A host with 3 SRIOV type devices consisting of a PF and 16 VFs would have a total of 51 devices and the description tree would be approximately 51 \\* 256 bytes = 13,056 bytes.  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Download Assignable Hardware description tree. 
        api_response = api_instance.host_assignable_hardware_manager_download_description_tree(mo_id)
        print("The response of HostAssignableHardwareManagerApi->host_assignable_hardware_manager_download_description_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_download_description_tree: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**bytearray**

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

# **host_assignable_hardware_manager_get_binding**
> List[HostAssignableHardwareBinding] host_assignable_hardware_manager_get_binding(mo_id)

Assignable Hardware bindings 

Assignable Hardware bindings  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_assignable_hardware_binding import HostAssignableHardwareBinding
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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Assignable Hardware bindings 
        api_response = api_instance.host_assignable_hardware_manager_get_binding(mo_id)
        print("The response of HostAssignableHardwareManagerApi->host_assignable_hardware_manager_get_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_get_binding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostAssignableHardwareBinding]**](HostAssignableHardwareBinding.md)

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

# **host_assignable_hardware_manager_get_config**
> HostAssignableHardwareConfig host_assignable_hardware_manager_get_config(mo_id)

Assignable Hardware configuration 

Assignable Hardware configuration  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_assignable_hardware_config import HostAssignableHardwareConfig
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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Assignable Hardware configuration 
        api_response = api_instance.host_assignable_hardware_manager_get_config(mo_id)
        print("The response of HostAssignableHardwareManagerApi->host_assignable_hardware_manager_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostAssignableHardwareConfig**](HostAssignableHardwareConfig.md)

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

# **host_assignable_hardware_manager_retrieve_dynamic_passthrough_info**
> List[VirtualMachineDynamicPassthroughInfo] host_assignable_hardware_manager_retrieve_dynamic_passthrough_info(mo_id)

Retrieve PCI Dynamic Passthrough info. 

Retrieve PCI Dynamic Passthrough info.  Returns the list of PCI devices that may be used as a Dynamic DirectPath IO device.  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_dynamic_passthrough_info import VirtualMachineDynamicPassthroughInfo
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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieve PCI Dynamic Passthrough info. 
        api_response = api_instance.host_assignable_hardware_manager_retrieve_dynamic_passthrough_info(mo_id)
        print("The response of HostAssignableHardwareManagerApi->host_assignable_hardware_manager_retrieve_dynamic_passthrough_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_retrieve_dynamic_passthrough_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VirtualMachineDynamicPassthroughInfo]**](VirtualMachineDynamicPassthroughInfo.md)

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

# **host_assignable_hardware_manager_retrieve_vendor_device_group_info**
> List[VirtualMachineVendorDeviceGroupInfo] host_assignable_hardware_manager_retrieve_vendor_device_group_info(mo_id)

Retrieve VendorDeviceGroup info. 

Retrieve VendorDeviceGroup info.  Returns the list of Vendor Device Group deviceTypes present.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_vendor_device_group_info import VirtualMachineVendorDeviceGroupInfo
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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieve VendorDeviceGroup info. 
        api_response = api_instance.host_assignable_hardware_manager_retrieve_vendor_device_group_info(mo_id)
        print("The response of HostAssignableHardwareManagerApi->host_assignable_hardware_manager_retrieve_vendor_device_group_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_retrieve_vendor_device_group_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VirtualMachineVendorDeviceGroupInfo]**](VirtualMachineVendorDeviceGroupInfo.md)

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

# **host_assignable_hardware_manager_update_assignable_hardware_config**
> host_assignable_hardware_manager_update_assignable_hardware_config(mo_id, update_assignable_hardware_config_request_type)

Update Assignable Hardware configuration. 

Update Assignable Hardware configuration.  Entries are updated as described in *HostAssignableHardwareConfig*.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_assignable_hardware_config_request_type import UpdateAssignableHardwareConfigRequestType
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
    api_instance = vmware_vi.HostAssignableHardwareManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_assignable_hardware_config_request_type = vmware_vi.UpdateAssignableHardwareConfigRequestType() # UpdateAssignableHardwareConfigRequestType | 

    try:
        # Update Assignable Hardware configuration. 
        api_instance.host_assignable_hardware_manager_update_assignable_hardware_config(mo_id, update_assignable_hardware_config_request_type)
    except Exception as e:
        print("Exception when calling HostAssignableHardwareManagerApi->host_assignable_hardware_manager_update_assignable_hardware_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_assignable_hardware_config_request_type** | [**UpdateAssignableHardwareConfigRequestType**](UpdateAssignableHardwareConfigRequestType.md)|  | 

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
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

