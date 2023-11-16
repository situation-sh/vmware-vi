# VirtualPointingDeviceBackingOption

The DeviceBackingOption data object type represents the options for a pointing device backing a VirtualPointingDevice data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_pointing_device** | [**ChoiceOption**](ChoiceOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_pointing_device_backing_option import VirtualPointingDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPointingDeviceBackingOption from a JSON string
virtual_pointing_device_backing_option_instance = VirtualPointingDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPointingDeviceBackingOption.to_json()

# convert the object into a dict
virtual_pointing_device_backing_option_dict = virtual_pointing_device_backing_option_instance.to_dict()
# create an instance of VirtualPointingDeviceBackingOption from a dict
virtual_pointing_device_backing_option_form_dict = virtual_pointing_device_backing_option.from_dict(virtual_pointing_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


