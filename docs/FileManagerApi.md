# vmware_vi.FileManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_manager_change_owner**](FileManagerApi.md#file_manager_change_owner) | **POST** /FileManager/{moId}/ChangeOwner | Change the owner for a file. 
[**file_manager_copy_datastore_file_task**](FileManagerApi.md#file_manager_copy_datastore_file_task) | **POST** /FileManager/{moId}/CopyDatastoreFile_Task | Copies the source file or folder to the destination. 
[**file_manager_delete_datastore_file_task**](FileManagerApi.md#file_manager_delete_datastore_file_task) | **POST** /FileManager/{moId}/DeleteDatastoreFile_Task | Deletes the specified file or folder from the datastore. 
[**file_manager_make_directory**](FileManagerApi.md#file_manager_make_directory) | **POST** /FileManager/{moId}/MakeDirectory | Create a folder using the specified name. 
[**file_manager_move_datastore_file_task**](FileManagerApi.md#file_manager_move_datastore_file_task) | **POST** /FileManager/{moId}/MoveDatastoreFile_Task | Moves the source file or folder to the destination. 


# **file_manager_change_owner**
> file_manager_change_owner(mo_id, change_owner_request_type)

Change the owner for a file. 

Change the owner for a file.  This method is currently not supported.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_owner_request_type import ChangeOwnerRequestType
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
    api_instance = vmware_vi.FileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_owner_request_type = vmware_vi.ChangeOwnerRequestType() # ChangeOwnerRequestType | 

    try:
        # Change the owner for a file. 
        api_instance.file_manager_change_owner(mo_id, change_owner_request_type)
    except Exception as e:
        print("Exception when calling FileManagerApi->file_manager_change_owner: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_owner_request_type** | [**ChangeOwnerRequestType**](ChangeOwnerRequestType.md)|  | 

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

# **file_manager_copy_datastore_file_task**
> ManagedObjectReference file_manager_copy_datastore_file_task(mo_id, copy_datastore_file_request_type)

Copies the source file or folder to the destination. 

Copies the source file or folder to the destination.  If the destination file does not exist, it is created. If the destination file exists, the force parameter determines whether to overwrite it with the source or not. Folders can be copied recursively. In this case, the destination, if it exists, must be a folder, else one will be created. Existing files on the destination that conflict with source files can be overwritten using the force parameter. Files and disks are always copied in binary format during recursive copy.  If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.  If any intermediate level folder specified by the source and destination does not exist, a *FileNotFound* fault is thrown.  If a file of a virtual machine is overwritten on the destination datastore as a result of the force parameter, it may corrupt that virtual machine.  If the source is an extent of a virtual disk, this operation treats the extent as a file.  If source and destination resolve to the same file system location, the call has no effect.  It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided when copying a folder. If the intent is to clone a virtual machine registered in the inventory, with transactional guarantees, please refer to *VirtualMachine.CloneVM_Task*.  Datastore.FileManagement privilege is required on both source and destination datastores.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.copy_datastore_file_request_type import CopyDatastoreFileRequestType
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
    api_instance = vmware_vi.FileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    copy_datastore_file_request_type = vmware_vi.CopyDatastoreFileRequestType() # CopyDatastoreFileRequestType | 

    try:
        # Copies the source file or folder to the destination. 
        api_response = api_instance.file_manager_copy_datastore_file_task(mo_id, copy_datastore_file_request_type)
        print("The response of FileManagerApi->file_manager_copy_datastore_file_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagerApi->file_manager_copy_datastore_file_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **copy_datastore_file_request_type** | [**CopyDatastoreFileRequestType**](CopyDatastoreFileRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: if the operation cannot be performed on the source or destination datastores. Typically, a specific subclass of this exception is thrown.  ***FileNotFound***: if the file or folder specified by sourceName is not found, or, any intermediate level folder specified by the destinationName is not found.  ***CannotAccessFile***: if the source cannot be accessed because of insufficient permissions.  ***FileLocked***: if the source file or folder is currently locked or in use.  ***FileAlreadyExists***: if a file with the given name already exists at the destination, and the force flag is false.  ***NoDiskSpace***: if there is not enough space available at the destination datastore.  ***FileFault***: if there is a generic file error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_manager_delete_datastore_file_task**
> ManagedObjectReference file_manager_delete_datastore_file_task(mo_id, delete_datastore_file_request_type)

Deletes the specified file or folder from the datastore. 

Deletes the specified file or folder from the datastore.  If a file of a virtual machine is deleted, it may corrupt that virtual machine. Folder deletes are always recursive. The datacenter parameter may be omitted if a URL is used to name the file or folder.  If the source is an extent of a virtual disk, this operation treats the extent as a file.  It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided when deleting folders. If the intent is to delete a virtual machine registered in the inventory, please refer to *ManagedEntity.Destroy_Task*.  Requires Datastore.FileManagement privilege on the datastore.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_datastore_file_request_type import DeleteDatastoreFileRequestType
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
    api_instance = vmware_vi.FileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_datastore_file_request_type = vmware_vi.DeleteDatastoreFileRequestType() # DeleteDatastoreFileRequestType | 

    try:
        # Deletes the specified file or folder from the datastore. 
        api_response = api_instance.file_manager_delete_datastore_file_task(mo_id, delete_datastore_file_request_type)
        print("The response of FileManagerApi->file_manager_delete_datastore_file_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagerApi->file_manager_delete_datastore_file_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_datastore_file_request_type** | [**DeleteDatastoreFileRequestType**](DeleteDatastoreFileRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: if the operation cannot be performed on the datastore. Typically, a specific subclass of this exception is thrown.  ***FileNotFound***: if the file or folder specified by name is not found.  ***CannotDeleteFile***: if the delete operation on the file or folder fails.  ***FileLocked***: if the source file or folder is currently locked or in use.  ***FileFault***: if there is a generic file error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_manager_make_directory**
> file_manager_make_directory(mo_id, make_directory_request_type)

Create a folder using the specified name. 

Create a folder using the specified name.  If the parent or intermediate level folders do not exist, and the parameter createParentDirectories is false, a *FileNotFound* fault is thrown. If the intermediate level folders do not exist, and the parameter createParentDirectories is true, all the non-existent folders are created.  Requires Datastore.FileManagement privilege on the datastore.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.make_directory_request_type import MakeDirectoryRequestType
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
    api_instance = vmware_vi.FileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    make_directory_request_type = vmware_vi.MakeDirectoryRequestType() # MakeDirectoryRequestType | 

    try:
        # Create a folder using the specified name. 
        api_instance.file_manager_make_directory(mo_id, make_directory_request_type)
    except Exception as e:
        print("Exception when calling FileManagerApi->file_manager_make_directory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **make_directory_request_type** | [**MakeDirectoryRequestType**](MakeDirectoryRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: if the operation cannot be performed on the datastore. Typically, a specific subclass of this exception is thrown.  ***CannotCreateFile***: if the create operation on the folder fails.  ***FileAlreadyExists***: if a file or folder with the given name already exists at the destination.  ***FileNotFound***: if the createParentDirectories is false and a intermediate level folder specified by name is not found.  ***FileFault***: if there is a generic file error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_manager_move_datastore_file_task**
> ManagedObjectReference file_manager_move_datastore_file_task(mo_id, move_datastore_file_request_type)

Moves the source file or folder to the destination. 

Moves the source file or folder to the destination.  If the destination file does not exist, it is created. If the destination file exists, the force parameter determines whether to overwrite it with the source or not. If the source path is a folder, then the destination path must not exist; the destination cannot be overwritten even with a force flag in that case. Folder moves are recursive, treating all files and disks to move as binary.  If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.  If any intermediate level folder specified by the source and destination does not exist, a *FileNotFound* fault is thrown.  If a file of a virtual machine is moved, it may corrupt that virtual machine. If a file of a virtual machine is overwritten on the destination datastore as a result of the force parameter, it may corrupt that virtual machine.  If the source is an extent of a virtual disk, this operation treats the extent as a file.  If source and destination resolve to the same file system location, the call has no effect.  It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided for folder moves. If the intent is to move a virtual machine registered in the inventory, with transactional guarantees, please refer to *VirtualMachine.RelocateVM_Task*. If the intent is to rename a virtual machine registered in the inventory, please refer to *ManagedEntity.Rename_Task*.  Datastore.FileManagement privilege is required on both source and destination datastores.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_datastore_file_request_type import MoveDatastoreFileRequestType
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
    api_instance = vmware_vi.FileManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_datastore_file_request_type = vmware_vi.MoveDatastoreFileRequestType() # MoveDatastoreFileRequestType | 

    try:
        # Moves the source file or folder to the destination. 
        api_response = api_instance.file_manager_move_datastore_file_task(mo_id, move_datastore_file_request_type)
        print("The response of FileManagerApi->file_manager_move_datastore_file_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagerApi->file_manager_move_datastore_file_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_datastore_file_request_type** | [**MoveDatastoreFileRequestType**](MoveDatastoreFileRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: if the operation cannot be performed on the source or destination datastores. Typically, a specific subclass of this exception is thrown.  ***FileNotFound***: if the file or folder specified by sourceName is not found, or, any intermediate level folder specified by the destinationName is not found.  ***CannotAccessFile***: if the source file or folder cannot be moved because of insufficient permissions.  ***FileLocked***: if the source file or folder is currently locked or in use.  ***FileAlreadyExists***: if a file with the given name already exists at the destination, and the force flag is false. For folders, if the destination exists, this fault is thrown regardless.  ***NoDiskSpace***: if there is not enough space available on the destination datastore.  ***FileFault***: if there is a generic file error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

