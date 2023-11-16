# FloppyImageFileInfo

This data object type describes a file that is a floppy disk image. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.floppy_image_file_info import FloppyImageFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FloppyImageFileInfo from a JSON string
floppy_image_file_info_instance = FloppyImageFileInfo.from_json(json)
# print the JSON string representation of the object
print FloppyImageFileInfo.to_json()

# convert the object into a dict
floppy_image_file_info_dict = floppy_image_file_info_instance.to_dict()
# create an instance of FloppyImageFileInfo from a dict
floppy_image_file_info_form_dict = floppy_image_file_info.from_dict(floppy_image_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


