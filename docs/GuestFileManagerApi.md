# vmware_vi.GuestFileManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**guest_file_manager_change_file_attributes_in_guest**](GuestFileManagerApi.md#guest_file_manager_change_file_attributes_in_guest) | **POST** /GuestFileManager/{moId}/ChangeFileAttributesInGuest | Changes the file attributes of a specified file inside the guest. 
[**guest_file_manager_create_temporary_directory_in_guest**](GuestFileManagerApi.md#guest_file_manager_create_temporary_directory_in_guest) | **POST** /GuestFileManager/{moId}/CreateTemporaryDirectoryInGuest | Creates a temporary directory. 
[**guest_file_manager_create_temporary_file_in_guest**](GuestFileManagerApi.md#guest_file_manager_create_temporary_file_in_guest) | **POST** /GuestFileManager/{moId}/CreateTemporaryFileInGuest | Creates a temporary file. 
[**guest_file_manager_delete_directory_in_guest**](GuestFileManagerApi.md#guest_file_manager_delete_directory_in_guest) | **POST** /GuestFileManager/{moId}/DeleteDirectoryInGuest | Deletes a directory in the guest OS. 
[**guest_file_manager_delete_file_in_guest**](GuestFileManagerApi.md#guest_file_manager_delete_file_in_guest) | **POST** /GuestFileManager/{moId}/DeleteFileInGuest | Deletes a file in the guest OS 
[**guest_file_manager_initiate_file_transfer_from_guest**](GuestFileManagerApi.md#guest_file_manager_initiate_file_transfer_from_guest) | **POST** /GuestFileManager/{moId}/InitiateFileTransferFromGuest | Initiates an operation to transfer a file from the guest. 
[**guest_file_manager_initiate_file_transfer_to_guest**](GuestFileManagerApi.md#guest_file_manager_initiate_file_transfer_to_guest) | **POST** /GuestFileManager/{moId}/InitiateFileTransferToGuest | Initiates an operation to transfer a file to the guest. 
[**guest_file_manager_list_files_in_guest**](GuestFileManagerApi.md#guest_file_manager_list_files_in_guest) | **POST** /GuestFileManager/{moId}/ListFilesInGuest | Returns information about files or directories in the guest. 
[**guest_file_manager_make_directory_in_guest**](GuestFileManagerApi.md#guest_file_manager_make_directory_in_guest) | **POST** /GuestFileManager/{moId}/MakeDirectoryInGuest | Creates a directory in the guest OS 
[**guest_file_manager_move_directory_in_guest**](GuestFileManagerApi.md#guest_file_manager_move_directory_in_guest) | **POST** /GuestFileManager/{moId}/MoveDirectoryInGuest | Moves or renames a directory in the guest. 
[**guest_file_manager_move_file_in_guest**](GuestFileManagerApi.md#guest_file_manager_move_file_in_guest) | **POST** /GuestFileManager/{moId}/MoveFileInGuest | Renames a file in the guest. 


# **guest_file_manager_change_file_attributes_in_guest**
> guest_file_manager_change_file_attributes_in_guest(mo_id, change_file_attributes_in_guest_request_type)

Changes the file attributes of a specified file inside the guest. 

Changes the file attributes of a specified file inside the guest.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_file_attributes_in_guest_request_type import ChangeFileAttributesInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_file_attributes_in_guest_request_type = vmware_vi.ChangeFileAttributesInGuestRequestType() # ChangeFileAttributesInGuestRequestType | 

    try:
        # Changes the file attributes of a specified file inside the guest. 
        api_instance.guest_file_manager_change_file_attributes_in_guest(mo_id, change_file_attributes_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_change_file_attributes_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_file_attributes_in_guest_request_type** | [**ChangeFileAttributesInGuestRequestType**](ChangeFileAttributesInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_create_temporary_directory_in_guest**
> str guest_file_manager_create_temporary_directory_in_guest(mo_id, create_temporary_directory_in_guest_request_type)

Creates a temporary directory. 

Creates a temporary directory.  Creates a new unique temporary directory for the user to use as needed. The user is responsible for removing it when it is no longer needed.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_temporary_directory_in_guest_request_type import CreateTemporaryDirectoryInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_temporary_directory_in_guest_request_type = vmware_vi.CreateTemporaryDirectoryInGuestRequestType() # CreateTemporaryDirectoryInGuestRequestType | 

    try:
        # Creates a temporary directory. 
        api_response = api_instance.guest_file_manager_create_temporary_directory_in_guest(mo_id, create_temporary_directory_in_guest_request_type)
        print("The response of GuestFileManagerApi->guest_file_manager_create_temporary_directory_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_create_temporary_directory_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_temporary_directory_in_guest_request_type** | [**CreateTemporaryDirectoryInGuestRequestType**](CreateTemporaryDirectoryInGuestRequestType.md)|  | 

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
**200** | The absolute path of the temporary directory that is created.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_create_temporary_file_in_guest**
> str guest_file_manager_create_temporary_file_in_guest(mo_id, create_temporary_file_in_guest_request_type)

Creates a temporary file. 

Creates a temporary file.  Creates a new unique temporary file for the user to use as needed. The user is responsible for removing it when it is no longer needed.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_temporary_file_in_guest_request_type import CreateTemporaryFileInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_temporary_file_in_guest_request_type = vmware_vi.CreateTemporaryFileInGuestRequestType() # CreateTemporaryFileInGuestRequestType | 

    try:
        # Creates a temporary file. 
        api_response = api_instance.guest_file_manager_create_temporary_file_in_guest(mo_id, create_temporary_file_in_guest_request_type)
        print("The response of GuestFileManagerApi->guest_file_manager_create_temporary_file_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_create_temporary_file_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_temporary_file_in_guest_request_type** | [**CreateTemporaryFileInGuestRequestType**](CreateTemporaryFileInGuestRequestType.md)|  | 

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
**200** | The absolute path of the temporary file that is created.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_delete_directory_in_guest**
> guest_file_manager_delete_directory_in_guest(mo_id, delete_directory_in_guest_request_type)

Deletes a directory in the guest OS. 

Deletes a directory in the guest OS.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_directory_in_guest_request_type import DeleteDirectoryInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_directory_in_guest_request_type = vmware_vi.DeleteDirectoryInGuestRequestType() # DeleteDirectoryInGuestRequestType | 

    try:
        # Deletes a directory in the guest OS. 
        api_instance.guest_file_manager_delete_directory_in_guest(mo_id, delete_directory_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_delete_directory_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_directory_in_guest_request_type** | [**DeleteDirectoryInGuestRequestType**](DeleteDirectoryInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***NotADirectory***: if the specified object is not a directory.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_delete_file_in_guest**
> guest_file_manager_delete_file_in_guest(mo_id, delete_file_in_guest_request_type)

Deletes a file in the guest OS 

Deletes a file in the guest OS  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_file_in_guest_request_type import DeleteFileInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_file_in_guest_request_type = vmware_vi.DeleteFileInGuestRequestType() # DeleteFileInGuestRequestType | 

    try:
        # Deletes a file in the guest OS 
        api_instance.guest_file_manager_delete_file_in_guest(mo_id, delete_file_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_delete_file_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_file_in_guest_request_type** | [**DeleteFileInGuestRequestType**](DeleteFileInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***NotAFile***: if the specified object is not a file.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_initiate_file_transfer_from_guest**
> FileTransferInformation guest_file_manager_initiate_file_transfer_from_guest(mo_id, initiate_file_transfer_from_guest_request_type)

Initiates an operation to transfer a file from the guest. 

Initiates an operation to transfer a file from the guest.  Obtains a reference to *FileTransferInformation* object for the file transfer operation. The information object contains a URL to the file inside the guest to be transferred to the client.    See *FileTransferInformation* for information on how to use the information object. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.  In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm (*VirtualMachine*) -&gt; runtime (*VirtualMachineRuntimeInfo*) \\-&gt; host (*HostSystem*) -&gt; config (*HostConfigInfo*) \\-&gt; certificate.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.file_transfer_information import FileTransferInformation
from vmware_vi.models.initiate_file_transfer_from_guest_request_type import InitiateFileTransferFromGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    initiate_file_transfer_from_guest_request_type = vmware_vi.InitiateFileTransferFromGuestRequestType() # InitiateFileTransferFromGuestRequestType | 

    try:
        # Initiates an operation to transfer a file from the guest. 
        api_response = api_instance.guest_file_manager_initiate_file_transfer_from_guest(mo_id, initiate_file_transfer_from_guest_request_type)
        print("The response of GuestFileManagerApi->guest_file_manager_initiate_file_transfer_from_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_initiate_file_transfer_from_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **initiate_file_transfer_from_guest_request_type** | [**InitiateFileTransferFromGuestRequestType**](InitiateFileTransferFromGuestRequestType.md)|  | 

### Return type

[**FileTransferInformation**](FileTransferInformation.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A reference to *FileTransferInformation*.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: If the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: If the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: If the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_initiate_file_transfer_to_guest**
> str guest_file_manager_initiate_file_transfer_to_guest(mo_id, initiate_file_transfer_to_guest_request_type)

Initiates an operation to transfer a file to the guest. 

Initiates an operation to transfer a file to the guest.  Obtains a URL to the file inside the guest to be transferred from the client. The user should send a HTTP PUT request specifying the file content in the body of the request. Multiple PUT request cannot be sent to the URL simultaneously. URL will be invalidated after a successful PUT request is sent. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.  In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm (*VirtualMachine*) -&gt; runtime (*VirtualMachineRuntimeInfo*) \\-&gt; host (*HostSystem*) -&gt; config (*HostConfigInfo*) \\-&gt; certificate.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.initiate_file_transfer_to_guest_request_type import InitiateFileTransferToGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    initiate_file_transfer_to_guest_request_type = vmware_vi.InitiateFileTransferToGuestRequestType() # InitiateFileTransferToGuestRequestType | 

    try:
        # Initiates an operation to transfer a file to the guest. 
        api_response = api_instance.guest_file_manager_initiate_file_transfer_to_guest(mo_id, initiate_file_transfer_to_guest_request_type)
        print("The response of GuestFileManagerApi->guest_file_manager_initiate_file_transfer_to_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_initiate_file_transfer_to_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **initiate_file_transfer_to_guest_request_type** | [**InitiateFileTransferToGuestRequestType**](InitiateFileTransferToGuestRequestType.md)|  | 

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
**200** | A URL to which the user has to send a PUT request. The host part of the URL is returned as &#39;\\*&#39; if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file can be uploaded to &#x60;https://esx-svr-1.domain1.com/guestFile?id&#x3D;1&amp;token&#x3D;1234&#x60;, the URL returned may be &#x60;https://&amp;#42;/guestFile?id&#x3D;1&amp;token&#x3D;1234&#x60;. The client replaces the asterisk with the server name on which it invoked the call.       The URL is valid only for 10 minutes from the time it is generated. Also, the URL becomes invalid whenever the virtual machine is powered off, suspended or unregistered.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: If the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: If the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: If the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_list_files_in_guest**
> GuestListFileInfo guest_file_manager_list_files_in_guest(mo_id, list_files_in_guest_request_type)

Returns information about files or directories in the guest. 

Returns information about files or directories in the guest.  The results could be extremely large, so to minimize the size of the return value for cases where a UI only needs to show the first N results, the answer is batched. Files are returned in OS-specific (inode) order. If the directory is modified between queries, missing or duplicate results can occur.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_list_file_info import GuestListFileInfo
from vmware_vi.models.list_files_in_guest_request_type import ListFilesInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_files_in_guest_request_type = vmware_vi.ListFilesInGuestRequestType() # ListFilesInGuestRequestType | 

    try:
        # Returns information about files or directories in the guest. 
        api_response = api_instance.guest_file_manager_list_files_in_guest(mo_id, list_files_in_guest_request_type)
        print("The response of GuestFileManagerApi->guest_file_manager_list_files_in_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_list_files_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_files_in_guest_request_type** | [**ListFilesInGuestRequestType**](ListFilesInGuestRequestType.md)|  | 

### Return type

[**GuestListFileInfo**](GuestListFileInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A *GuestListFileInfo* object containing information for all the matching files in the filePath and the number of files left to be returned.  |  -  |
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidArgument***: If the matchPattern is an invalid regular expression.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_make_directory_in_guest**
> guest_file_manager_make_directory_in_guest(mo_id, make_directory_in_guest_request_type)

Creates a directory in the guest OS 

Creates a directory in the guest OS  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.make_directory_in_guest_request_type import MakeDirectoryInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    make_directory_in_guest_request_type = vmware_vi.MakeDirectoryInGuestRequestType() # MakeDirectoryInGuestRequestType | 

    try:
        # Creates a directory in the guest OS 
        api_instance.guest_file_manager_make_directory_in_guest(mo_id, make_directory_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_make_directory_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **make_directory_in_guest_request_type** | [**MakeDirectoryInGuestRequestType**](MakeDirectoryInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the directory cannot be created because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileAlreadyExists***: if the specified object already exists.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_move_directory_in_guest**
> guest_file_manager_move_directory_in_guest(mo_id, move_directory_in_guest_request_type)

Moves or renames a directory in the guest. 

Moves or renames a directory in the guest.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.move_directory_in_guest_request_type import MoveDirectoryInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_directory_in_guest_request_type = vmware_vi.MoveDirectoryInGuestRequestType() # MoveDirectoryInGuestRequestType | 

    try:
        # Moves or renames a directory in the guest. 
        api_instance.guest_file_manager_move_directory_in_guest(mo_id, move_directory_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_move_directory_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_directory_in_guest_request_type** | [**MoveDirectoryInGuestRequestType**](MoveDirectoryInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_file_manager_move_file_in_guest**
> guest_file_manager_move_file_in_guest(mo_id, move_file_in_guest_request_type)

Renames a file in the guest. 

Renames a file in the guest.  ***Since:*** vSphere API 5.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.move_file_in_guest_request_type import MoveFileInGuestRequestType
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
    api_instance = vmware_vi.GuestFileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_file_in_guest_request_type = vmware_vi.MoveFileInGuestRequestType() # MoveFileInGuestRequestType | 

    try:
        # Renames a file in the guest. 
        api_instance.guest_file_manager_move_file_in_guest(mo_id, move_file_in_guest_request_type)
    except Exception as e:
        print("Exception when calling GuestFileManagerApi->guest_file_manager_move_file_in_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_file_in_guest_request_type** | [**MoveFileInGuestRequestType**](MoveFileInGuestRequestType.md)|  | 

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
**500** | ***GuestOperationsFault***: if there is an error processing a guest operation.  ***GuestOperationsUnavailable***: if the VM agent for guest operations is not running.  ***InvalidPowerState***: if the VM is not powered on.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***TaskInProgress***: if the virtual machine is busy.  ***GuestPermissionDenied***: if the operation fails because the guest authentication will not allow the operation.  ***InvalidGuestLogin***: if the the guest authentication information was not accepted.  ***FileFault***: if there is a file error in the guest operating system.  ***GuestComponentsOutOfDate***: if the guest agent is too old to support the operation.  ***OperationNotSupportedByGuest***: if the operation is not supported by the guest OS.  ***OperationDisabledByGuest***: if the operation is not enabled due to guest agent configuration.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

