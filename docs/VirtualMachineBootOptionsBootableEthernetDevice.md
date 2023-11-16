# VirtualMachineBootOptionsBootableEthernetDevice

Bootable ethernet adapter.  PXE boot is attempted from the device.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_key** | **int** | *Key* property of the bootable ethernet adapter.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_boot_options_bootable_ethernet_device import VirtualMachineBootOptionsBootableEthernetDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBootOptionsBootableEthernetDevice from a JSON string
virtual_machine_boot_options_bootable_ethernet_device_instance = VirtualMachineBootOptionsBootableEthernetDevice.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBootOptionsBootableEthernetDevice.to_json()

# convert the object into a dict
virtual_machine_boot_options_bootable_ethernet_device_dict = virtual_machine_boot_options_bootable_ethernet_device_instance.to_dict()
# create an instance of VirtualMachineBootOptionsBootableEthernetDevice from a dict
virtual_machine_boot_options_bootable_ethernet_device_form_dict = virtual_machine_boot_options_bootable_ethernet_device.from_dict(virtual_machine_boot_options_bootable_ethernet_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


