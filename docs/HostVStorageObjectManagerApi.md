# vmware_vi.HostVStorageObjectManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_v_storage_object_manager_host_clear_v_storage_object_control_flags**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_clear_v_storage_object_control_flags) | **POST** /HostVStorageObjectManager/{moId}/HostClearVStorageObjectControlFlags | Clear control flags on VStorageObject. 
[**host_v_storage_object_manager_host_clone_v_storage_object_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_clone_v_storage_object_task) | **POST** /HostVStorageObjectManager/{moId}/HostCloneVStorageObject_Task | Clone a virtual storage object. 
[**host_v_storage_object_manager_host_create_disk_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_create_disk_task) | **POST** /HostVStorageObjectManager/{moId}/HostCreateDisk_Task | Create a virtual disk, which is a storage object with *disk* as consumption type. 
[**host_v_storage_object_manager_host_delete_v_storage_object_ex_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_delete_v_storage_object_ex_task) | **POST** /HostVStorageObjectManager/{moId}/HostDeleteVStorageObjectEx_Task | Delete a virtual storage object and its assoicated backings. 
[**host_v_storage_object_manager_host_delete_v_storage_object_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_delete_v_storage_object_task) | **POST** /HostVStorageObjectManager/{moId}/HostDeleteVStorageObject_Task | Delete a virtual storage object and its assoicated backings. 
[**host_v_storage_object_manager_host_extend_disk_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_extend_disk_task) | **POST** /HostVStorageObjectManager/{moId}/HostExtendDisk_Task | Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 
[**host_v_storage_object_manager_host_inflate_disk_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_inflate_disk_task) | **POST** /HostVStorageObjectManager/{moId}/HostInflateDisk_Task | Inflate a sparse or thin-provisioned virtual disk up to the full size. 
[**host_v_storage_object_manager_host_list_v_storage_object**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_list_v_storage_object) | **POST** /HostVStorageObjectManager/{moId}/HostListVStorageObject | List all virtual storage objects located on a datastore. 
[**host_v_storage_object_manager_host_reconcile_datastore_inventory_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_reconcile_datastore_inventory_task) | **POST** /HostVStorageObjectManager/{moId}/HostReconcileDatastoreInventory_Task | Reconcile the datastore inventory info of virtual storage objects. 
[**host_v_storage_object_manager_host_register_disk**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_register_disk) | **POST** /HostVStorageObjectManager/{moId}/HostRegisterDisk | Promote a virtual disk to a First Class Disk. 
[**host_v_storage_object_manager_host_relocate_v_storage_object_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_relocate_v_storage_object_task) | **POST** /HostVStorageObjectManager/{moId}/HostRelocateVStorageObject_Task | Relocate a virtual storage object. 
[**host_v_storage_object_manager_host_rename_v_storage_object**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_rename_v_storage_object) | **POST** /HostVStorageObjectManager/{moId}/HostRenameVStorageObject | Rename a virtual storage object. 
[**host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy) | **POST** /HostVStorageObjectManager/{moId}/HostRetrieveVStorageInfrastructureObjectPolicy | Retrieve virtual storage infrastructure object SBPM policy on given datastore. 
[**host_v_storage_object_manager_host_retrieve_v_storage_object**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_retrieve_v_storage_object) | **POST** /HostVStorageObjectManager/{moId}/HostRetrieveVStorageObject | Retrieve a virtual storage object. 
[**host_v_storage_object_manager_host_retrieve_v_storage_object_metadata**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_retrieve_v_storage_object_metadata) | **POST** /HostVStorageObjectManager/{moId}/HostRetrieveVStorageObjectMetadata | Retrieve metadata KV pairs from a virtual storage object. 
[**host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value) | **POST** /HostVStorageObjectManager/{moId}/HostRetrieveVStorageObjectMetadataValue | Retrieve the metadata value by key from a virtual storage object. 
[**host_v_storage_object_manager_host_retrieve_v_storage_object_state**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_retrieve_v_storage_object_state) | **POST** /HostVStorageObjectManager/{moId}/HostRetrieveVStorageObjectState | Retrieve a virtual storage object state. 
[**host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory) | **POST** /HostVStorageObjectManager/{moId}/HostScheduleReconcileDatastoreInventory | Schedules reconcile of the datastore inventory info of virtual storage objects. 
[**host_v_storage_object_manager_host_set_v_storage_object_control_flags**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_set_v_storage_object_control_flags) | **POST** /HostVStorageObjectManager/{moId}/HostSetVStorageObjectControlFlags | Set control flags on VStorageObject. 
[**host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task) | **POST** /HostVStorageObjectManager/{moId}/HostUpdateVStorageObjectMetadataEx_Task | Update metadata KV pairs to a virtual storage object. 
[**host_v_storage_object_manager_host_update_v_storage_object_metadata_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_update_v_storage_object_metadata_task) | **POST** /HostVStorageObjectManager/{moId}/HostUpdateVStorageObjectMetadata_Task | Update metadata KV pairs to a virtual storage object. 
[**host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task) | **POST** /HostVStorageObjectManager/{moId}/HostVStorageObjectCreateDiskFromSnapshot_Task | Creates a new Disk from given snapshot of a VStorageObject. 
[**host_v_storage_object_manager_host_v_storage_object_create_snapshot_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_v_storage_object_create_snapshot_task) | **POST** /HostVStorageObjectManager/{moId}/HostVStorageObjectCreateSnapshot_Task | Creates a snapshot of a given VStorageObject. 
[**host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task) | **POST** /HostVStorageObjectManager/{moId}/HostVStorageObjectDeleteSnapshot_Task | Deletes a given snapshot of a VStorageObject. 
[**host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info) | **POST** /HostVStorageObjectManager/{moId}/HostVStorageObjectRetrieveSnapshotInfo | Retrieves snapshot information of a given VStorageObject. 
[**host_v_storage_object_manager_host_v_storage_object_revert_task**](HostVStorageObjectManagerApi.md#host_v_storage_object_manager_host_v_storage_object_revert_task) | **POST** /HostVStorageObjectManager/{moId}/HostVStorageObjectRevert_Task | Reverts to a given snapshot of a VStorageObject. 


# **host_v_storage_object_manager_host_clear_v_storage_object_control_flags**
> host_v_storage_object_manager_host_clear_v_storage_object_control_flags(mo_id, host_clear_v_storage_object_control_flags_request_type)

Clear control flags on VStorageObject. 

Clear control flags on VStorageObject.  The control flags are defined in *vslmVStorageObjectControlFlag_enum*.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_clear_v_storage_object_control_flags_request_type import HostClearVStorageObjectControlFlagsRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_clear_v_storage_object_control_flags_request_type = vmware_vi.HostClearVStorageObjectControlFlagsRequestType() # HostClearVStorageObjectControlFlagsRequestType | 

    try:
        # Clear control flags on VStorageObject. 
        api_instance.host_v_storage_object_manager_host_clear_v_storage_object_control_flags(mo_id, host_clear_v_storage_object_control_flags_request_type)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_clear_v_storage_object_control_flags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_clear_v_storage_object_control_flags_request_type** | [**HostClearVStorageObjectControlFlagsRequestType**](HostClearVStorageObjectControlFlagsRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_clone_v_storage_object_task**
> ManagedObjectReference host_v_storage_object_manager_host_clone_v_storage_object_task(mo_id, host_clone_v_storage_object_request_type)

Clone a virtual storage object. 

Clone a virtual storage object.  Requires Datastore.FileManagement privilege on both source and destination datastore.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_clone_v_storage_object_request_type import HostCloneVStorageObjectRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_clone_v_storage_object_request_type = vmware_vi.HostCloneVStorageObjectRequestType() # HostCloneVStorageObjectRequestType | 

    try:
        # Clone a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_clone_v_storage_object_task(mo_id, host_clone_v_storage_object_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_clone_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_clone_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_clone_v_storage_object_request_type** | [**HostCloneVStorageObjectRequestType**](HostCloneVStorageObjectRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while cloning the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_create_disk_task**
> ManagedObjectReference host_v_storage_object_manager_host_create_disk_task(mo_id, host_create_disk_request_type)

Create a virtual disk, which is a storage object with *disk* as consumption type. 

Create a virtual disk, which is a storage object with *disk* as consumption type.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk object is created.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_create_disk_request_type import HostCreateDiskRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_create_disk_request_type = vmware_vi.HostCreateDiskRequestType() # HostCreateDiskRequestType | 

    try:
        # Create a virtual disk, which is a storage object with *disk* as consumption type. 
        api_response = api_instance.host_v_storage_object_manager_host_create_disk_task(mo_id, host_create_disk_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_create_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_create_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_create_disk_request_type** | [**HostCreateDiskRequestType**](HostCreateDiskRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly created *VStorageObject* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***FileFault***: If an error occurs when creating the virtual disk.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_delete_v_storage_object_ex_task**
> ManagedObjectReference host_v_storage_object_manager_host_delete_v_storage_object_ex_task(mo_id, host_delete_v_storage_object_ex_request_type)

Delete a virtual storage object and its assoicated backings. 

Delete a virtual storage object and its assoicated backings.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 7.0.2.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_delete_v_storage_object_ex_request_type import HostDeleteVStorageObjectExRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_delete_v_storage_object_ex_request_type = vmware_vi.HostDeleteVStorageObjectExRequestType() # HostDeleteVStorageObjectExRequestType | 

    try:
        # Delete a virtual storage object and its assoicated backings. 
        api_response = api_instance.host_v_storage_object_manager_host_delete_v_storage_object_ex_task(mo_id, host_delete_v_storage_object_ex_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_delete_v_storage_object_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_delete_v_storage_object_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_delete_v_storage_object_ex_request_type** | [**HostDeleteVStorageObjectExRequestType**](HostDeleteVStorageObjectExRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs when deleting the virtual storage object.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed and cannot be deleted.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_delete_v_storage_object_task**
> ManagedObjectReference host_v_storage_object_manager_host_delete_v_storage_object_task(mo_id, host_delete_v_storage_object_request_type)

Delete a virtual storage object and its assoicated backings. 

Delete a virtual storage object and its assoicated backings.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_delete_v_storage_object_request_type import HostDeleteVStorageObjectRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_delete_v_storage_object_request_type = vmware_vi.HostDeleteVStorageObjectRequestType() # HostDeleteVStorageObjectRequestType | 

    try:
        # Delete a virtual storage object and its assoicated backings. 
        api_response = api_instance.host_v_storage_object_manager_host_delete_v_storage_object_task(mo_id, host_delete_v_storage_object_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_delete_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_delete_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_delete_v_storage_object_request_type** | [**HostDeleteVStorageObjectRequestType**](HostDeleteVStorageObjectRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs when deleting the virtual storage object.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed and cannot be deleted.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_extend_disk_task**
> ManagedObjectReference host_v_storage_object_manager_host_extend_disk_task(mo_id, host_extend_disk_request_type)

Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 

Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity.  If new capacity is smaller than current disk capacity, then operation fails due to invalid capacity. If new capacity is greater than current disk capacity, then operation proceeds. If new capacity is equal to current disk ccapcity, then operation succeeds without any actual extension. The extended disk region will be the same as the original disk: \\- For a zerothick disk, the extended disk region will be zeroedthick. \\- For an eagerzerothick disk, the extended disk region will be eagerzeroedthick \\- A thin-provisioned disk will always be extended as a thin-provisioned disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_extend_disk_request_type import HostExtendDiskRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_extend_disk_request_type = vmware_vi.HostExtendDiskRequestType() # HostExtendDiskRequestType | 

    try:
        # Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 
        api_response = api_instance.host_v_storage_object_manager_host_extend_disk_task(mo_id, host_extend_disk_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_extend_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_extend_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_extend_disk_request_type** | [**HostExtendDiskRequestType**](HostExtendDiskRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while extending the virtual disk.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed and cannot be extended.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_inflate_disk_task**
> ManagedObjectReference host_v_storage_object_manager_host_inflate_disk_task(mo_id, host_inflate_disk_request_type)

Inflate a sparse or thin-provisioned virtual disk up to the full size. 

Inflate a sparse or thin-provisioned virtual disk up to the full size.  Additional space allocated to the disk as a result of this operation will be filled with zeroes.  Currently inflateDisk API only supports the following combinations: Valid provisioning type: THIN; Valid Datastore: VMFS, NFS. Inflating a disk is not applicable for VVol/VSAN datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_inflate_disk_request_type import HostInflateDiskRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_inflate_disk_request_type = vmware_vi.HostInflateDiskRequestType() # HostInflateDiskRequestType | 

    try:
        # Inflate a sparse or thin-provisioned virtual disk up to the full size. 
        api_response = api_instance.host_v_storage_object_manager_host_inflate_disk_task(mo_id, host_inflate_disk_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_inflate_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_inflate_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_inflate_disk_request_type** | [**HostInflateDiskRequestType**](HostInflateDiskRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while inflating the virtual disk.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed and cannot be extended.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_list_v_storage_object**
> List[ID] host_v_storage_object_manager_host_list_v_storage_object(mo_id, host_list_v_storage_object_request_type)

List all virtual storage objects located on a datastore. 

List all virtual storage objects located on a datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_list_v_storage_object_request_type import HostListVStorageObjectRequestType
from vmware_vi.models.id import ID
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_list_v_storage_object_request_type = vmware_vi.HostListVStorageObjectRequestType() # HostListVStorageObjectRequestType | 

    try:
        # List all virtual storage objects located on a datastore. 
        api_response = api_instance.host_v_storage_object_manager_host_list_v_storage_object(mo_id, host_list_v_storage_object_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_list_v_storage_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_list_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_list_v_storage_object_request_type** | [**HostListVStorageObjectRequestType**](HostListVStorageObjectRequestType.md)|  | 

### Return type

[**List[ID]**](ID.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of IDs of the virtual storage objects located on the datastore.  |  -  |
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or inaccessible.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_reconcile_datastore_inventory_task**
> ManagedObjectReference host_v_storage_object_manager_host_reconcile_datastore_inventory_task(mo_id, host_reconcile_datastore_inventory_request_type)

Reconcile the datastore inventory info of virtual storage objects. 

Reconcile the datastore inventory info of virtual storage objects.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_reconcile_datastore_inventory_request_type import HostReconcileDatastoreInventoryRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_reconcile_datastore_inventory_request_type = vmware_vi.HostReconcileDatastoreInventoryRequestType() # HostReconcileDatastoreInventoryRequestType | 

    try:
        # Reconcile the datastore inventory info of virtual storage objects. 
        api_response = api_instance.host_v_storage_object_manager_host_reconcile_datastore_inventory_task(mo_id, host_reconcile_datastore_inventory_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_reconcile_datastore_inventory_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_reconcile_datastore_inventory_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_reconcile_datastore_inventory_request_type** | [**HostReconcileDatastoreInventoryRequestType**](HostReconcileDatastoreInventoryRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_register_disk**
> VStorageObject host_v_storage_object_manager_host_register_disk(mo_id, host_register_disk_request_type)

Promote a virtual disk to a First Class Disk. 

Promote a virtual disk to a First Class Disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_register_disk_request_type import HostRegisterDiskRequestType
from vmware_vi.models.v_storage_object import VStorageObject
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_register_disk_request_type = vmware_vi.HostRegisterDiskRequestType() # HostRegisterDiskRequestType | 

    try:
        # Promote a virtual disk to a First Class Disk. 
        api_response = api_instance.host_v_storage_object_manager_host_register_disk(mo_id, host_register_disk_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_register_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_register_disk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_register_disk_request_type** | [**HostRegisterDiskRequestType**](HostRegisterDiskRequestType.md)|  | 

### Return type

[**VStorageObject**](VStorageObject.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The registered virtual storage object for the disk.  |  -  |
**500** | ***FileFault***: If an error occurs while registering the virtual disk.  ***InvalidDatastore***: If datastore cannot be found or the operation cannot be performed on the datastore.  ***AlreadyExists***: If disk is already registered as a virtual storage object.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_relocate_v_storage_object_task**
> ManagedObjectReference host_v_storage_object_manager_host_relocate_v_storage_object_task(mo_id, host_relocate_v_storage_object_request_type)

Relocate a virtual storage object. 

Relocate a virtual storage object.  Requires Datastore.FileManagement privilege on both source and destination datastore.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_relocate_v_storage_object_request_type import HostRelocateVStorageObjectRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_relocate_v_storage_object_request_type = vmware_vi.HostRelocateVStorageObjectRequestType() # HostRelocateVStorageObjectRequestType | 

    try:
        # Relocate a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_relocate_v_storage_object_task(mo_id, host_relocate_v_storage_object_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_relocate_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_relocate_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_relocate_v_storage_object_request_type** | [**HostRelocateVStorageObjectRequestType**](HostRelocateVStorageObjectRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while relocating the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed and cannot be relocated.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_rename_v_storage_object**
> host_v_storage_object_manager_host_rename_v_storage_object(mo_id, host_rename_v_storage_object_request_type)

Rename a virtual storage object. 

Rename a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_rename_v_storage_object_request_type import HostRenameVStorageObjectRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_rename_v_storage_object_request_type = vmware_vi.HostRenameVStorageObjectRequestType() # HostRenameVStorageObjectRequestType | 

    try:
        # Rename a virtual storage object. 
        api_instance.host_v_storage_object_manager_host_rename_v_storage_object(mo_id, host_rename_v_storage_object_request_type)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_rename_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_rename_v_storage_object_request_type** | [**HostRenameVStorageObjectRequestType**](HostRenameVStorageObjectRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while renaming the virtual storage object.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy**
> List[VslmInfrastructureObjectPolicy] host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy(mo_id, host_retrieve_v_storage_infrastructure_object_policy_request_type)

Retrieve virtual storage infrastructure object SBPM policy on given datastore. 

Retrieve virtual storage infrastructure object SBPM policy on given datastore.  Only support VSAN datastore.  Requires Datastore.FileManagement privilege on the datastore specified.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_retrieve_v_storage_infrastructure_object_policy_request_type import HostRetrieveVStorageInfrastructureObjectPolicyRequestType
from vmware_vi.models.vslm_infrastructure_object_policy import VslmInfrastructureObjectPolicy
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_retrieve_v_storage_infrastructure_object_policy_request_type = vmware_vi.HostRetrieveVStorageInfrastructureObjectPolicyRequestType() # HostRetrieveVStorageInfrastructureObjectPolicyRequestType | 

    try:
        # Retrieve virtual storage infrastructure object SBPM policy on given datastore. 
        api_response = api_instance.host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy(mo_id, host_retrieve_v_storage_infrastructure_object_policy_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_infrastructure_object_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_retrieve_v_storage_infrastructure_object_policy_request_type** | [**HostRetrieveVStorageInfrastructureObjectPolicyRequestType**](HostRetrieveVStorageInfrastructureObjectPolicyRequestType.md)|  | 

### Return type

[**List[VslmInfrastructureObjectPolicy]**](VslmInfrastructureObjectPolicy.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The policy object of virtual storage object.  |  -  |
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_retrieve_v_storage_object**
> VStorageObject host_v_storage_object_manager_host_retrieve_v_storage_object(mo_id, host_retrieve_v_storage_object_request_type)

Retrieve a virtual storage object. 

Retrieve a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_retrieve_v_storage_object_request_type import HostRetrieveVStorageObjectRequestType
from vmware_vi.models.v_storage_object import VStorageObject
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_retrieve_v_storage_object_request_type = vmware_vi.HostRetrieveVStorageObjectRequestType() # HostRetrieveVStorageObjectRequestType | 

    try:
        # Retrieve a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_retrieve_v_storage_object(mo_id, host_retrieve_v_storage_object_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_retrieve_v_storage_object_request_type** | [**HostRetrieveVStorageObjectRequestType**](HostRetrieveVStorageObjectRequestType.md)|  | 

### Return type

[**VStorageObject**](VStorageObject.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The required virtual storage object.  |  -  |
**500** | ***FileFault***: If an error occurs when retrieving the virtual object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_retrieve_v_storage_object_metadata**
> List[KeyValue] host_v_storage_object_manager_host_retrieve_v_storage_object_metadata(mo_id, host_retrieve_v_storage_object_metadata_request_type)

Retrieve metadata KV pairs from a virtual storage object. 

Retrieve metadata KV pairs from a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_retrieve_v_storage_object_metadata_request_type import HostRetrieveVStorageObjectMetadataRequestType
from vmware_vi.models.key_value import KeyValue
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_retrieve_v_storage_object_metadata_request_type = vmware_vi.HostRetrieveVStorageObjectMetadataRequestType() # HostRetrieveVStorageObjectMetadataRequestType | 

    try:
        # Retrieve metadata KV pairs from a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_retrieve_v_storage_object_metadata(mo_id, host_retrieve_v_storage_object_metadata_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_retrieve_v_storage_object_metadata_request_type** | [**HostRetrieveVStorageObjectMetadataRequestType**](HostRetrieveVStorageObjectMetadataRequestType.md)|  | 

### Return type

[**List[KeyValue]**](KeyValue.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the array of key value pair  |  -  |
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or inaccessible.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value**
> str host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value(mo_id, host_retrieve_v_storage_object_metadata_value_request_type)

Retrieve the metadata value by key from a virtual storage object. 

Retrieve the metadata value by key from a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_retrieve_v_storage_object_metadata_value_request_type import HostRetrieveVStorageObjectMetadataValueRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_retrieve_v_storage_object_metadata_value_request_type = vmware_vi.HostRetrieveVStorageObjectMetadataValueRequestType() # HostRetrieveVStorageObjectMetadataValueRequestType | 

    try:
        # Retrieve the metadata value by key from a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value(mo_id, host_retrieve_v_storage_object_metadata_value_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_metadata_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_retrieve_v_storage_object_metadata_value_request_type** | [**HostRetrieveVStorageObjectMetadataValueRequestType**](HostRetrieveVStorageObjectMetadataValueRequestType.md)|  | 

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
**200** | returns the value for the key  |  -  |
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or inaccessible.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  ***KeyNotFound***: If specified key cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_retrieve_v_storage_object_state**
> VStorageObjectStateInfo host_v_storage_object_manager_host_retrieve_v_storage_object_state(mo_id, host_retrieve_v_storage_object_state_request_type)

Retrieve a virtual storage object state. 

Retrieve a virtual storage object state.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_retrieve_v_storage_object_state_request_type import HostRetrieveVStorageObjectStateRequestType
from vmware_vi.models.v_storage_object_state_info import VStorageObjectStateInfo
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_retrieve_v_storage_object_state_request_type = vmware_vi.HostRetrieveVStorageObjectStateRequestType() # HostRetrieveVStorageObjectStateRequestType | 

    try:
        # Retrieve a virtual storage object state. 
        api_response = api_instance.host_v_storage_object_manager_host_retrieve_v_storage_object_state(mo_id, host_retrieve_v_storage_object_state_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_retrieve_v_storage_object_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_retrieve_v_storage_object_state_request_type** | [**HostRetrieveVStorageObjectStateRequestType**](HostRetrieveVStorageObjectStateRequestType.md)|  | 

### Return type

[**VStorageObjectStateInfo**](VStorageObjectStateInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The required virtual storage object state.  |  -  |
**500** | ***FileFault***: If an error occurs when retrieving the virtual object state.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory**
> host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory(mo_id, host_schedule_reconcile_datastore_inventory_request_type)

Schedules reconcile of the datastore inventory info of virtual storage objects. 

Schedules reconcile of the datastore inventory info of virtual storage objects.  This method just schedules the reconcile operation for the nearby future and returns. Note that since the reconcile operation will be executed after this method already returns the success of this method should not be considered as success of the actual reconcile operation.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_schedule_reconcile_datastore_inventory_request_type import HostScheduleReconcileDatastoreInventoryRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_schedule_reconcile_datastore_inventory_request_type = vmware_vi.HostScheduleReconcileDatastoreInventoryRequestType() # HostScheduleReconcileDatastoreInventoryRequestType | 

    try:
        # Schedules reconcile of the datastore inventory info of virtual storage objects. 
        api_instance.host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory(mo_id, host_schedule_reconcile_datastore_inventory_request_type)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_schedule_reconcile_datastore_inventory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_schedule_reconcile_datastore_inventory_request_type** | [**HostScheduleReconcileDatastoreInventoryRequestType**](HostScheduleReconcileDatastoreInventoryRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_set_v_storage_object_control_flags**
> host_v_storage_object_manager_host_set_v_storage_object_control_flags(mo_id, host_set_v_storage_object_control_flags_request_type)

Set control flags on VStorageObject. 

Set control flags on VStorageObject.  The control flags are defined in *vslmVStorageObjectControlFlag_enum*.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_set_v_storage_object_control_flags_request_type import HostSetVStorageObjectControlFlagsRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_set_v_storage_object_control_flags_request_type = vmware_vi.HostSetVStorageObjectControlFlagsRequestType() # HostSetVStorageObjectControlFlagsRequestType | 

    try:
        # Set control flags on VStorageObject. 
        api_instance.host_v_storage_object_manager_host_set_v_storage_object_control_flags(mo_id, host_set_v_storage_object_control_flags_request_type)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_set_v_storage_object_control_flags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_set_v_storage_object_control_flags_request_type** | [**HostSetVStorageObjectControlFlagsRequestType**](HostSetVStorageObjectControlFlagsRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk. The disk may be consumed.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task**
> ManagedObjectReference host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task(mo_id, host_update_v_storage_object_metadata_ex_request_type)

Update metadata KV pairs to a virtual storage object. 

Update metadata KV pairs to a virtual storage object.  And this API is by design supposed to be used for all of the addition, modification and deletion operations of metadata KV pairs.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 7.0.2.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_update_v_storage_object_metadata_ex_request_type import HostUpdateVStorageObjectMetadataExRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_update_v_storage_object_metadata_ex_request_type = vmware_vi.HostUpdateVStorageObjectMetadataExRequestType() # HostUpdateVStorageObjectMetadataExRequestType | 

    try:
        # Update metadata KV pairs to a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task(mo_id, host_update_v_storage_object_metadata_ex_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_update_v_storage_object_metadata_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_update_v_storage_object_metadata_ex_request_type** | [**HostUpdateVStorageObjectMetadataExRequestType**](HostUpdateVStorageObjectMetadataExRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or inaccessible.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_update_v_storage_object_metadata_task**
> ManagedObjectReference host_v_storage_object_manager_host_update_v_storage_object_metadata_task(mo_id, host_update_v_storage_object_metadata_request_type)

Update metadata KV pairs to a virtual storage object. 

Update metadata KV pairs to a virtual storage object.  And this API is by design supposed to be used for all of the addition, modification and deletion operations of metadata KV pairs.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_update_v_storage_object_metadata_request_type import HostUpdateVStorageObjectMetadataRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_update_v_storage_object_metadata_request_type = vmware_vi.HostUpdateVStorageObjectMetadataRequestType() # HostUpdateVStorageObjectMetadataRequestType | 

    try:
        # Update metadata KV pairs to a virtual storage object. 
        api_response = api_instance.host_v_storage_object_manager_host_update_v_storage_object_metadata_task(mo_id, host_update_v_storage_object_metadata_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_update_v_storage_object_metadata_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_update_v_storage_object_metadata_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_update_v_storage_object_metadata_request_type** | [**HostUpdateVStorageObjectMetadataRequestType**](HostUpdateVStorageObjectMetadataRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or inaccessible.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task**
> ManagedObjectReference host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task(mo_id, host_v_storage_object_create_disk_from_snapshot_request_type)

Creates a new Disk from given snapshot of a VStorageObject. 

Creates a new Disk from given snapshot of a VStorageObject.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_storage_object_create_disk_from_snapshot_request_type import HostVStorageObjectCreateDiskFromSnapshotRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_v_storage_object_create_disk_from_snapshot_request_type = vmware_vi.HostVStorageObjectCreateDiskFromSnapshotRequestType() # HostVStorageObjectCreateDiskFromSnapshotRequestType | 

    try:
        # Creates a new Disk from given snapshot of a VStorageObject. 
        api_response = api_instance.host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task(mo_id, host_v_storage_object_create_disk_from_snapshot_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_create_disk_from_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_v_storage_object_create_disk_from_snapshot_request_type** | [**HostVStorageObjectCreateDiskFromSnapshotRequestType**](HostVStorageObjectCreateDiskFromSnapshotRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while snapshotting the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_v_storage_object_create_snapshot_task**
> ManagedObjectReference host_v_storage_object_manager_host_v_storage_object_create_snapshot_task(mo_id, host_v_storage_object_create_snapshot_request_type)

Creates a snapshot of a given VStorageObject. 

Creates a snapshot of a given VStorageObject.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_storage_object_create_snapshot_request_type import HostVStorageObjectCreateSnapshotRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_v_storage_object_create_snapshot_request_type = vmware_vi.HostVStorageObjectCreateSnapshotRequestType() # HostVStorageObjectCreateSnapshotRequestType | 

    try:
        # Creates a snapshot of a given VStorageObject. 
        api_response = api_instance.host_v_storage_object_manager_host_v_storage_object_create_snapshot_task(mo_id, host_v_storage_object_create_snapshot_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_create_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_create_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_v_storage_object_create_snapshot_request_type** | [**HostVStorageObjectCreateSnapshotRequestType**](HostVStorageObjectCreateSnapshotRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while snapshotting the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task**
> ManagedObjectReference host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task(mo_id, host_v_storage_object_delete_snapshot_request_type)

Deletes a given snapshot of a VStorageObject. 

Deletes a given snapshot of a VStorageObject.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_storage_object_delete_snapshot_request_type import HostVStorageObjectDeleteSnapshotRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_v_storage_object_delete_snapshot_request_type = vmware_vi.HostVStorageObjectDeleteSnapshotRequestType() # HostVStorageObjectDeleteSnapshotRequestType | 

    try:
        # Deletes a given snapshot of a VStorageObject. 
        api_response = api_instance.host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task(mo_id, host_v_storage_object_delete_snapshot_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_delete_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_v_storage_object_delete_snapshot_request_type** | [**HostVStorageObjectDeleteSnapshotRequestType**](HostVStorageObjectDeleteSnapshotRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while snapshotting the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info**
> VStorageObjectSnapshotInfo host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info(mo_id, host_v_storage_object_retrieve_snapshot_info_request_type)

Retrieves snapshot information of a given VStorageObject. 

Retrieves snapshot information of a given VStorageObject.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_storage_object_retrieve_snapshot_info_request_type import HostVStorageObjectRetrieveSnapshotInfoRequestType
from vmware_vi.models.v_storage_object_snapshot_info import VStorageObjectSnapshotInfo
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_v_storage_object_retrieve_snapshot_info_request_type = vmware_vi.HostVStorageObjectRetrieveSnapshotInfoRequestType() # HostVStorageObjectRetrieveSnapshotInfoRequestType | 

    try:
        # Retrieves snapshot information of a given VStorageObject. 
        api_response = api_instance.host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info(mo_id, host_v_storage_object_retrieve_snapshot_info_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_retrieve_snapshot_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_v_storage_object_retrieve_snapshot_info_request_type** | [**HostVStorageObjectRetrieveSnapshotInfoRequestType**](HostVStorageObjectRetrieveSnapshotInfoRequestType.md)|  | 

### Return type

[**VStorageObjectSnapshotInfo**](VStorageObjectSnapshotInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***FileFault***: If an error occurs while snapshotting the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_v_storage_object_manager_host_v_storage_object_revert_task**
> ManagedObjectReference host_v_storage_object_manager_host_v_storage_object_revert_task(mo_id, host_v_storage_object_revert_request_type)

Reverts to a given snapshot of a VStorageObject. 

Reverts to a given snapshot of a VStorageObject.  This operation is supported on detached VirtualDisks During revert all the snapshots which were taken after the specified snapshot would get deleted.  E.g. Consider Disk with 4 snapshots  BaseDisk -&gt; Snap-2 -&gt; Snap-3 -&gt; Snap-4 -&gt; Running-Point  If user chooses to revert to snap-2 then snap-4 and snap-3 would also be deleted. After revert operation disk would have below configuration:  BaseDisk -&gt; Snap-2 -&gt; Running-Point  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_v_storage_object_revert_request_type import HostVStorageObjectRevertRequestType
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
    api_instance = vmware_vi.HostVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    host_v_storage_object_revert_request_type = vmware_vi.HostVStorageObjectRevertRequestType() # HostVStorageObjectRevertRequestType | 

    try:
        # Reverts to a given snapshot of a VStorageObject. 
        api_response = api_instance.host_v_storage_object_manager_host_v_storage_object_revert_task(mo_id, host_v_storage_object_revert_request_type)
        print("The response of HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_revert_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostVStorageObjectManagerApi->host_v_storage_object_manager_host_v_storage_object_revert_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **host_v_storage_object_revert_request_type** | [**HostVStorageObjectRevertRequestType**](HostVStorageObjectRevertRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while snapshotting the virtual storage object.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

