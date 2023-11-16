# MoveIntoFolderRequestType

The parameters of *Folder.MoveIntoFolder_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of objects to be moved into the folder.  Refers instances of *ManagedEntity*.  | 

## Example

```python
from vmware_vi.models.move_into_folder_request_type import MoveIntoFolderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveIntoFolderRequestType from a JSON string
move_into_folder_request_type_instance = MoveIntoFolderRequestType.from_json(json)
# print the JSON string representation of the object
print MoveIntoFolderRequestType.to_json()

# convert the object into a dict
move_into_folder_request_type_dict = move_into_folder_request_type_instance.to_dict()
# create an instance of MoveIntoFolderRequestType from a dict
move_into_folder_request_type_form_dict = move_into_folder_request_type.from_dict(move_into_folder_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


