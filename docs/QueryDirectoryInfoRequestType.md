# QueryDirectoryInfoRequestType

The parameters of *DatastoreNamespaceManager.QueryDirectoryInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**stable_name** | **str** | stable vmfs path of the top-level directory to query  | 

## Example

```python
from vmware_vi.models.query_directory_info_request_type import QueryDirectoryInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDirectoryInfoRequestType from a JSON string
query_directory_info_request_type_instance = QueryDirectoryInfoRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDirectoryInfoRequestType.to_json()

# convert the object into a dict
query_directory_info_request_type_dict = query_directory_info_request_type_instance.to_dict()
# create an instance of QueryDirectoryInfoRequestType from a dict
query_directory_info_request_type_form_dict = query_directory_info_request_type.from_dict(query_directory_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


