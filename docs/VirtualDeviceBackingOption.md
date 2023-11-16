# VirtualDeviceBackingOption

The *VirtualDeviceBackingOption* data class defines options for device-specific virtual backing objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The name of the class the client should use to instantiate backing for the virtual device.  | 

## Example

```python
from vmware_vi.models.virtual_device_backing_option import VirtualDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceBackingOption from a JSON string
virtual_device_backing_option_instance = VirtualDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceBackingOption.to_json()

# convert the object into a dict
virtual_device_backing_option_dict = virtual_device_backing_option_instance.to_dict()
# create an instance of VirtualDeviceBackingOption from a dict
virtual_device_backing_option_form_dict = virtual_device_backing_option.from_dict(virtual_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


