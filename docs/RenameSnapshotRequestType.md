# RenameSnapshotRequestType

The parameters of *VirtualMachineSnapshot.RenameSnapshot*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name for the snapshot.  | [optional] 
**description** | **str** | New description for the snapshot.  | [optional] 

## Example

```python
from vmware_vi.models.rename_snapshot_request_type import RenameSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameSnapshotRequestType from a JSON string
rename_snapshot_request_type_instance = RenameSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print RenameSnapshotRequestType.to_json()

# convert the object into a dict
rename_snapshot_request_type_dict = rename_snapshot_request_type_instance.to_dict()
# create an instance of RenameSnapshotRequestType from a dict
rename_snapshot_request_type_form_dict = rename_snapshot_request_type.from_dict(rename_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


