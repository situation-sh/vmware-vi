# VirtualDeviceFileBackingOption

The FileBackingOption data class contains file-specific backing options. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name_extensions** | [**ChoiceOption**](ChoiceOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_file_backing_option import VirtualDeviceFileBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceFileBackingOption from a JSON string
virtual_device_file_backing_option_instance = VirtualDeviceFileBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceFileBackingOption.to_json()

# convert the object into a dict
virtual_device_file_backing_option_dict = virtual_device_file_backing_option_instance.to_dict()
# create an instance of VirtualDeviceFileBackingOption from a dict
virtual_device_file_backing_option_form_dict = virtual_device_file_backing_option.from_dict(virtual_device_file_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


