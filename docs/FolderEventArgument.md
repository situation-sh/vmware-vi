# FolderEventArgument

The event argument is a Folder object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.folder_event_argument import FolderEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderEventArgument from a JSON string
folder_event_argument_instance = FolderEventArgument.from_json(json)
# print the JSON string representation of the object
print FolderEventArgument.to_json()

# convert the object into a dict
folder_event_argument_dict = folder_event_argument_instance.to_dict()
# create an instance of FolderEventArgument from a dict
folder_event_argument_form_dict = folder_event_argument.from_dict(folder_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


