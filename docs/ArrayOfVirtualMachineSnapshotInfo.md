# ArrayOfVirtualMachineSnapshotInfo

A boxed array of *VirtualMachineSnapshotInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineSnapshotInfo]**](VirtualMachineSnapshotInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_snapshot_info import ArrayOfVirtualMachineSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineSnapshotInfo from a JSON string
array_of_virtual_machine_snapshot_info_instance = ArrayOfVirtualMachineSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineSnapshotInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_snapshot_info_dict = array_of_virtual_machine_snapshot_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineSnapshotInfo from a dict
array_of_virtual_machine_snapshot_info_form_dict = array_of_virtual_machine_snapshot_info.from_dict(array_of_virtual_machine_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


