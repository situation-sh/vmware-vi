# ArrayOfFolderEventArgument

A boxed array of *FolderEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderEventArgument]**](FolderEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_event_argument import ArrayOfFolderEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderEventArgument from a JSON string
array_of_folder_event_argument_instance = ArrayOfFolderEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderEventArgument.to_json()

# convert the object into a dict
array_of_folder_event_argument_dict = array_of_folder_event_argument_instance.to_dict()
# create an instance of ArrayOfFolderEventArgument from a dict
array_of_folder_event_argument_form_dict = array_of_folder_event_argument.from_dict(array_of_folder_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


