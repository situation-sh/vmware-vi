# CopyDatastoreFileRequestType

The parameters of *FileManager.CopyDatastoreFile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The name of the source, either a URL or a datastore path referring to the file or folder to be copied.  | 
**source_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**destination_name** | **str** | The name of the destination, either a URL or a datastore path referring to the destination file or folder.  | 
**destination_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**force** | **bool** | If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.  | [optional] 

## Example

```python
from vmware_vi.models.copy_datastore_file_request_type import CopyDatastoreFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CopyDatastoreFileRequestType from a JSON string
copy_datastore_file_request_type_instance = CopyDatastoreFileRequestType.from_json(json)
# print the JSON string representation of the object
print CopyDatastoreFileRequestType.to_json()

# convert the object into a dict
copy_datastore_file_request_type_dict = copy_datastore_file_request_type_instance.to_dict()
# create an instance of CopyDatastoreFileRequestType from a dict
copy_datastore_file_request_type_form_dict = copy_datastore_file_request_type.from_dict(copy_datastore_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


