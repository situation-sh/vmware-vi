# VirtualUSBOption

The *VirtualUSBOption* data object type contains options for USB device configuration on a virtual machine.  The vSphere API supports the following options: - Local host USB connection   (*VirtualUSBUSBBackingOption*) - Remote host USB connection   (*VirtualUSBRemoteHostBackingOption*)    For information about USB device configuration, see *VirtualUSB*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_usb_option import VirtualUSBOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBOption from a JSON string
virtual_usb_option_instance = VirtualUSBOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBOption.to_json()

# convert the object into a dict
virtual_usb_option_dict = virtual_usb_option_instance.to_dict()
# create an instance of VirtualUSBOption from a dict
virtual_usb_option_form_dict = virtual_usb_option.from_dict(virtual_usb_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


