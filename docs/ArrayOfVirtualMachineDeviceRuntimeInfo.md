# ArrayOfVirtualMachineDeviceRuntimeInfo

A boxed array of *VirtualMachineDeviceRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineDeviceRuntimeInfo]**](VirtualMachineDeviceRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_device_runtime_info import ArrayOfVirtualMachineDeviceRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineDeviceRuntimeInfo from a JSON string
array_of_virtual_machine_device_runtime_info_instance = ArrayOfVirtualMachineDeviceRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineDeviceRuntimeInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_device_runtime_info_dict = array_of_virtual_machine_device_runtime_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineDeviceRuntimeInfo from a dict
array_of_virtual_machine_device_runtime_info_form_dict = array_of_virtual_machine_device_runtime_info.from_dict(array_of_virtual_machine_device_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


