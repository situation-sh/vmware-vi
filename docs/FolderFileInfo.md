# FolderFileInfo

This data object type describes a file that is a folder (directory). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.folder_file_info import FolderFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FolderFileInfo from a JSON string
folder_file_info_instance = FolderFileInfo.from_json(json)
# print the JSON string representation of the object
print FolderFileInfo.to_json()

# convert the object into a dict
folder_file_info_dict = folder_file_info_instance.to_dict()
# create an instance of FolderFileInfo from a dict
folder_file_info_form_dict = folder_file_info.from_dict(folder_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


