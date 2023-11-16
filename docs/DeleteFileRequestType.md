# DeleteFileRequestType

The parameters of *HostDatastoreBrowser.DeleteFile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_path** | **str** |  | 

## Example

```python
from vmware_vi.models.delete_file_request_type import DeleteFileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFileRequestType from a JSON string
delete_file_request_type_instance = DeleteFileRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteFileRequestType.to_json()

# convert the object into a dict
delete_file_request_type_dict = delete_file_request_type_instance.to_dict()
# create an instance of DeleteFileRequestType from a dict
delete_file_request_type_form_dict = delete_file_request_type.from_dict(delete_file_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


