# VirtualDevicePciBusSlotInfo

The <code>*VirtualDevicePciBusSlotInfo*</code> data object type defines information about a pci bus slot of pci device in a virtual machine.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pci_slot_number** | **int** | The pci slot number of the virtual device.  The pci slot number assignment should generally be left to the system. If assigned a value, and the value is invalid or duplicated, it will automatically be reassigned. This will not cause an error.  Generally, the PCI slot numbers should never be specified in an Reconfigure operation, and only in a CreateVM operation if i) they are specified for all devices, and ii) the numbers have been determined by looking at an existing VM configuration of similar hardware version. In other words, when the virtual hardware configuration is duplicated.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_device_pci_bus_slot_info import VirtualDevicePciBusSlotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDevicePciBusSlotInfo from a JSON string
virtual_device_pci_bus_slot_info_instance = VirtualDevicePciBusSlotInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDevicePciBusSlotInfo.to_json()

# convert the object into a dict
virtual_device_pci_bus_slot_info_dict = virtual_device_pci_bus_slot_info_instance.to_dict()
# create an instance of VirtualDevicePciBusSlotInfo from a dict
virtual_device_pci_bus_slot_info_form_dict = virtual_device_pci_bus_slot_info.from_dict(virtual_device_pci_bus_slot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


