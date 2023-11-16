# vmware_vi.HostBootDeviceSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_boot_device_system_query_boot_devices**](HostBootDeviceSystemApi.md#host_boot_device_system_query_boot_devices) | **POST** /HostBootDeviceSystem/{moId}/QueryBootDevices | Retrieves a list of the available boot devices for the host system. 
[**host_boot_device_system_update_boot_device**](HostBootDeviceSystemApi.md#host_boot_device_system_update_boot_device) | **POST** /HostBootDeviceSystem/{moId}/UpdateBootDevice | Sets the current boot device for the host system. 


# **host_boot_device_system_query_boot_devices**
> HostBootDeviceInfo host_boot_device_system_query_boot_devices(mo_id)

Retrieves a list of the available boot devices for the host system. 

Retrieves a list of the available boot devices for the host system.  ***Since:*** VI API 2.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_boot_device_info import HostBootDeviceInfo
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
    api_instance = vmware_vi.HostBootDeviceSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Retrieves a list of the available boot devices for the host system. 
        api_response = api_instance.host_boot_device_system_query_boot_devices(mo_id)
        print("The response of HostBootDeviceSystemApi->host_boot_device_system_query_boot_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostBootDeviceSystemApi->host_boot_device_system_query_boot_devices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostBootDeviceInfo**](HostBootDeviceInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The boot device information for the host. The returned object has a list of *HostBootDevice* data objects; each boot device object defines a description and a key to identify the device. The order of devices in the list is unpredictable. The returned *HostBootDeviceInfo* data object also contains the key of the current boot device.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_boot_device_system_update_boot_device**
> host_boot_device_system_update_boot_device(mo_id, update_boot_device_request_type)

Sets the current boot device for the host system. 

Sets the current boot device for the host system.  ***Since:*** VI API 2.5  ***Required privileges:*** Host.Config.Maintenance 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_boot_device_request_type import UpdateBootDeviceRequestType
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
    api_instance = vmware_vi.HostBootDeviceSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_boot_device_request_type = vmware_vi.UpdateBootDeviceRequestType() # UpdateBootDeviceRequestType | 

    try:
        # Sets the current boot device for the host system. 
        api_instance.host_boot_device_system_update_boot_device(mo_id, update_boot_device_request_type)
    except Exception as e:
        print("Exception when calling HostBootDeviceSystemApi->host_boot_device_system_update_boot_device: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_boot_device_request_type** | [**UpdateBootDeviceRequestType**](UpdateBootDeviceRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

