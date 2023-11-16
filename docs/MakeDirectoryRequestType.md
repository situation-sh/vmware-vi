# MakeDirectoryRequestType

The parameters of *FileManager.MakeDirectory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder, either a URL or a datastore path referring to the folder to be created.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**create_parent_directories** | **bool** | If true, any non-existent intermediate level folders will be created. If not specified, it is assumed to be false.  | [optional] 

## Example

```python
from vmware_vi.models.make_directory_request_type import MakeDirectoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MakeDirectoryRequestType from a JSON string
make_directory_request_type_instance = MakeDirectoryRequestType.from_json(json)
# print the JSON string representation of the object
print MakeDirectoryRequestType.to_json()

# convert the object into a dict
make_directory_request_type_dict = make_directory_request_type_instance.to_dict()
# create an instance of MakeDirectoryRequestType from a dict
make_directory_request_type_form_dict = make_directory_request_type.from_dict(make_directory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


