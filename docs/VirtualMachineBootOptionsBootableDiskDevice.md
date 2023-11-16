# VirtualMachineBootOptionsBootableDiskDevice

Bootable disk.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_key** | **int** | *Key* property of the bootable harddisk.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_boot_options_bootable_disk_device import VirtualMachineBootOptionsBootableDiskDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBootOptionsBootableDiskDevice from a JSON string
virtual_machine_boot_options_bootable_disk_device_instance = VirtualMachineBootOptionsBootableDiskDevice.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBootOptionsBootableDiskDevice.to_json()

# convert the object into a dict
virtual_machine_boot_options_bootable_disk_device_dict = virtual_machine_boot_options_bootable_disk_device_instance.to_dict()
# create an instance of VirtualMachineBootOptionsBootableDiskDevice from a dict
virtual_machine_boot_options_bootable_disk_device_form_dict = virtual_machine_boot_options_bootable_disk_device.from_dict(virtual_machine_boot_options_bootable_disk_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


