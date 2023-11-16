# VirtualUSBXHCIController

The *VirtualUSBXHCIController* data object describes a virtual USB Extensible Host Controller Interface (USB 3.0).  For more informatino see *VirtualUSBController*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_connect_devices** | **bool** | Flag to indicate whether or not the ability to hot plug devices is enabled on this controller.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_usbxhci_controller import VirtualUSBXHCIController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBXHCIController from a JSON string
virtual_usbxhci_controller_instance = VirtualUSBXHCIController.from_json(json)
# print the JSON string representation of the object
print VirtualUSBXHCIController.to_json()

# convert the object into a dict
virtual_usbxhci_controller_dict = virtual_usbxhci_controller_instance.to_dict()
# create an instance of VirtualUSBXHCIController from a dict
virtual_usbxhci_controller_form_dict = virtual_usbxhci_controller.from_dict(virtual_usbxhci_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


