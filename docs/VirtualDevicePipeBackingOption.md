# VirtualDevicePipeBackingOption

The <code>*VirtualDevicePipeBackingOption*</code> data object type contains options specific to pipe backings. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_device_pipe_backing_option import VirtualDevicePipeBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDevicePipeBackingOption from a JSON string
virtual_device_pipe_backing_option_instance = VirtualDevicePipeBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDevicePipeBackingOption.to_json()

# convert the object into a dict
virtual_device_pipe_backing_option_dict = virtual_device_pipe_backing_option_instance.to_dict()
# create an instance of VirtualDevicePipeBackingOption from a dict
virtual_device_pipe_backing_option_form_dict = virtual_device_pipe_backing_option.from_dict(virtual_device_pipe_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


