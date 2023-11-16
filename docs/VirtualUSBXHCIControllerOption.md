# VirtualUSBXHCIControllerOption

The VirtualUSBXHCIControllerOption data object type contains the options for a virtual USB Extensible Host Controller Interface (USB 3.0).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_connect_devices** | [**BoolOption**](BoolOption.md) |  | 
**supported_speeds** | **List[str]** | Range of USB device speeds supported by this USB controller type.  Acceptable values are specified at *VirtualMachineUsbInfoSpeed_enum*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_usbxhci_controller_option import VirtualUSBXHCIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBXHCIControllerOption from a JSON string
virtual_usbxhci_controller_option_instance = VirtualUSBXHCIControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBXHCIControllerOption.to_json()

# convert the object into a dict
virtual_usbxhci_controller_option_dict = virtual_usbxhci_controller_option_instance.to_dict()
# create an instance of VirtualUSBXHCIControllerOption from a dict
virtual_usbxhci_controller_option_form_dict = virtual_usbxhci_controller_option.from_dict(virtual_usbxhci_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


