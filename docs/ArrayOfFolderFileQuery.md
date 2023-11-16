# ArrayOfFolderFileQuery

A boxed array of *FolderFileQuery*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderFileQuery]**](FolderFileQuery.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_file_query import ArrayOfFolderFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderFileQuery from a JSON string
array_of_folder_file_query_instance = ArrayOfFolderFileQuery.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderFileQuery.to_json()

# convert the object into a dict
array_of_folder_file_query_dict = array_of_folder_file_query_instance.to_dict()
# create an instance of ArrayOfFolderFileQuery from a dict
array_of_folder_file_query_form_dict = array_of_folder_file_query.from_dict(array_of_folder_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


