# ArrayOfVStorageObjectSnapshotInfo

A boxed array of *VStorageObjectSnapshotInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VStorageObjectSnapshotInfo]**](VStorageObjectSnapshotInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_storage_object_snapshot_info import ArrayOfVStorageObjectSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVStorageObjectSnapshotInfo from a JSON string
array_of_v_storage_object_snapshot_info_instance = ArrayOfVStorageObjectSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVStorageObjectSnapshotInfo.to_json()

# convert the object into a dict
array_of_v_storage_object_snapshot_info_dict = array_of_v_storage_object_snapshot_info_instance.to_dict()
# create an instance of ArrayOfVStorageObjectSnapshotInfo from a dict
array_of_v_storage_object_snapshot_info_form_dict = array_of_v_storage_object_snapshot_info.from_dict(array_of_v_storage_object_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


