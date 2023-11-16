# ArrayOfVirtualMachineBootOptionsBootableDiskDevice

A boxed array of *VirtualMachineBootOptionsBootableDiskDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineBootOptionsBootableDiskDevice]**](VirtualMachineBootOptionsBootableDiskDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_boot_options_bootable_disk_device import ArrayOfVirtualMachineBootOptionsBootableDiskDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineBootOptionsBootableDiskDevice from a JSON string
array_of_virtual_machine_boot_options_bootable_disk_device_instance = ArrayOfVirtualMachineBootOptionsBootableDiskDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineBootOptionsBootableDiskDevice.to_json()

# convert the object into a dict
array_of_virtual_machine_boot_options_bootable_disk_device_dict = array_of_virtual_machine_boot_options_bootable_disk_device_instance.to_dict()
# create an instance of ArrayOfVirtualMachineBootOptionsBootableDiskDevice from a dict
array_of_virtual_machine_boot_options_bootable_disk_device_form_dict = array_of_virtual_machine_boot_options_bootable_disk_device.from_dict(array_of_virtual_machine_boot_options_bootable_disk_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


