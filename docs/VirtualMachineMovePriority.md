# VirtualMachineMovePriority

A boxed *VirtualMachineMovePriority_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineMovePriorityEnum**](VirtualMachineMovePriorityEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_move_priority import VirtualMachineMovePriority

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMovePriority from a JSON string
virtual_machine_move_priority_instance = VirtualMachineMovePriority.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMovePriority.to_json()

# convert the object into a dict
virtual_machine_move_priority_dict = virtual_machine_move_priority_instance.to_dict()
# create an instance of VirtualMachineMovePriority from a dict
virtual_machine_move_priority_form_dict = virtual_machine_move_priority.from_dict(virtual_machine_move_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


