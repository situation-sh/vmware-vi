# vmware_vi.VirtualMachineCompatibilityCheckerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_compatibility_checker_check_compatibility_task**](VirtualMachineCompatibilityCheckerApi.md#virtual_machine_compatibility_checker_check_compatibility_task) | **POST** /VirtualMachineCompatibilityChecker/{moId}/CheckCompatibility_Task | Tests whether or not a virtual machine could be placed on the given host in the given resource pool. 
[**virtual_machine_compatibility_checker_check_power_on_task**](VirtualMachineCompatibilityCheckerApi.md#virtual_machine_compatibility_checker_check_power_on_task) | **POST** /VirtualMachineCompatibilityChecker/{moId}/CheckPowerOn_Task | Tests whether the provided virtual machine can be powered on on the given host and/or resource pool. 
[**virtual_machine_compatibility_checker_check_vm_config_task**](VirtualMachineCompatibilityCheckerApi.md#virtual_machine_compatibility_checker_check_vm_config_task) | **POST** /VirtualMachineCompatibilityChecker/{moId}/CheckVmConfig_Task | Tests whether the provided virtual machine specification can be applied on the given host and resource pool. 


# **virtual_machine_compatibility_checker_check_compatibility_task**
> ManagedObjectReference virtual_machine_compatibility_checker_check_compatibility_task(mo_id, check_compatibility_request_type)

Tests whether or not a virtual machine could be placed on the given host in the given resource pool. 

Tests whether or not a virtual machine could be placed on the given host in the given resource pool.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_compatibility_request_type import CheckCompatibilityRequestType
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
    api_instance = vmware_vi.VirtualMachineCompatibilityCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_compatibility_request_type = vmware_vi.CheckCompatibilityRequestType() # CheckCompatibilityRequestType | 

    try:
        # Tests whether or not a virtual machine could be placed on the given host in the given resource pool. 
        api_response = api_instance.virtual_machine_compatibility_checker_check_compatibility_task(mo_id, check_compatibility_request_type)
        print("The response of VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_compatibility_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_compatibility_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_compatibility_request_type** | [**CheckCompatibilityRequestType**](CheckCompatibilityRequestType.md)|  | 

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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: if the operation cannot be performed because of the host or virtual machine&#39;s current state. For example, if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available.  ***InvalidArgument***: if the desired host and pool are not associated with the same compute resource, the host parameter is left unset when the specified pool is associated with a non-DRS cluster, or if the specified vm does not exist.  ***DatacenterMismatch***: if the provided host and pool do not belong to the same datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_compatibility_checker_check_power_on_task**
> ManagedObjectReference virtual_machine_compatibility_checker_check_power_on_task(mo_id, check_power_on_request_type)

Tests whether the provided virtual machine can be powered on on the given host and/or resource pool. 

Tests whether the provided virtual machine can be powered on on the given host and/or resource pool.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_power_on_request_type import CheckPowerOnRequestType
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
    api_instance = vmware_vi.VirtualMachineCompatibilityCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_power_on_request_type = vmware_vi.CheckPowerOnRequestType() # CheckPowerOnRequestType | 

    try:
        # Tests whether the provided virtual machine can be powered on on the given host and/or resource pool. 
        api_response = api_instance.virtual_machine_compatibility_checker_check_power_on_task(mo_id, check_power_on_request_type)
        print("The response of VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_power_on_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_power_on_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_power_on_request_type** | [**CheckPowerOnRequestType**](CheckPowerOnRequestType.md)|  | 

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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if the desired host and pool are not associated with the same compute resource, the host parameter is left unset when the specified pool is associated with a non-DRS cluster, or if the provided vm does not exist.  ***DatacenterMismatch***: if the provided host and pool do not belong to the same datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_compatibility_checker_check_vm_config_task**
> ManagedObjectReference virtual_machine_compatibility_checker_check_vm_config_task(mo_id, check_vm_config_request_type)

Tests whether the provided virtual machine specification can be applied on the given host and resource pool. 

Tests whether the provided virtual machine specification can be applied on the given host and resource pool.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_vm_config_request_type import CheckVmConfigRequestType
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
    api_instance = vmware_vi.VirtualMachineCompatibilityCheckerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_vm_config_request_type = vmware_vi.CheckVmConfigRequestType() # CheckVmConfigRequestType | 

    try:
        # Tests whether the provided virtual machine specification can be applied on the given host and resource pool. 
        api_response = api_instance.virtual_machine_compatibility_checker_check_vm_config_task(mo_id, check_vm_config_request_type)
        print("The response of VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_vm_config_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineCompatibilityCheckerApi->virtual_machine_compatibility_checker_check_vm_config_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_vm_config_request_type** | [**CheckVmConfigRequestType**](CheckVmConfigRequestType.md)|  | 

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
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if the desired host and pool are not associated with the same compute resource, the host parameter is left unset when the specified pool is associated with a non-DRS cluster, or if the provided vm does not exist.  ***DatacenterMismatch***: if the provided host and pool do not belong to the same datacenter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

