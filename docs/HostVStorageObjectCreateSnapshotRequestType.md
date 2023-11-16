# HostVStorageObjectCreateSnapshotRequestType

The parameters of *HostVStorageObjectManager.HostVStorageObjectCreateSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**description** | **str** | A short description to be associated with the snapshot.  | 

## Example

```python
from vmware_vi.models.host_v_storage_object_create_snapshot_request_type import HostVStorageObjectCreateSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostVStorageObjectCreateSnapshotRequestType from a JSON string
host_v_storage_object_create_snapshot_request_type_instance = HostVStorageObjectCreateSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print HostVStorageObjectCreateSnapshotRequestType.to_json()

# convert the object into a dict
host_v_storage_object_create_snapshot_request_type_dict = host_v_storage_object_create_snapshot_request_type_instance.to_dict()
# create an instance of HostVStorageObjectCreateSnapshotRequestType from a dict
host_v_storage_object_create_snapshot_request_type_form_dict = host_v_storage_object_create_snapshot_request_type.from_dict(host_v_storage_object_create_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


