# ArrayOfVirtualMachineBootOptionsBootableDevice

A boxed array of *VirtualMachineBootOptionsBootableDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineBootOptionsBootableDevice]**](VirtualMachineBootOptionsBootableDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_boot_options_bootable_device import ArrayOfVirtualMachineBootOptionsBootableDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineBootOptionsBootableDevice from a JSON string
array_of_virtual_machine_boot_options_bootable_device_instance = ArrayOfVirtualMachineBootOptionsBootableDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineBootOptionsBootableDevice.to_json()

# convert the object into a dict
array_of_virtual_machine_boot_options_bootable_device_dict = array_of_virtual_machine_boot_options_bootable_device_instance.to_dict()
# create an instance of ArrayOfVirtualMachineBootOptionsBootableDevice from a dict
array_of_virtual_machine_boot_options_bootable_device_form_dict = array_of_virtual_machine_boot_options_bootable_device.from_dict(array_of_virtual_machine_boot_options_bootable_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


