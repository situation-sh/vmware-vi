# ArrayOfVStorageObjectSnapshotDetails

A boxed array of *VStorageObjectSnapshotDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VStorageObjectSnapshotDetails]**](VStorageObjectSnapshotDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_storage_object_snapshot_details import ArrayOfVStorageObjectSnapshotDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVStorageObjectSnapshotDetails from a JSON string
array_of_v_storage_object_snapshot_details_instance = ArrayOfVStorageObjectSnapshotDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfVStorageObjectSnapshotDetails.to_json()

# convert the object into a dict
array_of_v_storage_object_snapshot_details_dict = array_of_v_storage_object_snapshot_details_instance.to_dict()
# create an instance of ArrayOfVStorageObjectSnapshotDetails from a dict
array_of_v_storage_object_snapshot_details_form_dict = array_of_v_storage_object_snapshot_details.from_dict(array_of_v_storage_object_snapshot_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


