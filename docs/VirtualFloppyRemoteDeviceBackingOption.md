# VirtualFloppyRemoteDeviceBackingOption

The RemoteDeviceBackingOption data object type contains the options for the floppy remote device backing type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy_remote_device_backing_option import VirtualFloppyRemoteDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppyRemoteDeviceBackingOption from a JSON string
virtual_floppy_remote_device_backing_option_instance = VirtualFloppyRemoteDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualFloppyRemoteDeviceBackingOption.to_json()

# convert the object into a dict
virtual_floppy_remote_device_backing_option_dict = virtual_floppy_remote_device_backing_option_instance.to_dict()
# create an instance of VirtualFloppyRemoteDeviceBackingOption from a dict
virtual_floppy_remote_device_backing_option_form_dict = virtual_floppy_remote_device_backing_option.from_dict(virtual_floppy_remote_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


