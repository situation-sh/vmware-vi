# vmware_vi.VcenterVStorageObjectManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vcenter_v_storage_object_manager_attach_tag_to_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_attach_tag_to_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/AttachTagToVStorageObject | Attach a tag to a virtual storage object. 
[**vcenter_v_storage_object_manager_clear_v_storage_object_control_flags**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_clear_v_storage_object_control_flags) | **POST** /VcenterVStorageObjectManager/{moId}/ClearVStorageObjectControlFlags | Clear control flags on VStorageObject. 
[**vcenter_v_storage_object_manager_clone_v_storage_object_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_clone_v_storage_object_task) | **POST** /VcenterVStorageObjectManager/{moId}/CloneVStorageObject_Task | Clone a virtual storage object. 
[**vcenter_v_storage_object_manager_create_disk_from_snapshot_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_create_disk_from_snapshot_task) | **POST** /VcenterVStorageObjectManager/{moId}/CreateDiskFromSnapshot_Task | Creates a new Disk from given snapshot of a VStorageObject. 
[**vcenter_v_storage_object_manager_create_disk_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_create_disk_task) | **POST** /VcenterVStorageObjectManager/{moId}/CreateDisk_Task | Create a virtual disk, which is a storage object with *disk* as consumption type. 
[**vcenter_v_storage_object_manager_delete_snapshot_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_delete_snapshot_task) | **POST** /VcenterVStorageObjectManager/{moId}/DeleteSnapshot_Task | Deletes a given snapshot of a VStorageObject. 
[**vcenter_v_storage_object_manager_delete_v_storage_object_ex_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_delete_v_storage_object_ex_task) | **POST** /VcenterVStorageObjectManager/{moId}/DeleteVStorageObjectEx_Task | Delete a virtual storage object and its associated backings. 
[**vcenter_v_storage_object_manager_delete_v_storage_object_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_delete_v_storage_object_task) | **POST** /VcenterVStorageObjectManager/{moId}/DeleteVStorageObject_Task | Delete a virtual storage object and its associated backings. 
[**vcenter_v_storage_object_manager_detach_tag_from_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_detach_tag_from_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/DetachTagFromVStorageObject | Detach a tag from a virtual storage object. 
[**vcenter_v_storage_object_manager_extend_disk_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_extend_disk_task) | **POST** /VcenterVStorageObjectManager/{moId}/ExtendDisk_Task | Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 
[**vcenter_v_storage_object_manager_inflate_disk_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_inflate_disk_task) | **POST** /VcenterVStorageObjectManager/{moId}/InflateDisk_Task | Inflate a sparse or thin-provisioned virtual disk up to the full size. 
[**vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/ListTagsAttachedToVStorageObject | Lists all tags attached to virtual storage object. 
[**vcenter_v_storage_object_manager_list_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_list_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/ListVStorageObject | List all virtual storage objects located on a datastore. 
[**vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag) | **POST** /VcenterVStorageObjectManager/{moId}/ListVStorageObjectsAttachedToTag | Lists all virtual storage objects attached to the tag. 
[**vcenter_v_storage_object_manager_reconcile_datastore_inventory_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_reconcile_datastore_inventory_task) | **POST** /VcenterVStorageObjectManager/{moId}/ReconcileDatastoreInventory_Task | Reconcile the datastore inventory info of virtual storage objects. 
[**vcenter_v_storage_object_manager_register_disk**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_register_disk) | **POST** /VcenterVStorageObjectManager/{moId}/RegisterDisk | Promote a virtual disk to a First Class Disk. 
[**vcenter_v_storage_object_manager_relocate_v_storage_object_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_relocate_v_storage_object_task) | **POST** /VcenterVStorageObjectManager/{moId}/RelocateVStorageObject_Task | Relocate a virtual storage object. 
[**vcenter_v_storage_object_manager_rename_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_rename_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/RenameVStorageObject | Rename a virtual storage object. 
[**vcenter_v_storage_object_manager_retrieve_snapshot_details**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_snapshot_details) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveSnapshotDetails | Retrieves snapshot disk details of a given snapshot. 
[**vcenter_v_storage_object_manager_retrieve_snapshot_info**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_snapshot_info) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveSnapshotInfo | Retrieves snapshot information of a given VStorageObject. 
[**vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveVStorageInfrastructureObjectPolicy | Retrieve virtual storage infrastructure object SBPM policy on given datastore. 
[**vcenter_v_storage_object_manager_retrieve_v_storage_object**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_v_storage_object) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveVStorageObject | Retrieve a virtual storage object. 
[**vcenter_v_storage_object_manager_retrieve_v_storage_object_associations**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_v_storage_object_associations) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveVStorageObjectAssociations | Retrieve vm associations for each virtual storage object in the query. 
[**vcenter_v_storage_object_manager_retrieve_v_storage_object_state**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_retrieve_v_storage_object_state) | **POST** /VcenterVStorageObjectManager/{moId}/RetrieveVStorageObjectState | Retrieve a virtual storage object state. 
[**vcenter_v_storage_object_manager_revert_v_storage_object_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_revert_v_storage_object_task) | **POST** /VcenterVStorageObjectManager/{moId}/RevertVStorageObject_Task | Reverts to a given snapshot of a VStorageObject. 
[**vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory) | **POST** /VcenterVStorageObjectManager/{moId}/ScheduleReconcileDatastoreInventory | Schedules reconcile of the inventory info of virtual storage objects on one of the hosts that is connected with the datastore. 
[**vcenter_v_storage_object_manager_set_v_storage_object_control_flags**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_set_v_storage_object_control_flags) | **POST** /VcenterVStorageObjectManager/{moId}/SetVStorageObjectControlFlags | Set control flags on VStorageObject. 
[**vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task) | **POST** /VcenterVStorageObjectManager/{moId}/UpdateVStorageInfrastructureObjectPolicy_Task | Assigns specified SBPM policy to the given virtual storage infrastructure object. 
[**vcenter_v_storage_object_manager_update_v_storage_object_crypto_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_update_v_storage_object_crypto_task) | **POST** /VcenterVStorageObjectManager/{moId}/UpdateVStorageObjectCrypto_Task | Update the crypto on a virtual storage object. 
[**vcenter_v_storage_object_manager_update_v_storage_object_policy_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_update_v_storage_object_policy_task) | **POST** /VcenterVStorageObjectManager/{moId}/UpdateVStorageObjectPolicy_Task | Update the storage policy on a virtual storage object. 
[**vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task) | **POST** /VcenterVStorageObjectManager/{moId}/VCenterUpdateVStorageObjectMetadataEx_Task | Update metadata KV pairs to a virtual storage object and returns the corresponding vclock upon success. 
[**vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task) | **POST** /VcenterVStorageObjectManager/{moId}/VStorageObjectCreateSnapshot_Task | Creates a snapshot of a given VStorageObject. 
[**vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas**](VcenterVStorageObjectManagerApi.md#vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas) | **POST** /VcenterVStorageObjectManager/{moId}/VstorageObjectVCenterQueryChangedDiskAreas | Get a list of areas of a virtual disk that have been modified since a well-defined point in the past. 


# **vcenter_v_storage_object_manager_attach_tag_to_v_storage_object**
> vcenter_v_storage_object_manager_attach_tag_to_v_storage_object(mo_id, attach_tag_to_v_storage_object_request_type)

Attach a tag to a virtual storage object. 

Attach a tag to a virtual storage object.  Requires privilege InventoryService.Tagging.AttachTag on root folder  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.attach_tag_to_v_storage_object_request_type import AttachTagToVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    attach_tag_to_v_storage_object_request_type = vmware_vi.AttachTagToVStorageObjectRequestType() # AttachTagToVStorageObjectRequestType | 

    try:
        # Attach a tag to a virtual storage object. 
        api_instance.vcenter_v_storage_object_manager_attach_tag_to_v_storage_object(mo_id, attach_tag_to_v_storage_object_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_attach_tag_to_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **attach_tag_to_v_storage_object_request_type** | [**AttachTagToVStorageObjectRequestType**](AttachTagToVStorageObjectRequestType.md)|  | 

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
**500** | ***NotFound***: If the specified category or tag cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_clear_v_storage_object_control_flags**
> vcenter_v_storage_object_manager_clear_v_storage_object_control_flags(mo_id, clear_v_storage_object_control_flags_request_type)

Clear control flags on VStorageObject. 

Clear control flags on VStorageObject.  The control flags are defined in *vslmVStorageObjectControlFlag_enum*.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clear_v_storage_object_control_flags_request_type import ClearVStorageObjectControlFlagsRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clear_v_storage_object_control_flags_request_type = vmware_vi.ClearVStorageObjectControlFlagsRequestType() # ClearVStorageObjectControlFlagsRequestType | 

    try:
        # Clear control flags on VStorageObject. 
        api_instance.vcenter_v_storage_object_manager_clear_v_storage_object_control_flags(mo_id, clear_v_storage_object_control_flags_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_clear_v_storage_object_control_flags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clear_v_storage_object_control_flags_request_type** | [**ClearVStorageObjectControlFlagsRequestType**](ClearVStorageObjectControlFlagsRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_clone_v_storage_object_task**
> ManagedObjectReference vcenter_v_storage_object_manager_clone_v_storage_object_task(mo_id, clone_v_storage_object_request_type)

Clone a virtual storage object. 

Clone a virtual storage object.  Requires Datastore.FileManagement privilege on both source and destination datastore.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clone_v_storage_object_request_type import CloneVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clone_v_storage_object_request_type = vmware_vi.CloneVStorageObjectRequestType() # CloneVStorageObjectRequestType | 

    try:
        # Clone a virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_clone_v_storage_object_task(mo_id, clone_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_clone_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_clone_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clone_v_storage_object_request_type** | [**CloneVStorageObjectRequestType**](CloneVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_create_disk_from_snapshot_task**
> ManagedObjectReference vcenter_v_storage_object_manager_create_disk_from_snapshot_task(mo_id, create_disk_from_snapshot_request_type)

Creates a new Disk from given snapshot of a VStorageObject. 

Creates a new Disk from given snapshot of a VStorageObject.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_disk_from_snapshot_request_type import CreateDiskFromSnapshotRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_disk_from_snapshot_request_type = vmware_vi.CreateDiskFromSnapshotRequestType() # CreateDiskFromSnapshotRequestType | 

    try:
        # Creates a new Disk from given snapshot of a VStorageObject. 
        api_response = api_instance.vcenter_v_storage_object_manager_create_disk_from_snapshot_task(mo_id, create_disk_from_snapshot_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_create_disk_from_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_create_disk_from_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_disk_from_snapshot_request_type** | [**CreateDiskFromSnapshotRequestType**](CreateDiskFromSnapshotRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_create_disk_task**
> ManagedObjectReference vcenter_v_storage_object_manager_create_disk_task(mo_id, create_disk_request_type)

Create a virtual disk, which is a storage object with *disk* as consumption type. 

Create a virtual disk, which is a storage object with *disk* as consumption type.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk object is created.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_disk_request_type import CreateDiskRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_disk_request_type = vmware_vi.CreateDiskRequestType() # CreateDiskRequestType | 

    try:
        # Create a virtual disk, which is a storage object with *disk* as consumption type. 
        api_response = api_instance.vcenter_v_storage_object_manager_create_disk_task(mo_id, create_disk_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_create_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_create_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_disk_request_type** | [**CreateDiskRequestType**](CreateDiskRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor monitor the operation. The *info.result* property in the *Task* contains the newly created *VStorageObject* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***FileFault***: If an error occurs when creating the virtual disk.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_delete_snapshot_task**
> ManagedObjectReference vcenter_v_storage_object_manager_delete_snapshot_task(mo_id, delete_snapshot_request_type)

Deletes a given snapshot of a VStorageObject. 

Deletes a given snapshot of a VStorageObject.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_snapshot_request_type import DeleteSnapshotRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_snapshot_request_type = vmware_vi.DeleteSnapshotRequestType() # DeleteSnapshotRequestType | 

    try:
        # Deletes a given snapshot of a VStorageObject. 
        api_response = api_instance.vcenter_v_storage_object_manager_delete_snapshot_task(mo_id, delete_snapshot_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_snapshot_request_type** | [**DeleteSnapshotRequestType**](DeleteSnapshotRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_delete_v_storage_object_ex_task**
> ManagedObjectReference vcenter_v_storage_object_manager_delete_v_storage_object_ex_task(mo_id, delete_v_storage_object_ex_request_type)

Delete a virtual storage object and its associated backings. 

Delete a virtual storage object and its associated backings.  Returns the corresponding vclock upon succeess.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 7.0.2.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_v_storage_object_ex_request_type import DeleteVStorageObjectExRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_v_storage_object_ex_request_type = vmware_vi.DeleteVStorageObjectExRequestType() # DeleteVStorageObjectExRequestType | 

    try:
        # Delete a virtual storage object and its associated backings. 
        api_response = api_instance.vcenter_v_storage_object_manager_delete_v_storage_object_ex_task(mo_id, delete_v_storage_object_ex_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_v_storage_object_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_v_storage_object_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_v_storage_object_ex_request_type** | [**DeleteVStorageObjectExRequestType**](DeleteVStorageObjectExRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_delete_v_storage_object_task**
> ManagedObjectReference vcenter_v_storage_object_manager_delete_v_storage_object_task(mo_id, delete_v_storage_object_request_type)

Delete a virtual storage object and its associated backings. 

Delete a virtual storage object and its associated backings.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_v_storage_object_request_type import DeleteVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_v_storage_object_request_type = vmware_vi.DeleteVStorageObjectRequestType() # DeleteVStorageObjectRequestType | 

    try:
        # Delete a virtual storage object and its associated backings. 
        api_response = api_instance.vcenter_v_storage_object_manager_delete_v_storage_object_task(mo_id, delete_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_delete_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_v_storage_object_request_type** | [**DeleteVStorageObjectRequestType**](DeleteVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_detach_tag_from_v_storage_object**
> vcenter_v_storage_object_manager_detach_tag_from_v_storage_object(mo_id, detach_tag_from_v_storage_object_request_type)

Detach a tag from a virtual storage object. 

Detach a tag from a virtual storage object.  Requires privilege InventoryService.Tagging.AttachTag on root folder  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.detach_tag_from_v_storage_object_request_type import DetachTagFromVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    detach_tag_from_v_storage_object_request_type = vmware_vi.DetachTagFromVStorageObjectRequestType() # DetachTagFromVStorageObjectRequestType | 

    try:
        # Detach a tag from a virtual storage object. 
        api_instance.vcenter_v_storage_object_manager_detach_tag_from_v_storage_object(mo_id, detach_tag_from_v_storage_object_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_detach_tag_from_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **detach_tag_from_v_storage_object_request_type** | [**DetachTagFromVStorageObjectRequestType**](DetachTagFromVStorageObjectRequestType.md)|  | 

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
**500** | ***NotFound***: If the specified category or tag cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_extend_disk_task**
> ManagedObjectReference vcenter_v_storage_object_manager_extend_disk_task(mo_id, extend_disk_request_type)

Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 

Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity.  If new capacity is smaller than current disk capacity, then operation fails due to invalid capacity. If new capacity is greater than current disk capacity, then operation proceeds. If new capacity is equal to current disk ccapcity, then operation succeeds without any actual extension. The extended disk region will be the same as the original disk: \\- For a zerothick disk, the extended disk region will be zeroedthick. \\- For an eagerzerothick disk, the extended disk region will be eagerzeroedthick \\- A thin-provisioned disk will always be extended as a thin-provisioned disk.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extend_disk_request_type import ExtendDiskRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    extend_disk_request_type = vmware_vi.ExtendDiskRequestType() # ExtendDiskRequestType | 

    try:
        # Expand the capacity of a virtual disk, which is a storage object with *disk*, to the new capacity. 
        api_response = api_instance.vcenter_v_storage_object_manager_extend_disk_task(mo_id, extend_disk_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_extend_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_extend_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **extend_disk_request_type** | [**ExtendDiskRequestType**](ExtendDiskRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_inflate_disk_task**
> ManagedObjectReference vcenter_v_storage_object_manager_inflate_disk_task(mo_id, inflate_disk_request_type)

Inflate a sparse or thin-provisioned virtual disk up to the full size. 

Inflate a sparse or thin-provisioned virtual disk up to the full size.  Additional space allocated to the disk as a result of this operation will be filled with zeros.  Currently inflateDisk API only supports the following combinations: Valid provisioning type: THIN; Valid Datastore: VMFS, NFS. Inflating a disk is not applicable for VVol/VSAN datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.inflate_disk_request_type import InflateDiskRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    inflate_disk_request_type = vmware_vi.InflateDiskRequestType() # InflateDiskRequestType | 

    try:
        # Inflate a sparse or thin-provisioned virtual disk up to the full size. 
        api_response = api_instance.vcenter_v_storage_object_manager_inflate_disk_task(mo_id, inflate_disk_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_inflate_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_inflate_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **inflate_disk_request_type** | [**InflateDiskRequestType**](InflateDiskRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object**
> List[VslmTagEntry] vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object(mo_id, list_tags_attached_to_v_storage_object_request_type)

Lists all tags attached to virtual storage object. 

Lists all tags attached to virtual storage object.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.list_tags_attached_to_v_storage_object_request_type import ListTagsAttachedToVStorageObjectRequestType
from vmware_vi.models.vslm_tag_entry import VslmTagEntry
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_tags_attached_to_v_storage_object_request_type = vmware_vi.ListTagsAttachedToVStorageObjectRequestType() # ListTagsAttachedToVStorageObjectRequestType | 

    try:
        # Lists all tags attached to virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object(mo_id, list_tags_attached_to_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_tags_attached_to_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_tags_attached_to_v_storage_object_request_type** | [**ListTagsAttachedToVStorageObjectRequestType**](ListTagsAttachedToVStorageObjectRequestType.md)|  | 

### Return type

[**List[VslmTagEntry]**](VslmTagEntry.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Tag-association tuples associated with the virtual storage object.  |  -  |
**500** | ***NotFound***: If the specified category or tag cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_list_v_storage_object**
> List[ID] vcenter_v_storage_object_manager_list_v_storage_object(mo_id, list_v_storage_object_request_type)

List all virtual storage objects located on a datastore. 

List all virtual storage objects located on a datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.id import ID
from vmware_vi.models.list_v_storage_object_request_type import ListVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_v_storage_object_request_type = vmware_vi.ListVStorageObjectRequestType() # ListVStorageObjectRequestType | 

    try:
        # List all virtual storage objects located on a datastore. 
        api_response = api_instance.vcenter_v_storage_object_manager_list_v_storage_object(mo_id, list_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_v_storage_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_v_storage_object_request_type** | [**ListVStorageObjectRequestType**](ListVStorageObjectRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or is inaccessible.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag**
> List[ID] vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag(mo_id, list_v_storage_objects_attached_to_tag_request_type)

Lists all virtual storage objects attached to the tag. 

Lists all virtual storage objects attached to the tag.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.id import ID
from vmware_vi.models.list_v_storage_objects_attached_to_tag_request_type import ListVStorageObjectsAttachedToTagRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    list_v_storage_objects_attached_to_tag_request_type = vmware_vi.ListVStorageObjectsAttachedToTagRequestType() # ListVStorageObjectsAttachedToTagRequestType | 

    try:
        # Lists all virtual storage objects attached to the tag. 
        api_response = api_instance.vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag(mo_id, list_v_storage_objects_attached_to_tag_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_list_v_storage_objects_attached_to_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **list_v_storage_objects_attached_to_tag_request_type** | [**ListVStorageObjectsAttachedToTagRequestType**](ListVStorageObjectsAttachedToTagRequestType.md)|  | 

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
**200** | The list of IDs of the virtual storage objects.  |  -  |
**500** | ***NotFound***: If the specified category or tag cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_reconcile_datastore_inventory_task**
> ManagedObjectReference vcenter_v_storage_object_manager_reconcile_datastore_inventory_task(mo_id, reconcile_datastore_inventory_request_type)

Reconcile the datastore inventory info of virtual storage objects. 

Reconcile the datastore inventory info of virtual storage objects.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconcile_datastore_inventory_request_type import ReconcileDatastoreInventoryRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconcile_datastore_inventory_request_type = vmware_vi.ReconcileDatastoreInventoryRequestType() # ReconcileDatastoreInventoryRequestType | 

    try:
        # Reconcile the datastore inventory info of virtual storage objects. 
        api_response = api_instance.vcenter_v_storage_object_manager_reconcile_datastore_inventory_task(mo_id, reconcile_datastore_inventory_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_reconcile_datastore_inventory_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_reconcile_datastore_inventory_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconcile_datastore_inventory_request_type** | [**ReconcileDatastoreInventoryRequestType**](ReconcileDatastoreInventoryRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_register_disk**
> VStorageObject vcenter_v_storage_object_manager_register_disk(mo_id, register_disk_request_type)

Promote a virtual disk to a First Class Disk. 

Promote a virtual disk to a First Class Disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.register_disk_request_type import RegisterDiskRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    register_disk_request_type = vmware_vi.RegisterDiskRequestType() # RegisterDiskRequestType | 

    try:
        # Promote a virtual disk to a First Class Disk. 
        api_response = api_instance.vcenter_v_storage_object_manager_register_disk(mo_id, register_disk_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_register_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_register_disk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **register_disk_request_type** | [**RegisterDiskRequestType**](RegisterDiskRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_relocate_v_storage_object_task**
> ManagedObjectReference vcenter_v_storage_object_manager_relocate_v_storage_object_task(mo_id, relocate_v_storage_object_request_type)

Relocate a virtual storage object. 

Relocate a virtual storage object.  Requires Datastore.FileManagement privilege on both source and destination datastore.  Supports only detached virtual storage object. Requires a host that has access to both source and destination datastores.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.relocate_v_storage_object_request_type import RelocateVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    relocate_v_storage_object_request_type = vmware_vi.RelocateVStorageObjectRequestType() # RelocateVStorageObjectRequestType | 

    try:
        # Relocate a virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_relocate_v_storage_object_task(mo_id, relocate_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_relocate_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_relocate_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **relocate_v_storage_object_request_type** | [**RelocateVStorageObjectRequestType**](RelocateVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_rename_v_storage_object**
> vcenter_v_storage_object_manager_rename_v_storage_object(mo_id, rename_v_storage_object_request_type)

Rename a virtual storage object. 

Rename a virtual storage object.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.rename_v_storage_object_request_type import RenameVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_v_storage_object_request_type = vmware_vi.RenameVStorageObjectRequestType() # RenameVStorageObjectRequestType | 

    try:
        # Rename a virtual storage object. 
        api_instance.vcenter_v_storage_object_manager_rename_v_storage_object(mo_id, rename_v_storage_object_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_rename_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_v_storage_object_request_type** | [**RenameVStorageObjectRequestType**](RenameVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_retrieve_snapshot_details**
> VStorageObjectSnapshotDetails vcenter_v_storage_object_manager_retrieve_snapshot_details(mo_id, retrieve_snapshot_details_request_type)

Retrieves snapshot disk details of a given snapshot. 

Retrieves snapshot disk details of a given snapshot.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_snapshot_details_request_type import RetrieveSnapshotDetailsRequestType
from vmware_vi.models.v_storage_object_snapshot_details import VStorageObjectSnapshotDetails
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_snapshot_details_request_type = vmware_vi.RetrieveSnapshotDetailsRequestType() # RetrieveSnapshotDetailsRequestType | 

    try:
        # Retrieves snapshot disk details of a given snapshot. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_snapshot_details(mo_id, retrieve_snapshot_details_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_snapshot_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_snapshot_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_snapshot_details_request_type** | [**RetrieveSnapshotDetailsRequestType**](RetrieveSnapshotDetailsRequestType.md)|  | 

### Return type

[**VStorageObjectSnapshotDetails**](VStorageObjectSnapshotDetails.md)

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

# **vcenter_v_storage_object_manager_retrieve_snapshot_info**
> VStorageObjectSnapshotInfo vcenter_v_storage_object_manager_retrieve_snapshot_info(mo_id, retrieve_snapshot_info_request_type)

Retrieves snapshot information of a given VStorageObject. 

Retrieves snapshot information of a given VStorageObject.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_snapshot_info_request_type import RetrieveSnapshotInfoRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_snapshot_info_request_type = vmware_vi.RetrieveSnapshotInfoRequestType() # RetrieveSnapshotInfoRequestType | 

    try:
        # Retrieves snapshot information of a given VStorageObject. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_snapshot_info(mo_id, retrieve_snapshot_info_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_snapshot_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_snapshot_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_snapshot_info_request_type** | [**RetrieveSnapshotInfoRequestType**](RetrieveSnapshotInfoRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy**
> List[VslmInfrastructureObjectPolicy] vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy(mo_id, retrieve_v_storage_infrastructure_object_policy_request_type)

Retrieve virtual storage infrastructure object SBPM policy on given datastore. 

Retrieve virtual storage infrastructure object SBPM policy on given datastore.  Only support VSAN datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage infrastructure object is located.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_v_storage_infrastructure_object_policy_request_type import RetrieveVStorageInfrastructureObjectPolicyRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_v_storage_infrastructure_object_policy_request_type = vmware_vi.RetrieveVStorageInfrastructureObjectPolicyRequestType() # RetrieveVStorageInfrastructureObjectPolicyRequestType | 

    try:
        # Retrieve virtual storage infrastructure object SBPM policy on given datastore. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy(mo_id, retrieve_v_storage_infrastructure_object_policy_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_infrastructure_object_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_v_storage_infrastructure_object_policy_request_type** | [**RetrieveVStorageInfrastructureObjectPolicyRequestType**](RetrieveVStorageInfrastructureObjectPolicyRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_retrieve_v_storage_object**
> VStorageObject vcenter_v_storage_object_manager_retrieve_v_storage_object(mo_id, retrieve_v_storage_object_request_type)

Retrieve a virtual storage object. 

Retrieve a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_v_storage_object_request_type import RetrieveVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_v_storage_object_request_type = vmware_vi.RetrieveVStorageObjectRequestType() # RetrieveVStorageObjectRequestType | 

    try:
        # Retrieve a virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_v_storage_object(mo_id, retrieve_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_v_storage_object_request_type** | [**RetrieveVStorageObjectRequestType**](RetrieveVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_retrieve_v_storage_object_associations**
> List[VStorageObjectAssociations] vcenter_v_storage_object_manager_retrieve_v_storage_object_associations(mo_id, retrieve_v_storage_object_associations_request_type)

Retrieve vm associations for each virtual storage object in the query. 

Retrieve vm associations for each virtual storage object in the query.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_v_storage_object_associations_request_type import RetrieveVStorageObjectAssociationsRequestType
from vmware_vi.models.v_storage_object_associations import VStorageObjectAssociations
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_v_storage_object_associations_request_type = vmware_vi.RetrieveVStorageObjectAssociationsRequestType() # RetrieveVStorageObjectAssociationsRequestType | 

    try:
        # Retrieve vm associations for each virtual storage object in the query. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_v_storage_object_associations(mo_id, retrieve_v_storage_object_associations_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_v_storage_object_associations_request_type** | [**RetrieveVStorageObjectAssociationsRequestType**](RetrieveVStorageObjectAssociationsRequestType.md)|  | 

### Return type

[**List[VStorageObjectAssociations]**](VStorageObjectAssociations.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of VStorageObjectVmAssociations which provides virtual storage object id to vm associations mapping.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_retrieve_v_storage_object_state**
> VStorageObjectStateInfo vcenter_v_storage_object_manager_retrieve_v_storage_object_state(mo_id, retrieve_v_storage_object_state_request_type)

Retrieve a virtual storage object state. 

Retrieve a virtual storage object state.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.retrieve_v_storage_object_state_request_type import RetrieveVStorageObjectStateRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_v_storage_object_state_request_type = vmware_vi.RetrieveVStorageObjectStateRequestType() # RetrieveVStorageObjectStateRequestType | 

    try:
        # Retrieve a virtual storage object state. 
        api_response = api_instance.vcenter_v_storage_object_manager_retrieve_v_storage_object_state(mo_id, retrieve_v_storage_object_state_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_retrieve_v_storage_object_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_v_storage_object_state_request_type** | [**RetrieveVStorageObjectStateRequestType**](RetrieveVStorageObjectStateRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_revert_v_storage_object_task**
> ManagedObjectReference vcenter_v_storage_object_manager_revert_v_storage_object_task(mo_id, revert_v_storage_object_request_type)

Reverts to a given snapshot of a VStorageObject. 

Reverts to a given snapshot of a VStorageObject.  This operation is supported on detached VirtualDisks During revert all the snapshots which were taken after the specified snapshot would get deleted.  E.g. Consider Disk with 4 snapshots  BaseDisk -&gt; Snap-2 -&gt; Snap-3 -&gt; Snap-4 -&gt; Running-Point  If user chooses to revert to snap-2 then snap-4 and snap-3 would also be deleted. After revert operation disk would have below configuration:  BaseDisk -&gt; Snap-2 -&gt; Running-Point  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.revert_v_storage_object_request_type import RevertVStorageObjectRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    revert_v_storage_object_request_type = vmware_vi.RevertVStorageObjectRequestType() # RevertVStorageObjectRequestType | 

    try:
        # Reverts to a given snapshot of a VStorageObject. 
        api_response = api_instance.vcenter_v_storage_object_manager_revert_v_storage_object_task(mo_id, revert_v_storage_object_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_revert_v_storage_object_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_revert_v_storage_object_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **revert_v_storage_object_request_type** | [**RevertVStorageObjectRequestType**](RevertVStorageObjectRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory**
> vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory(mo_id, schedule_reconcile_datastore_inventory_request_type)

Schedules reconcile of the inventory info of virtual storage objects on one of the hosts that is connected with the datastore. 

Schedules reconcile of the inventory info of virtual storage objects on one of the hosts that is connected with the datastore.  This method just schedules the reconcile operation for the nearby future and returns. Note that since the reconcile operation will be executed after this method already returns the success of this method should not be considered as success of the actual reconcile operation.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.schedule_reconcile_datastore_inventory_request_type import ScheduleReconcileDatastoreInventoryRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    schedule_reconcile_datastore_inventory_request_type = vmware_vi.ScheduleReconcileDatastoreInventoryRequestType() # ScheduleReconcileDatastoreInventoryRequestType | 

    try:
        # Schedules reconcile of the inventory info of virtual storage objects on one of the hosts that is connected with the datastore. 
        api_instance.vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory(mo_id, schedule_reconcile_datastore_inventory_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_schedule_reconcile_datastore_inventory: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **schedule_reconcile_datastore_inventory_request_type** | [**ScheduleReconcileDatastoreInventoryRequestType**](ScheduleReconcileDatastoreInventoryRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_set_v_storage_object_control_flags**
> vcenter_v_storage_object_manager_set_v_storage_object_control_flags(mo_id, set_v_storage_object_control_flags_request_type)

Set control flags on VStorageObject. 

Set control flags on VStorageObject.  The control flags are defined in *vslmVStorageObjectControlFlag_enum*.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_v_storage_object_control_flags_request_type import SetVStorageObjectControlFlagsRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_v_storage_object_control_flags_request_type = vmware_vi.SetVStorageObjectControlFlagsRequestType() # SetVStorageObjectControlFlagsRequestType | 

    try:
        # Set control flags on VStorageObject. 
        api_instance.vcenter_v_storage_object_manager_set_v_storage_object_control_flags(mo_id, set_v_storage_object_control_flags_request_type)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_set_v_storage_object_control_flags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_v_storage_object_control_flags_request_type** | [**SetVStorageObjectControlFlagsRequestType**](SetVStorageObjectControlFlagsRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task**
> ManagedObjectReference vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task(mo_id, update_v_storage_infrastructure_object_policy_request_type)

Assigns specified SBPM policy to the given virtual storage infrastructure object. 

Assigns specified SBPM policy to the given virtual storage infrastructure object.  Only support VSAN datastore.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage infrastructure object is located.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_v_storage_infrastructure_object_policy_request_type import UpdateVStorageInfrastructureObjectPolicyRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_v_storage_infrastructure_object_policy_request_type = vmware_vi.UpdateVStorageInfrastructureObjectPolicyRequestType() # UpdateVStorageInfrastructureObjectPolicyRequestType | 

    try:
        # Assigns specified SBPM policy to the given virtual storage infrastructure object. 
        api_response = api_instance.vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task(mo_id, update_v_storage_infrastructure_object_policy_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_infrastructure_object_policy_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_v_storage_infrastructure_object_policy_request_type** | [**UpdateVStorageInfrastructureObjectPolicyRequestType**](UpdateVStorageInfrastructureObjectPolicyRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***InvalidState***: If there is issue with profile spec.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_update_v_storage_object_crypto_task**
> ManagedObjectReference vcenter_v_storage_object_manager_update_v_storage_object_crypto_task(mo_id, update_v_storage_object_crypto_request_type)

Update the crypto on a virtual storage object. 

Update the crypto on a virtual storage object.  This is also intended for disk encryption, decryption and re-encryption. To encrypt the disk, profile must contain an encryption component. disksCrypto can be left as blank, which means caller doesn't care which key is used to encrypt the disk. If it's not blank, it has to be of type CryptoSpecEncrypt. To decrypt the disk, profile must not contain an encryption component. disksCrypto can be left as blank, if not, it has be of type CryptoSpecDecrypt. To re-encrypt the disk, profile must contain an encryption component. disksCrypto cannot be left as blank. It has to be of type either CryptoSpecShallowRecrypt or CryptoSpecDeepRecrypt.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 7.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_v_storage_object_crypto_request_type import UpdateVStorageObjectCryptoRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_v_storage_object_crypto_request_type = vmware_vi.UpdateVStorageObjectCryptoRequestType() # UpdateVStorageObjectCryptoRequestType | 

    try:
        # Update the crypto on a virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_update_v_storage_object_crypto_task(mo_id, update_v_storage_object_crypto_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_object_crypto_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_object_crypto_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_v_storage_object_crypto_request_type** | [**UpdateVStorageObjectCryptoRequestType**](UpdateVStorageObjectCryptoRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while updating the virtual storage object policy.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_update_v_storage_object_policy_task**
> ManagedObjectReference vcenter_v_storage_object_manager_update_v_storage_object_policy_task(mo_id, update_v_storage_object_policy_request_type)

Update the storage policy on a virtual storage object. 

Update the storage policy on a virtual storage object.  Requires Datastore.FileManagement privilege on the datastore where the virtual storage object is located.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.update_v_storage_object_policy_request_type import UpdateVStorageObjectPolicyRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_v_storage_object_policy_request_type = vmware_vi.UpdateVStorageObjectPolicyRequestType() # UpdateVStorageObjectPolicyRequestType | 

    try:
        # Update the storage policy on a virtual storage object. 
        api_response = api_instance.vcenter_v_storage_object_manager_update_v_storage_object_policy_task(mo_id, update_v_storage_object_policy_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_object_policy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_update_v_storage_object_policy_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_v_storage_object_policy_request_type** | [**UpdateVStorageObjectPolicyRequestType**](UpdateVStorageObjectPolicyRequestType.md)|  | 

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
**500** | ***FileFault***: If an error occurs while updating the virtual storage object policy.  ***NotFound***: If the specified virtual storage object cannot be found.  ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***TaskInProgress***: If the virtual storage object is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task**
> ManagedObjectReference vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task(mo_id, v_center_update_v_storage_object_metadata_ex_request_type)

Update metadata KV pairs to a virtual storage object and returns the corresponding vclock upon success. 

Update metadata KV pairs to a virtual storage object and returns the corresponding vclock upon success.  ***Since:*** vSphere API 7.0.2.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.v_center_update_v_storage_object_metadata_ex_request_type import VCenterUpdateVStorageObjectMetadataExRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    v_center_update_v_storage_object_metadata_ex_request_type = vmware_vi.VCenterUpdateVStorageObjectMetadataExRequestType() # VCenterUpdateVStorageObjectMetadataExRequestType | 

    try:
        # Update metadata KV pairs to a virtual storage object and returns the corresponding vclock upon success. 
        api_response = api_instance.vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task(mo_id, v_center_update_v_storage_object_metadata_ex_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_v_center_update_v_storage_object_metadata_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **v_center_update_v_storage_object_metadata_ex_request_type** | [**VCenterUpdateVStorageObjectMetadataExRequestType**](VCenterUpdateVStorageObjectMetadataExRequestType.md)|  | 

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
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore, such as datastore cannot be found or is inaccessible.  ***InvalidState***: If the operation cannot be performed on the disk.  ***NotFound***: If specified virtual storage object cannot be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task**
> ManagedObjectReference vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task(mo_id, v_storage_object_create_snapshot_request_type)

Creates a snapshot of a given VStorageObject. 

Creates a snapshot of a given VStorageObject.  Requires Datastore.FileManagement privilege.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.v_storage_object_create_snapshot_request_type import VStorageObjectCreateSnapshotRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    v_storage_object_create_snapshot_request_type = vmware_vi.VStorageObjectCreateSnapshotRequestType() # VStorageObjectCreateSnapshotRequestType | 

    try:
        # Creates a snapshot of a given VStorageObject. 
        api_response = api_instance.vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task(mo_id, v_storage_object_create_snapshot_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_v_storage_object_create_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **v_storage_object_create_snapshot_request_type** | [**VStorageObjectCreateSnapshotRequestType**](VStorageObjectCreateSnapshotRequestType.md)|  | 

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

# **vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas**
> DiskChangeInfo vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas(mo_id, vstorage_object_v_center_query_changed_disk_areas_request_type)

Get a list of areas of a virtual disk that have been modified since a well-defined point in the past. 

Get a list of areas of a virtual disk that have been modified since a well-defined point in the past.  The beginning of the change interval is identified by \"changeId\", while the end of the change interval is implied by the snapshot ID passed in.  Note that the result of this function may contain \"false positives\" (i.e: flag areas of the disk as modified that are not). However, it is guaranteed that no changes will be missed.  ***Since:*** vSphere API 6.7  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disk_change_info import DiskChangeInfo
from vmware_vi.models.vstorage_object_v_center_query_changed_disk_areas_request_type import VstorageObjectVCenterQueryChangedDiskAreasRequestType
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
    api_instance = vmware_vi.VcenterVStorageObjectManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    vstorage_object_v_center_query_changed_disk_areas_request_type = vmware_vi.VstorageObjectVCenterQueryChangedDiskAreasRequestType() # VstorageObjectVCenterQueryChangedDiskAreasRequestType | 

    try:
        # Get a list of areas of a virtual disk that have been modified since a well-defined point in the past. 
        api_response = api_instance.vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas(mo_id, vstorage_object_v_center_query_changed_disk_areas_request_type)
        print("The response of VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcenterVStorageObjectManagerApi->vcenter_v_storage_object_manager_vstorage_object_v_center_query_changed_disk_areas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **vstorage_object_v_center_query_changed_disk_areas_request_type** | [**VstorageObjectVCenterQueryChangedDiskAreasRequestType**](VstorageObjectVCenterQueryChangedDiskAreasRequestType.md)|  | 

### Return type

[**DiskChangeInfo**](DiskChangeInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a data structure specifying extents of the virtual disk that have changed since the thime the changeId string was obtained.  |  -  |
**500** | ***InvalidDatastore***: If the operation cannot be performed on the datastore.  ***NotFound***: If specified virtual storage object or snapshot cannot be found.  ***FileFault***: if the virtual disk files cannot be accessed/queried.  ***InvalidState***: if change tracking is not supported for this particular disk.  ***InvalidArgument***: if startOffset is beyond the end of the virtual disk or changeId is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

