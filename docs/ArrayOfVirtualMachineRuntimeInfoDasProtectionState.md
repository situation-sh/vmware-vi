# ArrayOfVirtualMachineRuntimeInfoDasProtectionState

A boxed array of *VirtualMachineRuntimeInfoDasProtectionState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineRuntimeInfoDasProtectionState]**](VirtualMachineRuntimeInfoDasProtectionState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_runtime_info_das_protection_state import ArrayOfVirtualMachineRuntimeInfoDasProtectionState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineRuntimeInfoDasProtectionState from a JSON string
array_of_virtual_machine_runtime_info_das_protection_state_instance = ArrayOfVirtualMachineRuntimeInfoDasProtectionState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineRuntimeInfoDasProtectionState.to_json()

# convert the object into a dict
array_of_virtual_machine_runtime_info_das_protection_state_dict = array_of_virtual_machine_runtime_info_das_protection_state_instance.to_dict()
# create an instance of ArrayOfVirtualMachineRuntimeInfoDasProtectionState from a dict
array_of_virtual_machine_runtime_info_das_protection_state_form_dict = array_of_virtual_machine_runtime_info_das_protection_state.from_dict(array_of_virtual_machine_runtime_info_das_protection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


