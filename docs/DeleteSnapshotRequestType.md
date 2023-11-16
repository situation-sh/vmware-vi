# DeleteSnapshotRequestType

The parameters of *VcenterVStorageObjectManager.DeleteSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.delete_snapshot_request_type import DeleteSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotRequestType from a JSON string
delete_snapshot_request_type_instance = DeleteSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteSnapshotRequestType.to_json()

# convert the object into a dict
delete_snapshot_request_type_dict = delete_snapshot_request_type_instance.to_dict()
# create an instance of DeleteSnapshotRequestType from a dict
delete_snapshot_request_type_form_dict = delete_snapshot_request_type.from_dict(delete_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


