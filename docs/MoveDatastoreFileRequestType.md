# MoveDatastoreFileRequestType

The parameters of *FileManager.MoveDatastoreFile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The name of the source, either a URL or a datastore path referring to the file or folder to be moved.  | 
**source_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**destination_name** | **str** | The name of the destination, either a URL or a datastore path referring to the destination file or folder.  | 
**destination_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**force** | **bool** | If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.  | [optional] 

## Example

```python
from vmware_vi.models.move_datastore_file_request_type import MoveDatastoreFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveDatastoreFileRequestType from a JSON string
move_datastore_file_request_type_instance = MoveDatastoreFileRequestType.from_json(json)
# print the JSON string representation of the object
print MoveDatastoreFileRequestType.to_json()

# convert the object into a dict
move_datastore_file_request_type_dict = move_datastore_file_request_type_instance.to_dict()
# create an instance of MoveDatastoreFileRequestType from a dict
move_datastore_file_request_type_form_dict = move_datastore_file_request_type.from_dict(move_datastore_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


