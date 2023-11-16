# ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState

A boxed array of *VirtualMachineDeviceRuntimeInfoDeviceRuntimeState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineDeviceRuntimeInfoDeviceRuntimeState]**](VirtualMachineDeviceRuntimeInfoDeviceRuntimeState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_device_runtime_info_device_runtime_state import ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState from a JSON string
array_of_virtual_machine_device_runtime_info_device_runtime_state_instance = ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState.to_json()

# convert the object into a dict
array_of_virtual_machine_device_runtime_info_device_runtime_state_dict = array_of_virtual_machine_device_runtime_info_device_runtime_state_instance.to_dict()
# create an instance of ArrayOfVirtualMachineDeviceRuntimeInfoDeviceRuntimeState from a dict
array_of_virtual_machine_device_runtime_info_device_runtime_state_form_dict = array_of_virtual_machine_device_runtime_info_device_runtime_state.from_dict(array_of_virtual_machine_device_runtime_info_device_runtime_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


