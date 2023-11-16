# VirtualFloppyImageBackingOption

The ImageBackingOption data object type contains the options for the floppy image backing type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy_image_backing_option import VirtualFloppyImageBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppyImageBackingOption from a JSON string
virtual_floppy_image_backing_option_instance = VirtualFloppyImageBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualFloppyImageBackingOption.to_json()

# convert the object into a dict
virtual_floppy_image_backing_option_dict = virtual_floppy_image_backing_option_instance.to_dict()
# create an instance of VirtualFloppyImageBackingOption from a dict
virtual_floppy_image_backing_option_form_dict = virtual_floppy_image_backing_option.from_dict(virtual_floppy_image_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


