# VirtualUSBControllerOption

The VirtualUSBControllerOption data object type contains the options for a virtual USB Host Controller Interface. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_connect_devices** | [**BoolOption**](BoolOption.md) |  | 
**ehci_supported** | [**BoolOption**](BoolOption.md) |  | 
**supported_speeds** | **List[str]** | Range of USB device speeds supported by this USB controller type.  Acceptable values are specified at *VirtualMachineUsbInfoSpeed_enum*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_usb_controller_option import VirtualUSBControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBControllerOption from a JSON string
virtual_usb_controller_option_instance = VirtualUSBControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBControllerOption.to_json()

# convert the object into a dict
virtual_usb_controller_option_dict = virtual_usb_controller_option_instance.to_dict()
# create an instance of VirtualUSBControllerOption from a dict
virtual_usb_controller_option_form_dict = virtual_usb_controller_option.from_dict(virtual_usb_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


