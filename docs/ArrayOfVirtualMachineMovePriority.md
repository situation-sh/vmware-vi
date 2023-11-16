# ArrayOfVirtualMachineMovePriority

A boxed array of *VirtualMachineMovePriority_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMovePriorityEnum]**](VirtualMachineMovePriorityEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_move_priority import ArrayOfVirtualMachineMovePriority

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMovePriority from a JSON string
array_of_virtual_machine_move_priority_instance = ArrayOfVirtualMachineMovePriority.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMovePriority.to_json()

# convert the object into a dict
array_of_virtual_machine_move_priority_dict = array_of_virtual_machine_move_priority_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMovePriority from a dict
array_of_virtual_machine_move_priority_form_dict = array_of_virtual_machine_move_priority.from_dict(array_of_virtual_machine_move_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


