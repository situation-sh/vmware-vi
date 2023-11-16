# VirtualPointingDevice

The VirtualPointingDevice data object type contains information about the mouse type on a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pointing_device import VirtualPointingDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPointingDevice from a JSON string
virtual_pointing_device_instance = VirtualPointingDevice.from_json(json)
# print the JSON string representation of the object
print VirtualPointingDevice.to_json()

# convert the object into a dict
virtual_pointing_device_dict = virtual_pointing_device_instance.to_dict()
# create an instance of VirtualPointingDevice from a dict
virtual_pointing_device_form_dict = virtual_pointing_device.from_dict(virtual_pointing_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


