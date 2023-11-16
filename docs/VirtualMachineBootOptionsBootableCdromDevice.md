# VirtualMachineBootOptionsBootableCdromDevice

Bootable CDROM.  First CDROM with bootable media found is used.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_boot_options_bootable_cdrom_device import VirtualMachineBootOptionsBootableCdromDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBootOptionsBootableCdromDevice from a JSON string
virtual_machine_boot_options_bootable_cdrom_device_instance = VirtualMachineBootOptionsBootableCdromDevice.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBootOptionsBootableCdromDevice.to_json()

# convert the object into a dict
virtual_machine_boot_options_bootable_cdrom_device_dict = virtual_machine_boot_options_bootable_cdrom_device_instance.to_dict()
# create an instance of VirtualMachineBootOptionsBootableCdromDevice from a dict
virtual_machine_boot_options_bootable_cdrom_device_form_dict = virtual_machine_boot_options_bootable_cdrom_device.from_dict(virtual_machine_boot_options_bootable_cdrom_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


