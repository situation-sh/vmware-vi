# ArrayOfFolderNewHostSpec

A boxed array of *FolderNewHostSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderNewHostSpec]**](FolderNewHostSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_new_host_spec import ArrayOfFolderNewHostSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderNewHostSpec from a JSON string
array_of_folder_new_host_spec_instance = ArrayOfFolderNewHostSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderNewHostSpec.to_json()

# convert the object into a dict
array_of_folder_new_host_spec_dict = array_of_folder_new_host_spec_instance.to_dict()
# create an instance of ArrayOfFolderNewHostSpec from a dict
array_of_folder_new_host_spec_form_dict = array_of_folder_new_host_spec.from_dict(array_of_folder_new_host_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


