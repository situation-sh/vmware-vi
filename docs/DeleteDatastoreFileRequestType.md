# DeleteDatastoreFileRequestType

The parameters of *FileManager.DeleteDatastoreFile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file or folder, either a URL or a datastore path referring to the file or folder to be deleted.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.delete_datastore_file_request_type import DeleteDatastoreFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDatastoreFileRequestType from a JSON string
delete_datastore_file_request_type_instance = DeleteDatastoreFileRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteDatastoreFileRequestType.to_json()

# convert the object into a dict
delete_datastore_file_request_type_dict = delete_datastore_file_request_type_instance.to_dict()
# create an instance of DeleteDatastoreFileRequestType from a dict
delete_datastore_file_request_type_form_dict = delete_datastore_file_request_type.from_dict(delete_datastore_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


