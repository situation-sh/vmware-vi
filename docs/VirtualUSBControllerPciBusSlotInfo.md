# VirtualUSBControllerPciBusSlotInfo

The <code>*VirtualUSBControllerPciBusSlotInfo*</code> data object type defines information about the pci bus slots of usb controller device in a virtual machine.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ehci_pci_slot_number** | **int** | The pci slot number of eHCI controller.  This property should be used only when the ehciEnabled property is set to true.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_usb_controller_pci_bus_slot_info import VirtualUSBControllerPciBusSlotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBControllerPciBusSlotInfo from a JSON string
virtual_usb_controller_pci_bus_slot_info_instance = VirtualUSBControllerPciBusSlotInfo.from_json(json)
# print the JSON string representation of the object
print VirtualUSBControllerPciBusSlotInfo.to_json()

# convert the object into a dict
virtual_usb_controller_pci_bus_slot_info_dict = virtual_usb_controller_pci_bus_slot_info_instance.to_dict()
# create an instance of VirtualUSBControllerPciBusSlotInfo from a dict
virtual_usb_controller_pci_bus_slot_info_form_dict = virtual_usb_controller_pci_bus_slot_info.from_dict(virtual_usb_controller_pci_bus_slot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


