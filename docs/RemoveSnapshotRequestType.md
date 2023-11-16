# RemoveSnapshotRequestType

The parameters of *VirtualMachineSnapshot.RemoveSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove_children** | **bool** | Flag to specify removal of the entire snapshot subtree.  | 
**consolidate** | **bool** | (optional) If set to true, the virtual disk associated with this snapshot will be merged with other disk if possible. Defaults to true.  | [optional] 

## Example

```python
from vmware_vi.models.remove_snapshot_request_type import RemoveSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSnapshotRequestType from a JSON string
remove_snapshot_request_type_instance = RemoveSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveSnapshotRequestType.to_json()

# convert the object into a dict
remove_snapshot_request_type_dict = remove_snapshot_request_type_instance.to_dict()
# create an instance of RemoveSnapshotRequestType from a dict
remove_snapshot_request_type_form_dict = remove_snapshot_request_type.from_dict(remove_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


