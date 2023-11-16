# DeleteDirectoryRequestType

The parameters of *DatastoreNamespaceManager.DeleteDirectory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**datastore_path** | **str** | Stable vmfs path of the directory to delete.  | 

## Example

```python
from vmware_vi.models.delete_directory_request_type import DeleteDirectoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDirectoryRequestType from a JSON string
delete_directory_request_type_instance = DeleteDirectoryRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteDirectoryRequestType.to_json()

# convert the object into a dict
delete_directory_request_type_dict = delete_directory_request_type_instance.to_dict()
# create an instance of DeleteDirectoryRequestType from a dict
delete_directory_request_type_form_dict = delete_directory_request_type.from_dict(delete_directory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


