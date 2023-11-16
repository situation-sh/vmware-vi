# VirtualUSBUSBBackingOption

The *VirtualUSBUSBBackingOption* data object contains the options for virtual backing for a USB device.  This backing option indicates support for a local connection where the virtual machine will remain on the host to which the USB device is attached.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_usbusb_backing_option import VirtualUSBUSBBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBUSBBackingOption from a JSON string
virtual_usbusb_backing_option_instance = VirtualUSBUSBBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBUSBBackingOption.to_json()

# convert the object into a dict
virtual_usbusb_backing_option_dict = virtual_usbusb_backing_option_instance.to_dict()
# create an instance of VirtualUSBUSBBackingOption from a dict
virtual_usbusb_backing_option_form_dict = virtual_usbusb_backing_option.from_dict(virtual_usbusb_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


