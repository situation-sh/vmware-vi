# VirtualMachineFaultToleranceState

A boxed *VirtualMachineFaultToleranceState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineFaultToleranceStateEnum**](VirtualMachineFaultToleranceStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_fault_tolerance_state import VirtualMachineFaultToleranceState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFaultToleranceState from a JSON string
virtual_machine_fault_tolerance_state_instance = VirtualMachineFaultToleranceState.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFaultToleranceState.to_json()

# convert the object into a dict
virtual_machine_fault_tolerance_state_dict = virtual_machine_fault_tolerance_state_instance.to_dict()
# create an instance of VirtualMachineFaultToleranceState from a dict
virtual_machine_fault_tolerance_state_form_dict = virtual_machine_fault_tolerance_state.from_dict(virtual_machine_fault_tolerance_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


