# vmware_vi.GuestProcessManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_process_manager_list_processes_in_guest**](GuestProcessManagerApi.md#guest_process_manager_list_processes_in_guest) | **POST** /GuestProcessManager/{moId}/ListProcessesInGuest | List the processes running in the guest operating system, plus those started by *GuestProcessManager.StartProgramInGuest* that have recently completed. 
[**guest_process_manager_read_environment_variable_in_guest**](GuestProcessManagerApi.md#guest_process_manager_read_environment_variable_in_guest) | **POST** /GuestProcessManager/{moId}/ReadEnvironmentVariableInGuest | Reads an environment variable from the guest OS 
[**guest_process_manager_start_program_in_guest**](GuestProcessManagerApi.md#guest_process_manager_start_program_in_guest) | **POST** /GuestProcessManager/{moId}/StartProgramInGuest | Starts a program in the guest operating system. 
[**guest_process_manager_terminate_process_in_guest**](GuestProcessManagerApi.md#guest_process_manager_terminate_process_in_guest) | **POST** /GuestProcessManager/{moId}/TerminateProcessInGuest | Terminates a process in the guest OS. 


# **guest_process_manager_list_processes_in_guest**
> List[GuestProcessInfo] guest_process_manager_list_processes_in_guest(mo_id, list_processes_in_guest_request_type)

List the processes running in the guest operating system, plus those started by *GuestProcessManager.StartProgramInGuest* that have recently completed. 

List the processes running in the guest operating system, plus those started by *GuestProcessManager.StartProgramInGuest* that have recently completed.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_process_info import GuestProcessInfo
from vmware_vi.models.list_processes_in_guest_request_type import ListProcessesInGuestRequestType
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
    api_instance = vmware_vi.GuestProcessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_processes_in_guest_request_type = vmware_vi.ListProcessesInGuestRequestType() # ListProcessesInGuestRequestType | 

    try:
        # List the processes running in the guest operating system, plus those started by *GuestProcessManager.StartProgramInGuest* that have recently completed. 
        api_response = api_instance.guest_process_manager_list_processes_in_guest(mo_id, list_processes_in_guest_request_type)
        print("The response of GuestProcessManagerApi->guest_process_manager_list_processes_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestProcessManagerApi->guest_process_manager_list_processes_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_processes_in_guest_request_type** | [**ListProcessesInGuestRequestType**](ListProcessesInGuestRequestType.md)|  | 

### Return type

[**List[GuestProcessInfo]**](GuestProcessInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list running processes is returned in an array of *GuestProcessInfo* structures.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_process_manager_read_environment_variable_in_guest**
> List[str] guest_process_manager_read_environment_variable_in_guest(mo_id, read_environment_variable_in_guest_request_type)

Reads an environment variable from the guest OS 

Reads an environment variable from the guest OS  If the authentication uses interactiveSession, then the environment being read will be that of the user logged into the desktop. Otherwise it's the environment of the user specified by the auth.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.read_environment_variable_in_guest_request_type import ReadEnvironmentVariableInGuestRequestType
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
    api_instance = vmware_vi.GuestProcessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    read_environment_variable_in_guest_request_type = vmware_vi.ReadEnvironmentVariableInGuestRequestType() # ReadEnvironmentVariableInGuestRequestType | 

    try:
        # Reads an environment variable from the guest OS 
        api_response = api_instance.guest_process_manager_read_environment_variable_in_guest(mo_id, read_environment_variable_in_guest_request_type)
        print("The response of GuestProcessManagerApi->guest_process_manager_read_environment_variable_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestProcessManagerApi->guest_process_manager_read_environment_variable_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **read_environment_variable_in_guest_request_type** | [**ReadEnvironmentVariableInGuestRequestType**](ReadEnvironmentVariableInGuestRequestType.md)|  | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A string array containing the value of the variables, or all environment variables if nothing is specified. The format of each string is \&quot;name&#x3D;value\&quot;. If any specified environment variable isn&#39;t set, then nothing is returned for that variable.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy. accepted by the guest OS.  ***GuestPermissionDenied***: if there are insufficient permissions in the guest OS.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_process_manager_start_program_in_guest**
> int guest_process_manager_start_program_in_guest(mo_id, start_program_in_guest_request_type)

Starts a program in the guest operating system. 

Starts a program in the guest operating system.  A process started this way can have its status queried with *GuestProcessManager.ListProcessesInGuest*. When the process completes, its exit code and end time will be available for 5 minutes after completion.  If VMware Tools is restarted, the exit code and end time will not be available.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.start_program_in_guest_request_type import StartProgramInGuestRequestType
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
    api_instance = vmware_vi.GuestProcessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    start_program_in_guest_request_type = vmware_vi.StartProgramInGuestRequestType() # StartProgramInGuestRequestType | 

    try:
        # Starts a program in the guest operating system. 
        api_response = api_instance.guest_process_manager_start_program_in_guest(mo_id, start_program_in_guest_request_type)
        print("The response of GuestProcessManagerApi->guest_process_manager_start_program_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestProcessManagerApi->guest_process_manager_start_program_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **start_program_in_guest_request_type** | [**StartProgramInGuestRequestType**](StartProgramInGuestRequestType.md)|  | 

### Return type

**int**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pid of the program started.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***FileNotFound***: if the program path does not exist.  ***FileFault***: if there is a file error in the guest operating system.  ***CannotAccessFile***: if the program path cannot be accessed.  ***GuestPermissionDenied***: if the program path cannot be run because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_process_manager_terminate_process_in_guest**
> guest_process_manager_terminate_process_in_guest(mo_id, terminate_process_in_guest_request_type)

Terminates a process in the guest OS. 

Terminates a process in the guest OS.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.terminate_process_in_guest_request_type import TerminateProcessInGuestRequestType
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
    api_instance = vmware_vi.GuestProcessManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    terminate_process_in_guest_request_type = vmware_vi.TerminateProcessInGuestRequestType() # TerminateProcessInGuestRequestType | 

    try:
        # Terminates a process in the guest OS. 
        api_instance.guest_process_manager_terminate_process_in_guest(mo_id, terminate_process_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestProcessManagerApi->guest_process_manager_terminate_process_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **terminate_process_in_guest_request_type** | [**TerminateProcessInGuestRequestType**](TerminateProcessInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***GuestProcessNotFound***: if the pid does not refer to a valid process.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the process cannot be terminated because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

