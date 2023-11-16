# VirtualMachineBootOptionsBootableDevice

Bootable device.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_boot_options_bootable_device import VirtualMachineBootOptionsBootableDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBootOptionsBootableDevice from a JSON string
virtual_machine_boot_options_bootable_device_instance = VirtualMachineBootOptionsBootableDevice.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBootOptionsBootableDevice.to_json()

# convert the object into a dict
virtual_machine_boot_options_bootable_device_dict = virtual_machine_boot_options_bootable_device_instance.to_dict()
# create an instance of VirtualMachineBootOptionsBootableDevice from a dict
virtual_machine_boot_options_bootable_device_form_dict = virtual_machine_boot_options_bootable_device.from_dict(virtual_machine_boot_options_bootable_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


