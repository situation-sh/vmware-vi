# VirtualMachineDeviceRuntimeInfo

The DeviceRuntimeInfo data object type provides information about the execution state of a single virtual device.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_state** | [**VirtualMachineDeviceRuntimeInfoDeviceRuntimeState**](VirtualMachineDeviceRuntimeInfoDeviceRuntimeState.md) |  | 
**key** | **int** | The device key.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.virtual_machine_device_runtime_info import VirtualMachineDeviceRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDeviceRuntimeInfo from a JSON string
virtual_machine_device_runtime_info_instance = VirtualMachineDeviceRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDeviceRuntimeInfo.to_json()

# convert the object into a dict
virtual_machine_device_runtime_info_dict = virtual_machine_device_runtime_info_instance.to_dict()
# create an instance of VirtualMachineDeviceRuntimeInfo from a dict
virtual_machine_device_runtime_info_form_dict = virtual_machine_device_runtime_info.from_dict(virtual_machine_device_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


