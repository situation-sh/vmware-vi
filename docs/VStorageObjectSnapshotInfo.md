# VStorageObjectSnapshotInfo

This data object type contains the brief information of a virtual storage snapshot.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[VStorageObjectSnapshotInfoVStorageObjectSnapshot]**](VStorageObjectSnapshotInfoVStorageObjectSnapshot.md) | An array of snapshots  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.v_storage_object_snapshot_info import VStorageObjectSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectSnapshotInfo from a JSON string
v_storage_object_snapshot_info_instance = VStorageObjectSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print VStorageObjectSnapshotInfo.to_json()

# convert the object into a dict
v_storage_object_snapshot_info_dict = v_storage_object_snapshot_info_instance.to_dict()
# create an instance of VStorageObjectSnapshotInfo from a dict
v_storage_object_snapshot_info_form_dict = v_storage_object_snapshot_info.from_dict(v_storage_object_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


