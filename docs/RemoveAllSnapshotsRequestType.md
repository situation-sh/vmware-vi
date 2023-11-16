# RemoveAllSnapshotsRequestType

The parameters of *VirtualMachine.RemoveAllSnapshots_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consolidate** | **bool** | (optional) If set to true, the virtual disks of the deleted snapshot will be merged with other disk if possible. Default to true.  | [optional] 

## Example

```python
from vmware_vi.models.remove_all_snapshots_request_type import RemoveAllSnapshotsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAllSnapshotsRequestType from a JSON string
remove_all_snapshots_request_type_instance = RemoveAllSnapshotsRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveAllSnapshotsRequestType.to_json()

# convert the object into a dict
remove_all_snapshots_request_type_dict = remove_all_snapshots_request_type_instance.to_dict()
# create an instance of RemoveAllSnapshotsRequestType from a dict
remove_all_snapshots_request_type_form_dict = remove_all_snapshots_request_type.from_dict(remove_all_snapshots_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


