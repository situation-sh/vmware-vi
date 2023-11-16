# ArrayOfVirtualMachinePowerState

A boxed array of *VirtualMachinePowerState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachinePowerStateEnum]**](VirtualMachinePowerStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_power_state import ArrayOfVirtualMachinePowerState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachinePowerState from a JSON string
array_of_virtual_machine_power_state_instance = ArrayOfVirtualMachinePowerState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachinePowerState.to_json()

# convert the object into a dict
array_of_virtual_machine_power_state_dict = array_of_virtual_machine_power_state_instance.to_dict()
# create an instance of ArrayOfVirtualMachinePowerState from a dict
array_of_virtual_machine_power_state_form_dict = array_of_virtual_machine_power_state.from_dict(array_of_virtual_machine_power_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


