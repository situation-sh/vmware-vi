# IsoImageFileInfo

This data object type describes a file that is an ISO CD-ROM image. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.iso_image_file_info import IsoImageFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IsoImageFileInfo from a JSON string
iso_image_file_info_instance = IsoImageFileInfo.from_json(json)
# print the JSON string representation of the object
print IsoImageFileInfo.to_json()

# convert the object into a dict
iso_image_file_info_dict = iso_image_file_info_instance.to_dict()
# create an instance of IsoImageFileInfo from a dict
iso_image_file_info_form_dict = iso_image_file_info.from_dict(iso_image_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


