# ArrayOfVirtualMachineFaultToleranceState

A boxed array of *VirtualMachineFaultToleranceState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineFaultToleranceStateEnum]**](VirtualMachineFaultToleranceStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_fault_tolerance_state import ArrayOfVirtualMachineFaultToleranceState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineFaultToleranceState from a JSON string
array_of_virtual_machine_fault_tolerance_state_instance = ArrayOfVirtualMachineFaultToleranceState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineFaultToleranceState.to_json()

# convert the object into a dict
array_of_virtual_machine_fault_tolerance_state_dict = array_of_virtual_machine_fault_tolerance_state_instance.to_dict()
# create an instance of ArrayOfVirtualMachineFaultToleranceState from a dict
array_of_virtual_machine_fault_tolerance_state_form_dict = array_of_virtual_machine_fault_tolerance_state.from_dict(array_of_virtual_machine_fault_tolerance_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


