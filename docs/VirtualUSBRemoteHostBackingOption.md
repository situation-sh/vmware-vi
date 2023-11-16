# VirtualUSBRemoteHostBackingOption

The *VirtualUSBRemoteHostBackingOption* data object contains options for remote host USB configuration.  This backing option indicates support for persistent USB connections when vMotion operations migrate virtual machines to different hosts.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_usb_remote_host_backing_option import VirtualUSBRemoteHostBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBRemoteHostBackingOption from a JSON string
virtual_usb_remote_host_backing_option_instance = VirtualUSBRemoteHostBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBRemoteHostBackingOption.to_json()

# convert the object into a dict
virtual_usb_remote_host_backing_option_dict = virtual_usb_remote_host_backing_option_instance.to_dict()
# create an instance of VirtualUSBRemoteHostBackingOption from a dict
virtual_usb_remote_host_backing_option_form_dict = virtual_usb_remote_host_backing_option.from_dict(virtual_usb_remote_host_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


