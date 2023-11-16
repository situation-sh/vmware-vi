# VirtualMachineDeviceRuntimeInfoDeviceRuntimeState

Runtime state of a device.  Subclassed for information that is specific to certain device types.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_device_runtime_info_device_runtime_state import VirtualMachineDeviceRuntimeInfoDeviceRuntimeState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDeviceRuntimeInfoDeviceRuntimeState from a JSON string
virtual_machine_device_runtime_info_device_runtime_state_instance = VirtualMachineDeviceRuntimeInfoDeviceRuntimeState.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDeviceRuntimeInfoDeviceRuntimeState.to_json()

# convert the object into a dict
virtual_machine_device_runtime_info_device_runtime_state_dict = virtual_machine_device_runtime_info_device_runtime_state_instance.to_dict()
# create an instance of VirtualMachineDeviceRuntimeInfoDeviceRuntimeState from a dict
virtual_machine_device_runtime_info_device_runtime_state_form_dict = virtual_machine_device_runtime_info_device_runtime_state.from_dict(virtual_machine_device_runtime_info_device_runtime_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


