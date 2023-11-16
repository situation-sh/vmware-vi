# vmware_vi.HostPowerSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_power_system_configure_power_policy**](HostPowerSystemApi.md#host_power_system_configure_power_policy) | **POST** /HostPowerSystem/{moId}/ConfigurePowerPolicy | Configure host power policy. 
[**host_power_system_get_capability**](HostPowerSystemApi.md#host_power_system_get_capability) | **GET** /HostPowerSystem/{moId}/capability | Power system capabilities object. 
[**host_power_system_get_info**](HostPowerSystemApi.md#host_power_system_get_info) | **GET** /HostPowerSystem/{moId}/info | Power system state info object. 


# **host_power_system_configure_power_policy**
> host_power_system_configure_power_policy(mo_id, configure_power_policy_request_type)

Configure host power policy. 

Configure host power policy.  ***Since:*** vSphere API 4.1  ***Required privileges:*** Host.Config.Power 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.configure_power_policy_request_type import ConfigurePowerPolicyRequestType
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
    api_instance = vmware_vi.HostPowerSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    configure_power_policy_request_type = vmware_vi.ConfigurePowerPolicyRequestType() # ConfigurePowerPolicyRequestType | 

    try:
        # Configure host power policy. 
        api_instance.host_power_system_configure_power_policy(mo_id, configure_power_policy_request_type)
    except Exception as e:
        print("Exception when calling HostPowerSystemApi->host_power_system_configure_power_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **configure_power_policy_request_type** | [**ConfigurePowerPolicyRequestType**](ConfigurePowerPolicyRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if an invalid power policy key is provided.  ***HostConfigFault***: for any other failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_power_system_get_capability**
> PowerSystemCapability host_power_system_get_capability(mo_id)

Power system capabilities object. 

Power system capabilities object.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.power_system_capability import PowerSystemCapability
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
    api_instance = vmware_vi.HostPowerSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Power system capabilities object. 
        api_response = api_instance.host_power_system_get_capability(mo_id)
        print("The response of HostPowerSystemApi->host_power_system_get_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPowerSystemApi->host_power_system_get_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**PowerSystemCapability**](PowerSystemCapability.md)

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

# **host_power_system_get_info**
> PowerSystemInfo host_power_system_get_info(mo_id)

Power system state info object. 

Power system state info object.  ***Since:*** vSphere API 4.1  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.power_system_info import PowerSystemInfo
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
    api_instance = vmware_vi.HostPowerSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Power system state info object. 
        api_response = api_instance.host_power_system_get_info(mo_id)
        print("The response of HostPowerSystemApi->host_power_system_get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostPowerSystemApi->host_power_system_get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**PowerSystemInfo**](PowerSystemInfo.md)

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

