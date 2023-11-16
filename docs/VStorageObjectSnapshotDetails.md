# VStorageObjectSnapshotDetails

This data object type provides details of a vstorage object snapshot  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the snaphost object  ***Since:*** vSphere API 6.7  | [optional] 
**changed_block_tracking_id** | **str** | Changed block tracking ID of the snapshot  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.v_storage_object_snapshot_details import VStorageObjectSnapshotDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectSnapshotDetails from a JSON string
v_storage_object_snapshot_details_instance = VStorageObjectSnapshotDetails.from_json(json)
# print the JSON string representation of the object
print VStorageObjectSnapshotDetails.to_json()

# convert the object into a dict
v_storage_object_snapshot_details_dict = v_storage_object_snapshot_details_instance.to_dict()
# create an instance of VStorageObjectSnapshotDetails from a dict
v_storage_object_snapshot_details_form_dict = v_storage_object_snapshot_details.from_dict(v_storage_object_snapshot_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


