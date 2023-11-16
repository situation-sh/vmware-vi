# VirtualMachineDatastoreInfo

DatastoreInfo describes a datastore that a virtual disk can be stored on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreSummary**](DatastoreSummary.md) |  | 
**capability** | [**DatastoreCapability**](DatastoreCapability.md) |  | 
**max_file_size** | **int** | The maximum size of a file that can reside on this datastore.  | 
**max_virtual_disk_capacity** | **int** | The maximum capacity of a virtual disk which can be created on this volume  ***Since:*** vSphere API 5.5  | [optional] 
**max_physical_rdm_file_size** | **int** | Maximum raw device mapping size (physical compatibility)  ***Since:*** vSphere API 6.0  | [optional] 
**max_virtual_rdm_file_size** | **int** | Maximum raw device mapping size (virtual compatibility)  ***Since:*** vSphere API 6.0  | [optional] 
**mode** | **str** | Access mode for this datastore.  This is either readOnly or readWrite. A virtual disk needs to be stored on readWrite datastore. ISOs can be read from a readOnly datastore.  See also *HostMountMode_enum*.  | 
**v_storage_support** | **str** | Indicate the states of vStorage hardware acceleration support for this datastore.  In the case of a cluster compute resource, this property is aggregated from the values reported by individual hosts as follows: - If at least one host reports   *vStorageSupported*,   then it is set to   *vStorageSupported*. - Else if at least one host reports   *vStorageUnknown*,   it is set to   *vStorageUnknown*. - Else if at least one host reports   *vStorageUnsupported*,   it is set to   *vStorageUnsupported*. - Else it is unset.    See also *FileSystemMountInfoVStorageSupportStatus_enum*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_datastore_info import VirtualMachineDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDatastoreInfo from a JSON string
virtual_machine_datastore_info_instance = VirtualMachineDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDatastoreInfo.to_json()

# convert the object into a dict
virtual_machine_datastore_info_dict = virtual_machine_datastore_info_instance.to_dict()
# create an instance of VirtualMachineDatastoreInfo from a dict
virtual_machine_datastore_info_form_dict = virtual_machine_datastore_info.from_dict(virtual_machine_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


