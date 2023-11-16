# ArrayOfVirtualMachineSnapshotTree

A boxed array of *VirtualMachineSnapshotTree*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineSnapshotTree]**](VirtualMachineSnapshotTree.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_snapshot_tree import ArrayOfVirtualMachineSnapshotTree

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineSnapshotTree from a JSON string
array_of_virtual_machine_snapshot_tree_instance = ArrayOfVirtualMachineSnapshotTree.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineSnapshotTree.to_json()

# convert the object into a dict
array_of_virtual_machine_snapshot_tree_dict = array_of_virtual_machine_snapshot_tree_instance.to_dict()
# create an instance of ArrayOfVirtualMachineSnapshotTree from a dict
array_of_virtual_machine_snapshot_tree_form_dict = array_of_virtual_machine_snapshot_tree.from_dict(array_of_virtual_machine_snapshot_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


