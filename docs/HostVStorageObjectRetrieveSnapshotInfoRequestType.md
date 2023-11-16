# HostVStorageObjectRetrieveSnapshotInfoRequestType

The parameters of *HostVStorageObjectManager.HostVStorageObjectRetrieveSnapshotInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_v_storage_object_retrieve_snapshot_info_request_type import HostVStorageObjectRetrieveSnapshotInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostVStorageObjectRetrieveSnapshotInfoRequestType from a JSON string
host_v_storage_object_retrieve_snapshot_info_request_type_instance = HostVStorageObjectRetrieveSnapshotInfoRequestType.from_json(json)
# print the JSON string representation of the object
print HostVStorageObjectRetrieveSnapshotInfoRequestType.to_json()

# convert the object into a dict
host_v_storage_object_retrieve_snapshot_info_request_type_dict = host_v_storage_object_retrieve_snapshot_info_request_type_instance.to_dict()
# create an instance of HostVStorageObjectRetrieveSnapshotInfoRequestType from a dict
host_v_storage_object_retrieve_snapshot_info_request_type_form_dict = host_v_storage_object_retrieve_snapshot_info_request_type.from_dict(host_v_storage_object_retrieve_snapshot_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


