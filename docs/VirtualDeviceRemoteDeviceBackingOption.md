# VirtualDeviceRemoteDeviceBackingOption

VirtualDeviceOption.RemoteDeviceBackingOption describes the options for a remote device backing.  The primary difference between a remote device backing and a local device backing is that the VirtualCenter server cannot provide a list of remote host devices available for this virtual device backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect_available** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_remote_device_backing_option import VirtualDeviceRemoteDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceRemoteDeviceBackingOption from a JSON string
virtual_device_remote_device_backing_option_instance = VirtualDeviceRemoteDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceRemoteDeviceBackingOption.to_json()

# convert the object into a dict
virtual_device_remote_device_backing_option_dict = virtual_device_remote_device_backing_option_instance.to_dict()
# create an instance of VirtualDeviceRemoteDeviceBackingOption from a dict
virtual_device_remote_device_backing_option_form_dict = virtual_device_remote_device_backing_option.from_dict(virtual_device_remote_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


