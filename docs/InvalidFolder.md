# InvalidFolder

An InvalidFolderFault exception is thrown when a node is moved to an invalid place in the hierarchy.  This can be because it is a child of the current node, or a wrong kind of container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.invalid_folder import InvalidFolder

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidFolder from a JSON string
invalid_folder_instance = InvalidFolder.from_json(json)
# print the JSON string representation of the object
print InvalidFolder.to_json()

# convert the object into a dict
invalid_folder_dict = invalid_folder_instance.to_dict()
# create an instance of InvalidFolder from a dict
invalid_folder_form_dict = invalid_folder.from_dict(invalid_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


