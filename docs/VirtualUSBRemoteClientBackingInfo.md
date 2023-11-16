# VirtualUSBRemoteClientBackingInfo

The virtual remote client USB device backing class.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname of the remote client where the physical USB device resides.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_usb_remote_client_backing_info import VirtualUSBRemoteClientBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualUSBRemoteClientBackingInfo from a JSON string
virtual_usb_remote_client_backing_info_instance = VirtualUSBRemoteClientBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualUSBRemoteClientBackingInfo.to_json()

# convert the object into a dict
virtual_usb_remote_client_backing_info_dict = virtual_usb_remote_client_backing_info_instance.to_dict()
# create an instance of VirtualUSBRemoteClientBackingInfo from a dict
virtual_usb_remote_client_backing_info_form_dict = virtual_usb_remote_client_backing_info.from_dict(virtual_usb_remote_client_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


