# VirtualUSBRemoteClientBackingOption

This data object type contains the options for the virtual remote USB client backing data object type.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_usb_remote_client_backing_option import VirtualUSBRemoteClientBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBRemoteClientBackingOption from a JSON string
virtual_usb_remote_client_backing_option_instance = VirtualUSBRemoteClientBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualUSBRemoteClientBackingOption.to_json()

# convert the object into a dict
virtual_usb_remote_client_backing_option_dict = virtual_usb_remote_client_backing_option_instance.to_dict()
# create an instance of VirtualUSBRemoteClientBackingOption from a dict
virtual_usb_remote_client_backing_option_form_dict = virtual_usb_remote_client_backing_option.from_dict(virtual_usb_remote_client_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


