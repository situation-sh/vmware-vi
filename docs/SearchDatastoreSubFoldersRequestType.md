# SearchDatastoreSubFoldersRequestType

The parameters of *HostDatastoreBrowser.SearchDatastoreSubFolders_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_path** | **str** |  | 
**search_spec** | [**HostDatastoreBrowserSearchSpec**](HostDatastoreBrowserSearchSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.search_datastore_sub_folders_request_type import SearchDatastoreSubFoldersRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDatastoreSubFoldersRequestType from a JSON string
search_datastore_sub_folders_request_type_instance = SearchDatastoreSubFoldersRequestType.from_json(json)
# print the JSON string representation of the object
print SearchDatastoreSubFoldersRequestType.to_json()

# convert the object into a dict
search_datastore_sub_folders_request_type_dict = search_datastore_sub_folders_request_type_instance.to_dict()
# create an instance of SearchDatastoreSubFoldersRequestType from a dict
search_datastore_sub_folders_request_type_form_dict = search_datastore_sub_folders_request_type.from_dict(search_datastore_sub_folders_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


