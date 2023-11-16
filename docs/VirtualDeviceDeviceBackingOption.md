# VirtualDeviceDeviceBackingOption

The DeviceBackingOption data class contains device-specific backing options. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect_available** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_device_backing_option import VirtualDeviceDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceDeviceBackingOption from a JSON string
virtual_device_device_backing_option_instance = VirtualDeviceDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceDeviceBackingOption.to_json()

# convert the object into a dict
virtual_device_device_backing_option_dict = virtual_device_device_backing_option_instance.to_dict()
# create an instance of VirtualDeviceDeviceBackingOption from a dict
virtual_device_device_backing_option_form_dict = virtual_device_device_backing_option.from_dict(virtual_device_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


