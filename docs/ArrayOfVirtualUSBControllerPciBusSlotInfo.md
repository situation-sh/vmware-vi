# ArrayOfVirtualUSBControllerPciBusSlotInfo

A boxed array of *VirtualUSBControllerPciBusSlotInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualUSBControllerPciBusSlotInfo]**](VirtualUSBControllerPciBusSlotInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_usb_controller_pci_bus_slot_info import ArrayOfVirtualUSBControllerPciBusSlotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualUSBControllerPciBusSlotInfo from a JSON string
array_of_virtual_usb_controller_pci_bus_slot_info_instance = ArrayOfVirtualUSBControllerPciBusSlotInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualUSBControllerPciBusSlotInfo.to_json()

# convert the object into a dict
array_of_virtual_usb_controller_pci_bus_slot_info_dict = array_of_virtual_usb_controller_pci_bus_slot_info_instance.to_dict()
# create an instance of ArrayOfVirtualUSBControllerPciBusSlotInfo from a dict
array_of_virtual_usb_controller_pci_bus_slot_info_form_dict = array_of_virtual_usb_controller_pci_bus_slot_info.from_dict(array_of_virtual_usb_controller_pci_bus_slot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


