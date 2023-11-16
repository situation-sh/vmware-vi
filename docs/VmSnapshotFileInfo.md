# VmSnapshotFileInfo

This data object type describes a file that is a virtual disk snapshot file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_snapshot_file_info import VmSnapshotFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmSnapshotFileInfo from a JSON string
vm_snapshot_file_info_instance = VmSnapshotFileInfo.from_json(json)
# print the JSON string representation of the object
print VmSnapshotFileInfo.to_json()

# convert the object into a dict
vm_snapshot_file_info_dict = vm_snapshot_file_info_instance.to_dict()
# create an instance of VmSnapshotFileInfo from a dict
vm_snapshot_file_info_form_dict = vm_snapshot_file_info.from_dict(vm_snapshot_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


