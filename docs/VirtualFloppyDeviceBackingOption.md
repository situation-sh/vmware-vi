# VirtualFloppyDeviceBackingOption

The DeviceBackingOption data object type contains the options for the floppy device backing type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy_device_backing_option import VirtualFloppyDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppyDeviceBackingOption from a JSON string
virtual_floppy_device_backing_option_instance = VirtualFloppyDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualFloppyDeviceBackingOption.to_json()

# convert the object into a dict
virtual_floppy_device_backing_option_dict = virtual_floppy_device_backing_option_instance.to_dict()
# create an instance of VirtualFloppyDeviceBackingOption from a dict
virtual_floppy_device_backing_option_form_dict = virtual_floppy_device_backing_option.from_dict(virtual_floppy_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


