# VirtualPointingDeviceOption

The VirtualPointingDeviceOption data object type contains the options for the host mouse type defined in the *VirtualPointingDevice* data object type.  These options include the valid selections for the mouse type, the supported mouse types, and the default mouse type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pointing_device_option import VirtualPointingDeviceOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPointingDeviceOption from a JSON string
virtual_pointing_device_option_instance = VirtualPointingDeviceOption.from_json(json)
# print the JSON string representation of the object
print VirtualPointingDeviceOption.to_json()

# convert the object into a dict
virtual_pointing_device_option_dict = virtual_pointing_device_option_instance.to_dict()
# create an instance of VirtualPointingDeviceOption from a dict
virtual_pointing_device_option_form_dict = virtual_pointing_device_option.from_dict(virtual_pointing_device_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


