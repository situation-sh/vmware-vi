# vmware_vi.VirtualMachineGuestCustomizationManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_guest_customization_manager_abort_customization_task**](VirtualMachineGuestCustomizationManagerApi.md#virtual_machine_guest_customization_manager_abort_customization_task) | **POST** /VirtualMachineGuestCustomizationManager/{moId}/AbortCustomization_Task | Abort any running guest customization process in the guest and remove the guest customization lock in the guest as well. 
[**virtual_machine_guest_customization_manager_customize_guest_task**](VirtualMachineGuestCustomizationManagerApi.md#virtual_machine_guest_customization_manager_customize_guest_task) | **POST** /VirtualMachineGuestCustomizationManager/{moId}/CustomizeGuest_Task | Customize a running virtual machine. 
[**virtual_machine_guest_customization_manager_start_guest_network_task**](VirtualMachineGuestCustomizationManagerApi.md#virtual_machine_guest_customization_manager_start_guest_network_task) | **POST** /VirtualMachineGuestCustomizationManager/{moId}/StartGuestNetwork_Task | Start the network service in the guest, e.g. 


# **virtual_machine_guest_customization_manager_abort_customization_task**
> ManagedObjectReference virtual_machine_guest_customization_manager_abort_customization_task(mo_id, abort_customization_request_type)

Abort any running guest customization process in the guest and remove the guest customization lock in the guest as well. 

Abort any running guest customization process in the guest and remove the guest customization lock in the guest as well.  As a result of the operation, the guest configuration may be left in an undefined state, which is however fine because guest customization is idempotent. A later successful guest customization can set the guest configuration to a valid state. The virtual machine must be in the powered-on state and the VMware Tools must be running. The VM is typically a cloned VM after the InstantClone operation. See *VirtualMachine.InstantClone_Task*.  ***Since:*** vSphere API 6.8.7  ***Required privileges:*** VirtualMachine.Provisioning.Customize 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.abort_customization_request_type import AbortCustomizationRequestType
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
    api_instance = vmware_vi.VirtualMachineGuestCustomizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    abort_customization_request_type = vmware_vi.AbortCustomizationRequestType() # AbortCustomizationRequestType | 

    try:
        # Abort any running guest customization process in the guest and remove the guest customization lock in the guest as well. 
        api_response = api_instance.virtual_machine_guest_customization_manager_abort_customization_task(mo_id, abort_customization_request_type)
        print("The response of VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_abort_customization_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_abort_customization_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **abort_customization_request_type** | [**AbortCustomizationRequestType**](AbortCustomizationRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the VMware Tools is not running.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestPermissionDenied***: if the provided guest authentication is not sufficient to perform the guest customization.  ***CustomizationFault***: if a customization error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_guest_customization_manager_customize_guest_task**
> ManagedObjectReference virtual_machine_guest_customization_manager_customize_guest_task(mo_id, customize_guest_request_type)

Customize a running virtual machine. 

Customize a running virtual machine.  The virtual machine must be in the powered-on state and the VMware Tools must be running. The VM is typically a cloned VM after the InstantClone operation. See *VirtualMachine.InstantClone_Task*.  ***Since:*** vSphere API 6.8.7  ***Required privileges:*** VirtualMachine.Provisioning.Customize 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customize_guest_request_type import CustomizeGuestRequestType
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
    api_instance = vmware_vi.VirtualMachineGuestCustomizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    customize_guest_request_type = vmware_vi.CustomizeGuestRequestType() # CustomizeGuestRequestType | 

    try:
        # Customize a running virtual machine. 
        api_response = api_instance.virtual_machine_guest_customization_manager_customize_guest_task(mo_id, customize_guest_request_type)
        print("The response of VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_customize_guest_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_customize_guest_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **customize_guest_request_type** | [**CustomizeGuestRequestType**](CustomizeGuestRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the VMware Tools is not running.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestPermissionDenied***: if the provided guest authentication is not sufficient to perform the guest customization.  ***CustomizationFault***: if a customization error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_guest_customization_manager_start_guest_network_task**
> ManagedObjectReference virtual_machine_guest_customization_manager_start_guest_network_task(mo_id, start_guest_network_request_type)

Start the network service in the guest, e.g. 

Start the network service in the guest, e.g.  acquire IPs from DHCP. The virtual machine must be in the powered-on state and the VMware Tools must be running. The VM is typically a cloned VM after the InstantClone operation. See *VirtualMachine.InstantClone_Task*.  ***Since:*** vSphere API 6.8.7  ***Required privileges:*** VirtualMachine.Provisioning.Customize 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.start_guest_network_request_type import StartGuestNetworkRequestType
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
    api_instance = vmware_vi.VirtualMachineGuestCustomizationManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    start_guest_network_request_type = vmware_vi.StartGuestNetworkRequestType() # StartGuestNetworkRequestType | 

    try:
        # Start the network service in the guest, e.g. 
        api_response = api_instance.virtual_machine_guest_customization_manager_start_guest_network_task(mo_id, start_guest_network_request_type)
        print("The response of VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_start_guest_network_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineGuestCustomizationManagerApi->virtual_machine_guest_customization_manager_start_guest_network_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **start_guest_network_request_type** | [**StartGuestNetworkRequestType**](StartGuestNetworkRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the VMware Tools is not running.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestPermissionDenied***: if the provided guest authentication is not sufficient to perform the guest customization.  ***CustomizationFault***: if a customization error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

