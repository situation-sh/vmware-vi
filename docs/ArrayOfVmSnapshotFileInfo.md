# ArrayOfVmSnapshotFileInfo

A boxed array of *VmSnapshotFileInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmSnapshotFileInfo]**](VmSnapshotFileInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_snapshot_file_info import ArrayOfVmSnapshotFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmSnapshotFileInfo from a JSON string
array_of_vm_snapshot_file_info_instance = ArrayOfVmSnapshotFileInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmSnapshotFileInfo.to_json()

# convert the object into a dict
array_of_vm_snapshot_file_info_dict = array_of_vm_snapshot_file_info_instance.to_dict()
# create an instance of ArrayOfVmSnapshotFileInfo from a dict
array_of_vm_snapshot_file_info_form_dict = array_of_vm_snapshot_file_info.from_dict(array_of_vm_snapshot_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


