# FolderFileQuery

This data object type describes the query specification for a folder (directory). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.folder_file_query import FolderFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FolderFileQuery from a JSON string
folder_file_query_instance = FolderFileQuery.from_json(json)
# print the JSON string representation of the object
print FolderFileQuery.to_json()

# convert the object into a dict
folder_file_query_dict = folder_file_query_instance.to_dict()
# create an instance of FolderFileQuery from a dict
folder_file_query_form_dict = folder_file_query.from_dict(folder_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


