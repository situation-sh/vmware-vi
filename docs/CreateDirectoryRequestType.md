# CreateDirectoryRequestType

The parameters of *DatastoreNamespaceManager.CreateDirectory*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**display_name** | **str** | display name hint for the directory to create  | [optional] 
**policy** | **str** | opaque storage policy to associate with the directory  | [optional] 
**size** | **int** | directory size in MB on vvol/vsan backed object storage. default directory size will be used for vsan backed object storage if not set.  | [optional] 

## Example

```python
from vmware_vi.models.create_directory_request_type import CreateDirectoryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDirectoryRequestType from a JSON string
create_directory_request_type_instance = CreateDirectoryRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDirectoryRequestType.to_json()

# convert the object into a dict
create_directory_request_type_dict = create_directory_request_type_instance.to_dict()
# create an instance of CreateDirectoryRequestType from a dict
create_directory_request_type_form_dict = create_directory_request_type.from_dict(create_directory_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


