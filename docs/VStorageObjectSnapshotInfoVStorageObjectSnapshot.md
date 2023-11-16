# VStorageObjectSnapshotInfoVStorageObjectSnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | [optional] 
**backing_object_id** | **str** | Backing object ID  ***Since:*** vSphere API 6.7  | [optional] 
**create_time** | **datetime** | The date and time this object was created.  ***Since:*** vSphere API 6.7  | 
**description** | **str** | Short description of the snapshot  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.v_storage_object_snapshot_info_v_storage_object_snapshot import VStorageObjectSnapshotInfoVStorageObjectSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectSnapshotInfoVStorageObjectSnapshot from a JSON string
v_storage_object_snapshot_info_v_storage_object_snapshot_instance = VStorageObjectSnapshotInfoVStorageObjectSnapshot.from_json(json)
# print the JSON string representation of the object
print VStorageObjectSnapshotInfoVStorageObjectSnapshot.to_json()

# convert the object into a dict
v_storage_object_snapshot_info_v_storage_object_snapshot_dict = v_storage_object_snapshot_info_v_storage_object_snapshot_instance.to_dict()
# create an instance of VStorageObjectSnapshotInfoVStorageObjectSnapshot from a dict
v_storage_object_snapshot_info_v_storage_object_snapshot_form_dict = v_storage_object_snapshot_info_v_storage_object_snapshot.from_dict(v_storage_object_snapshot_info_v_storage_object_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


