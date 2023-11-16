# VmSnapshotFileQuery

This data object type describes the query specification for a virtual machine snapshot file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_snapshot_file_query import VmSnapshotFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VmSnapshotFileQuery from a JSON string
vm_snapshot_file_query_instance = VmSnapshotFileQuery.from_json(json)
# print the JSON string representation of the object
print VmSnapshotFileQuery.to_json()

# convert the object into a dict
vm_snapshot_file_query_dict = vm_snapshot_file_query_instance.to_dict()
# create an instance of VmSnapshotFileQuery from a dict
vm_snapshot_file_query_form_dict = vm_snapshot_file_query.from_dict(vm_snapshot_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


