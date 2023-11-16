# vmware_vi.VirtualDiskManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_disk_manager_copy_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_copy_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/CopyVirtualDisk_Task | Copy a virtual disk, performing conversions as specified in the spec. 
[**virtual_disk_manager_create_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_create_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/CreateVirtualDisk_Task | Create a virtual disk. 
[**virtual_disk_manager_defragment_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_defragment_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/DefragmentVirtualDisk_Task | Defragment a sparse virtual disk. 
[**virtual_disk_manager_delete_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_delete_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/DeleteVirtualDisk_Task | Delete a virtual disk. 
[**virtual_disk_manager_eager_zero_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_eager_zero_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/EagerZeroVirtualDisk_Task | Explicitly zero out unaccessed parts zeroedthick disk. 
[**virtual_disk_manager_extend_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_extend_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/ExtendVirtualDisk_Task | Expand the capacity of a virtual disk to the new capacity. 
[**virtual_disk_manager_import_unmanaged_snapshot**](VirtualDiskManagerApi.md#virtual_disk_manager_import_unmanaged_snapshot) | **POST** /VirtualDiskManager/{moId}/ImportUnmanagedSnapshot | Import an unmanaged-snapshot from Virtual-Volume(VVol) enabled Storage Array. 
[**virtual_disk_manager_inflate_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_inflate_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/InflateVirtualDisk_Task | Inflate a sparse or thin-provisioned virtual disk up to the full size. 
[**virtual_disk_manager_move_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_move_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/MoveVirtualDisk_Task | Move a virtual disk and all related files from the source location specified by &lt;code&gt;sourceName&lt;/code&gt; and &lt;code&gt;sourceDatacenter&lt;/code&gt; to the destination location specified by &lt;code&gt;destName&lt;/code&gt; and &lt;code&gt;destDatacenter&lt;/code&gt;. 
[**virtual_disk_manager_query_virtual_disk_fragmentation**](VirtualDiskManagerApi.md#virtual_disk_manager_query_virtual_disk_fragmentation) | **POST** /VirtualDiskManager/{moId}/QueryVirtualDiskFragmentation | Return the percentage of fragmentation of the sparse virtual disk. 
[**virtual_disk_manager_query_virtual_disk_geometry**](VirtualDiskManagerApi.md#virtual_disk_manager_query_virtual_disk_geometry) | **POST** /VirtualDiskManager/{moId}/QueryVirtualDiskGeometry | Get the disk geometry information for the virtual disk. 
[**virtual_disk_manager_query_virtual_disk_uuid**](VirtualDiskManagerApi.md#virtual_disk_manager_query_virtual_disk_uuid) | **POST** /VirtualDiskManager/{moId}/QueryVirtualDiskUuid | Get the virtual disk SCSI inquiry page 0x83 data. 
[**virtual_disk_manager_release_managed_snapshot**](VirtualDiskManagerApi.md#virtual_disk_manager_release_managed_snapshot) | **POST** /VirtualDiskManager/{moId}/ReleaseManagedSnapshot | Release a snapshot previously imported with importUnmanagedSnapshot 
[**virtual_disk_manager_set_virtual_disk_uuid**](VirtualDiskManagerApi.md#virtual_disk_manager_set_virtual_disk_uuid) | **POST** /VirtualDiskManager/{moId}/SetVirtualDiskUuid | Set the virtual disk SCSI inquiry page 0x83 data. 
[**virtual_disk_manager_shrink_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_shrink_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/ShrinkVirtualDisk_Task | Shrink a sparse virtual disk. 
[**virtual_disk_manager_zero_fill_virtual_disk_task**](VirtualDiskManagerApi.md#virtual_disk_manager_zero_fill_virtual_disk_task) | **POST** /VirtualDiskManager/{moId}/ZeroFillVirtualDisk_Task | Overwrite all blocks of the virtual disk with zeros. 


# **virtual_disk_manager_copy_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_copy_virtual_disk_task(mo_id, copy_virtual_disk_request_type)

Copy a virtual disk, performing conversions as specified in the spec. 

Copy a virtual disk, performing conversions as specified in the spec.  If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.  If source and destination resolve to the same file system location, the call has no effect, regardless of destSpec content.  Requires Datastore.FileManagement privilege on both source and destination datastores.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.copy_virtual_disk_request_type import CopyVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    copy_virtual_disk_request_type = vmware_vi.CopyVirtualDiskRequestType() # CopyVirtualDiskRequestType | 

    try:
        # Copy a virtual disk, performing conversions as specified in the spec. 
        api_response = api_instance.virtual_disk_manager_copy_virtual_disk_task(mo_id, copy_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_copy_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_copy_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **copy_virtual_disk_request_type** | [**CopyVirtualDiskRequestType**](CopyVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs cloning the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the source or destination datastore.  ***InvalidDiskFormat***: if the destination&#39;s format is not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_create_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_create_virtual_disk_task(mo_id, create_virtual_disk_request_type)

Create a virtual disk. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostCreateDisk_Task* instead.  Create a virtual disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk is created.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_virtual_disk_request_type import CreateVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_virtual_disk_request_type = vmware_vi.CreateVirtualDiskRequestType() # CreateVirtualDiskRequestType | 

    try:
        # Create a virtual disk. 
        api_response = api_instance.virtual_disk_manager_create_virtual_disk_task(mo_id, create_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_create_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_create_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_virtual_disk_request_type** | [**CreateVirtualDiskRequestType**](CreateVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs creating the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_defragment_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_defragment_virtual_disk_task(mo_id, defragment_virtual_disk_request_type)

Defragment a sparse virtual disk. 

Deprecated as of vSphere 6.5, use *VirtualMachine.DefragmentAllDisks* instead.  Defragment a sparse virtual disk.  This is defragmentation of the virtual disk file(s) in the host operating system, not defragmentation of the guest operating system filesystem inside the virtual disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.defragment_virtual_disk_request_type import DefragmentVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    defragment_virtual_disk_request_type = vmware_vi.DefragmentVirtualDiskRequestType() # DefragmentVirtualDiskRequestType | 

    try:
        # Defragment a sparse virtual disk. 
        api_response = api_instance.virtual_disk_manager_defragment_virtual_disk_task(mo_id, defragment_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_defragment_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_defragment_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **defragment_virtual_disk_request_type** | [**DefragmentVirtualDiskRequestType**](DefragmentVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs defragmenting the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_delete_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_delete_virtual_disk_task(mo_id, delete_virtual_disk_request_type)

Delete a virtual disk. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostDeleteVStorageObject_Task* instead.  Delete a virtual disk.  All files relating to the disk will be deleted.  Deletion of virtual disk is prohibited if it is attached to VMs.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk is removed.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_virtual_disk_request_type import DeleteVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_virtual_disk_request_type = vmware_vi.DeleteVirtualDiskRequestType() # DeleteVirtualDiskRequestType | 

    try:
        # Delete a virtual disk. 
        api_response = api_instance.virtual_disk_manager_delete_virtual_disk_task(mo_id, delete_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_delete_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_delete_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_virtual_disk_request_type** | [**DeleteVirtualDiskRequestType**](DeleteVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs deleting the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_eager_zero_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_eager_zero_virtual_disk_task(mo_id, eager_zero_virtual_disk_request_type)

Explicitly zero out unaccessed parts zeroedthick disk. 

Explicitly zero out unaccessed parts zeroedthick disk.  Effectively a no-op if the disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which wipes the entire disk, this operation only affects previously unaccessed parts of the disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.eager_zero_virtual_disk_request_type import EagerZeroVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    eager_zero_virtual_disk_request_type = vmware_vi.EagerZeroVirtualDiskRequestType() # EagerZeroVirtualDiskRequestType | 

    try:
        # Explicitly zero out unaccessed parts zeroedthick disk. 
        api_response = api_instance.virtual_disk_manager_eager_zero_virtual_disk_task(mo_id, eager_zero_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_eager_zero_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_eager_zero_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **eager_zero_virtual_disk_request_type** | [**EagerZeroVirtualDiskRequestType**](EagerZeroVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs while eager-zeroing the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_extend_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_extend_virtual_disk_task(mo_id, extend_virtual_disk_request_type)

Expand the capacity of a virtual disk to the new capacity. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostExtendDisk_Task* instead.  Expand the capacity of a virtual disk to the new capacity.  If the eagerZero flag is not specified, \\- the extended disk region of a zerothick disk will be zeroedthick \\- the extended disk region of a eagerzerothick disk will be eagerzeroedthick \\- a thin-provisioned disk will always be extended as a thin-provisioned disk. If the eagerZero flag TRUE, the extended region of the disk will always be eagerly zeroed. If the eagerZero flag FALSE, the extended region of a zeroedthick or eagerzeroedthick the disk will not be eagerly zeroed. This condition has no effect on a thin source disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extend_virtual_disk_request_type import ExtendVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    extend_virtual_disk_request_type = vmware_vi.ExtendVirtualDiskRequestType() # ExtendVirtualDiskRequestType | 

    try:
        # Expand the capacity of a virtual disk to the new capacity. 
        api_response = api_instance.virtual_disk_manager_extend_virtual_disk_task(mo_id, extend_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_extend_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_extend_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **extend_virtual_disk_request_type** | [**ExtendVirtualDiskRequestType**](ExtendVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs extending the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_import_unmanaged_snapshot**
> virtual_disk_manager_import_unmanaged_snapshot(mo_id, import_unmanaged_snapshot_request_type)

Import an unmanaged-snapshot from Virtual-Volume(VVol) enabled Storage Array. 

Import an unmanaged-snapshot from Virtual-Volume(VVol) enabled Storage Array.  Storage Array may support users to take snapshots indepedent of VMware stack. Such copies or snapshots are known as 'Unmanaged-Snapshots'. We are providing an ability to end-users to import such unmanaged-snapshots as Virtual Disks.  End-user needs to know the VVol-Identifier to import unmanaged snapshot as VirtualDisk.  Once VirtualDisk is created, user can use 'Datastore Browser' to use with rest of Virtual Machine provisioning APIs.  ***Since:*** vSphere API 6.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.import_unmanaged_snapshot_request_type import ImportUnmanagedSnapshotRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    import_unmanaged_snapshot_request_type = vmware_vi.ImportUnmanagedSnapshotRequestType() # ImportUnmanagedSnapshotRequestType | 

    try:
        # Import an unmanaged-snapshot from Virtual-Volume(VVol) enabled Storage Array. 
        api_instance.virtual_disk_manager_import_unmanaged_snapshot(mo_id, import_unmanaged_snapshot_request_type)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_import_unmanaged_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **import_unmanaged_snapshot_request_type** | [**ImportUnmanagedSnapshotRequestType**](ImportUnmanagedSnapshotRequestType.md)|  | 

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
**500** | ***NotFound***: if VVol is not found  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_inflate_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_inflate_virtual_disk_task(mo_id, inflate_virtual_disk_request_type)

Inflate a sparse or thin-provisioned virtual disk up to the full size. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostInflateDisk_Task* instead.  Inflate a sparse or thin-provisioned virtual disk up to the full size.  Additional space allocated to the disk as a result of this operation will be filled with zeroes.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.inflate_virtual_disk_request_type import InflateVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    inflate_virtual_disk_request_type = vmware_vi.InflateVirtualDiskRequestType() # InflateVirtualDiskRequestType | 

    try:
        # Inflate a sparse or thin-provisioned virtual disk up to the full size. 
        api_response = api_instance.virtual_disk_manager_inflate_virtual_disk_task(mo_id, inflate_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_inflate_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_inflate_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **inflate_virtual_disk_request_type** | [**InflateVirtualDiskRequestType**](InflateVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs inflating the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_move_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_move_virtual_disk_task(mo_id, move_virtual_disk_request_type)

Move a virtual disk and all related files from the source location specified by <code>sourceName</code> and <code>sourceDatacenter</code> to the destination location specified by <code>destName</code> and <code>destDatacenter</code>. 

Move a virtual disk and all related files from the source location specified by <code>sourceName</code> and <code>sourceDatacenter</code> to the destination location specified by <code>destName</code> and <code>destDatacenter</code>.  If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.  If source and destination resolve to the same file system location, the call has no effect.  Requires Datastore.FileManagement privilege on both source and destination datastores.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.move_virtual_disk_request_type import MoveVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    move_virtual_disk_request_type = vmware_vi.MoveVirtualDiskRequestType() # MoveVirtualDiskRequestType | 

    try:
        # Move a virtual disk and all related files from the source location specified by <code>sourceName</code> and <code>sourceDatacenter</code> to the destination location specified by <code>destName</code> and <code>destDatacenter</code>. 
        api_response = api_instance.virtual_disk_manager_move_virtual_disk_task(mo_id, move_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_move_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_move_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **move_virtual_disk_request_type** | [**MoveVirtualDiskRequestType**](MoveVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs renaming the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the source or destination datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_query_virtual_disk_fragmentation**
> int virtual_disk_manager_query_virtual_disk_fragmentation(mo_id, query_virtual_disk_fragmentation_request_type)

Return the percentage of fragmentation of the sparse virtual disk. 

Return the percentage of fragmentation of the sparse virtual disk.  This is the fragmentation of virtual disk file(s) in the host operating system, not the fragmentation of the guest operating systemS filesystem inside the virtual disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_virtual_disk_fragmentation_request_type import QueryVirtualDiskFragmentationRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_virtual_disk_fragmentation_request_type = vmware_vi.QueryVirtualDiskFragmentationRequestType() # QueryVirtualDiskFragmentationRequestType | 

    try:
        # Return the percentage of fragmentation of the sparse virtual disk. 
        api_response = api_instance.virtual_disk_manager_query_virtual_disk_fragmentation(mo_id, query_virtual_disk_fragmentation_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_fragmentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_fragmentation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_virtual_disk_fragmentation_request_type** | [**QueryVirtualDiskFragmentationRequestType**](QueryVirtualDiskFragmentationRequestType.md)|  | 

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
**200** | the percentage of fragmentation (as an integer between 0 and 100) of the sparse virtual disk.  |  -  |
**500** | ***FileFault***: if an error occurs reading the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_query_virtual_disk_geometry**
> HostDiskDimensionsChs virtual_disk_manager_query_virtual_disk_geometry(mo_id, query_virtual_disk_geometry_request_type)

Get the disk geometry information for the virtual disk. 

Get the disk geometry information for the virtual disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_disk_dimensions_chs import HostDiskDimensionsChs
from vmware_vi.models.query_virtual_disk_geometry_request_type import QueryVirtualDiskGeometryRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_virtual_disk_geometry_request_type = vmware_vi.QueryVirtualDiskGeometryRequestType() # QueryVirtualDiskGeometryRequestType | 

    try:
        # Get the disk geometry information for the virtual disk. 
        api_response = api_instance.virtual_disk_manager_query_virtual_disk_geometry(mo_id, query_virtual_disk_geometry_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_geometry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_geometry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_virtual_disk_geometry_request_type** | [**QueryVirtualDiskGeometryRequestType**](QueryVirtualDiskGeometryRequestType.md)|  | 

### Return type

[**HostDiskDimensionsChs**](HostDiskDimensionsChs.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The geometry information for this virtual disk.  |  -  |
**500** | ***FileFault***: if an error occurs reading the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_query_virtual_disk_uuid**
> str virtual_disk_manager_query_virtual_disk_uuid(mo_id, query_virtual_disk_uuid_request_type)

Get the virtual disk SCSI inquiry page 0x83 data. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostRetrieveVStorageObject* instead.  Get the virtual disk SCSI inquiry page 0x83 data.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.query_virtual_disk_uuid_request_type import QueryVirtualDiskUuidRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_virtual_disk_uuid_request_type = vmware_vi.QueryVirtualDiskUuidRequestType() # QueryVirtualDiskUuidRequestType | 

    try:
        # Get the virtual disk SCSI inquiry page 0x83 data. 
        api_response = api_instance.virtual_disk_manager_query_virtual_disk_uuid(mo_id, query_virtual_disk_uuid_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_query_virtual_disk_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_virtual_disk_uuid_request_type** | [**QueryVirtualDiskUuidRequestType**](QueryVirtualDiskUuidRequestType.md)|  | 

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
**200** | The hex representation of the unique ID for this virtual disk.  |  -  |
**500** | ***FileFault***: if an error occurs reading the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_release_managed_snapshot**
> virtual_disk_manager_release_managed_snapshot(mo_id, release_managed_snapshot_request_type)

Release a snapshot previously imported with importUnmanagedSnapshot 

Release a snapshot previously imported with importUnmanagedSnapshot  ***Since:*** vSphere API 6.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.release_managed_snapshot_request_type import ReleaseManagedSnapshotRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    release_managed_snapshot_request_type = vmware_vi.ReleaseManagedSnapshotRequestType() # ReleaseManagedSnapshotRequestType | 

    try:
        # Release a snapshot previously imported with importUnmanagedSnapshot 
        api_instance.virtual_disk_manager_release_managed_snapshot(mo_id, release_managed_snapshot_request_type)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_release_managed_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **release_managed_snapshot_request_type** | [**ReleaseManagedSnapshotRequestType**](ReleaseManagedSnapshotRequestType.md)|  | 

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
**500** | ***FileNotFound***: if vdisk is not found  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_set_virtual_disk_uuid**
> virtual_disk_manager_set_virtual_disk_uuid(mo_id, set_virtual_disk_uuid_request_type)

Set the virtual disk SCSI inquiry page 0x83 data. 

Deprecated as of vSphere 6.5, use *HostVStorageObjectManager.HostRegisterDisk* to register a disk as vStorageObject with new unique UUID.  Set the virtual disk SCSI inquiry page 0x83 data.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_virtual_disk_uuid_request_type import SetVirtualDiskUuidRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_virtual_disk_uuid_request_type = vmware_vi.SetVirtualDiskUuidRequestType() # SetVirtualDiskUuidRequestType | 

    try:
        # Set the virtual disk SCSI inquiry page 0x83 data. 
        api_instance.virtual_disk_manager_set_virtual_disk_uuid(mo_id, set_virtual_disk_uuid_request_type)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_set_virtual_disk_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_virtual_disk_uuid_request_type** | [**SetVirtualDiskUuidRequestType**](SetVirtualDiskUuidRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs updating the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_shrink_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_shrink_virtual_disk_task(mo_id, shrink_virtual_disk_request_type)

Shrink a sparse virtual disk. 

Deprecated as of vSphere 6.5, use *VirtualMachine.ShrinkDisk_Task* instead.  Shrink a sparse virtual disk.  The datacenter parameter may be omitted if a URL is used to name the disk.  The optional parameter <code>copy</code> specifies whether to shrink the disk in copy-shrink mode or in-place mode. In copy-shrink mode, additional space is required, but will result in a shrunk disk that is also defragmented. In-place shrink does not require additional space, but will increase fragmentation. The default behavior is to perform copy-shrink if the parameter is not specified.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.shrink_virtual_disk_request_type import ShrinkVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    shrink_virtual_disk_request_type = vmware_vi.ShrinkVirtualDiskRequestType() # ShrinkVirtualDiskRequestType | 

    try:
        # Shrink a sparse virtual disk. 
        api_response = api_instance.virtual_disk_manager_shrink_virtual_disk_task(mo_id, shrink_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_shrink_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_shrink_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **shrink_virtual_disk_request_type** | [**ShrinkVirtualDiskRequestType**](ShrinkVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs shrinking the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_disk_manager_zero_fill_virtual_disk_task**
> ManagedObjectReference virtual_disk_manager_zero_fill_virtual_disk_task(mo_id, zero_fill_virtual_disk_request_type)

Overwrite all blocks of the virtual disk with zeros. 

Overwrite all blocks of the virtual disk with zeros.  All data will be lost.  The datacenter parameter may be omitted if a URL is used to name the disk.  Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.zero_fill_virtual_disk_request_type import ZeroFillVirtualDiskRequestType
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
    api_instance = vmware_vi.VirtualDiskManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    zero_fill_virtual_disk_request_type = vmware_vi.ZeroFillVirtualDiskRequestType() # ZeroFillVirtualDiskRequestType | 

    try:
        # Overwrite all blocks of the virtual disk with zeros. 
        api_response = api_instance.virtual_disk_manager_zero_fill_virtual_disk_task(mo_id, zero_fill_virtual_disk_request_type)
        print("The response of VirtualDiskManagerApi->virtual_disk_manager_zero_fill_virtual_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDiskManagerApi->virtual_disk_manager_zero_fill_virtual_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **zero_fill_virtual_disk_request_type** | [**ZeroFillVirtualDiskRequestType**](ZeroFillVirtualDiskRequestType.md)|  | 

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
**500** | ***FileFault***: if an error occurs zero filling the virtual disk.  ***InvalidDatastore***: if the operation cannot be performed on the datastore.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

