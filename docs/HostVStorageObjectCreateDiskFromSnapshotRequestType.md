# HostVStorageObjectCreateDiskFromSnapshotRequestType

The parameters of *HostVStorageObjectManager.HostVStorageObjectCreateDiskFromSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 
**name** | **str** | A user friendly name to be associated with the new disk.  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | SPBM Profile requirement on the new virtual storage object. If not specified datastore default policy would be assigned.  ***Since:*** vSphere API 5.5  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 
**path** | **str** | Relative location in the specified datastore where disk needs to be created. If not specified disk gets created at defualt VStorageObject location on the specified datastore  | [optional] 
**provisioning_type** | **str** | Provisioining type of the disk as specified in above mentioned profile. The list of supported values can be found in *BaseConfigInfoDiskFileBackingInfoProvisioningType_enum*  | [optional] 

## Example

```python
from vmware_vi.models.host_v_storage_object_create_disk_from_snapshot_request_type import HostVStorageObjectCreateDiskFromSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostVStorageObjectCreateDiskFromSnapshotRequestType from a JSON string
host_v_storage_object_create_disk_from_snapshot_request_type_instance = HostVStorageObjectCreateDiskFromSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print HostVStorageObjectCreateDiskFromSnapshotRequestType.to_json()

# convert the object into a dict
host_v_storage_object_create_disk_from_snapshot_request_type_dict = host_v_storage_object_create_disk_from_snapshot_request_type_instance.to_dict()
# create an instance of HostVStorageObjectCreateDiskFromSnapshotRequestType from a dict
host_v_storage_object_create_disk_from_snapshot_request_type_form_dict = host_v_storage_object_create_disk_from_snapshot_request_type.from_dict(host_v_storage_object_create_disk_from_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


