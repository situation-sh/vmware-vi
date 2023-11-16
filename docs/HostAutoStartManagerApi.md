# vmware_vi.HostAutoStartManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_auto_start_manager_auto_start_power_off**](HostAutoStartManagerApi.md#host_auto_start_manager_auto_start_power_off) | **POST** /HostAutoStartManager/{moId}/AutoStartPowerOff | Powers-off virtual machines according to the current AutoStart configuration. 
[**host_auto_start_manager_auto_start_power_on**](HostAutoStartManagerApi.md#host_auto_start_manager_auto_start_power_on) | **POST** /HostAutoStartManager/{moId}/AutoStartPowerOn | Powers-on virtual machines according to the current AutoStart configuration. 
[**host_auto_start_manager_get_config**](HostAutoStartManagerApi.md#host_auto_start_manager_get_config) | **GET** /HostAutoStartManager/{moId}/config | 
[**host_auto_start_manager_reconfigure_autostart**](HostAutoStartManagerApi.md#host_auto_start_manager_reconfigure_autostart) | **POST** /HostAutoStartManager/{moId}/ReconfigureAutostart | Changes the power-on or power-off sequence and system defaults. 


# **host_auto_start_manager_auto_start_power_off**
> host_auto_start_manager_auto_start_power_off(mo_id)

Powers-off virtual machines according to the current AutoStart configuration. 

Powers-off virtual machines according to the current AutoStart configuration.  See the description of the (@link vim.host.AutoStartManager.AutoPowerInfo) data object type for more information on Auto power-off behavior.  ***Required privileges:*** Host.Config.AutoStart 

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
    api_instance = vmware_vi.HostAutoStartManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Powers-off virtual machines according to the current AutoStart configuration. 
        api_instance.host_auto_start_manager_auto_start_power_off(mo_id)
    except Exception as e:
        print("Exception when calling HostAutoStartManagerApi->host_auto_start_manager_auto_start_power_off: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_auto_start_manager_auto_start_power_on**
> host_auto_start_manager_auto_start_power_on(mo_id)

Powers-on virtual machines according to the current AutoStart configuration. 

Powers-on virtual machines according to the current AutoStart configuration.  See the description of the (@link vim.host.AutoStartManager.AutoPowerInfo) data object type for more information on Auto power-on behavior.  ***Required privileges:*** Host.Config.AutoStart 

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
    api_instance = vmware_vi.HostAutoStartManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Powers-on virtual machines according to the current AutoStart configuration. 
        api_instance.host_auto_start_manager_auto_start_power_on(mo_id)
    except Exception as e:
        print("Exception when calling HostAutoStartManagerApi->host_auto_start_manager_auto_start_power_on: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_auto_start_manager_get_config**
> HostAutoStartManagerConfig host_auto_start_manager_get_config(mo_id)



### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_auto_start_manager_config import HostAutoStartManagerConfig
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
    api_instance = vmware_vi.HostAutoStartManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        api_response = api_instance.host_auto_start_manager_get_config(mo_id)
        print("The response of HostAutoStartManagerApi->host_auto_start_manager_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostAutoStartManagerApi->host_auto_start_manager_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostAutoStartManagerConfig**](HostAutoStartManagerConfig.md)

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

# **host_auto_start_manager_reconfigure_autostart**
> host_auto_start_manager_reconfigure_autostart(mo_id, reconfigure_autostart_request_type)

Changes the power-on or power-off sequence and system defaults. 

Changes the power-on or power-off sequence and system defaults.  The specification is an incremental change to the current configuration.  If systemDefaults are included, only values that are specified in the specification are changed.  For the spec.powerInfo array, each element is interpreted as an incremental change and the changes are processed sequentially. It is not an error to remove a non-existing virtual machine. If both startAction and stopAction are set to none, then the virtual machine is removed from the configuration.  A virtual machine's position in the order can be changed either by assigning the virtual machine a different position in the order or removing the machine from the order. When a virtual machine's position changes, all other virtual machines' positions may be affected as they move to new positions relative to each other.  ***Required privileges:*** Host.Config.AutoStart 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.reconfigure_autostart_request_type import ReconfigureAutostartRequestType
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
    api_instance = vmware_vi.HostAutoStartManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfigure_autostart_request_type = vmware_vi.ReconfigureAutostartRequestType() # ReconfigureAutostartRequestType | 

    try:
        # Changes the power-on or power-off sequence and system defaults. 
        api_instance.host_auto_start_manager_reconfigure_autostart(mo_id, reconfigure_autostart_request_type)
    except Exception as e:
        print("Exception when calling HostAutoStartManagerApi->host_auto_start_manager_reconfigure_autostart: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfigure_autostart_request_type** | [**ReconfigureAutostartRequestType**](ReconfigureAutostartRequestType.md)|  | 

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

