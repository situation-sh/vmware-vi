# VirtualUSBController

The *VirtualUSBController* data object describes a virtual USB controller and contains a list of the devices connected to the controller.  A virtual machine must have a virtual USB controller before you can add a USB device to the virtual machine configuration. To add a controller, include a *VirtualUSBController* object in the *VirtualDeviceConfigSpec* for your virtual machine configuration. You can add only one controller to a virtual machine. A virtual USB controller supports up to 20 USB device connections on the virtual machine.  The ESX Server host must have the USB controller hardware and modules that support USB 2.0 and USB1.1. You can use a maximum of 15 USB controllers on a host. If your system includes an additional number of controllers with connected devices, the additional devices will not be available to virtual machines on the host.  You must remove all USB devices from a virtual machine before you can remove the USB controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_connect_devices** | **bool** | Flag to indicate whether or not the ability to hot plug devices is enabled on this controller.  | [optional] 
**ehci_enabled** | **bool** | Flag to indicate whether or not enhanced host controller interface (USB 2.0) is enabled on this controller.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_usb_controller import VirtualUSBController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBController from a JSON string
virtual_usb_controller_instance = VirtualUSBController.from_json(json)
# print the JSON string representation of the object
print VirtualUSBController.to_json()

# convert the object into a dict
virtual_usb_controller_dict = virtual_usb_controller_instance.to_dict()
# create an instance of VirtualUSBController from a dict
virtual_usb_controller_form_dict = virtual_usb_controller.from_dict(virtual_usb_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


