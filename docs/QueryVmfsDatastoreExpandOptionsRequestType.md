# QueryVmfsDatastoreExpandOptionsRequestType

The parameters of *HostDatastoreSystem.QueryVmfsDatastoreExpandOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_vmfs_datastore_expand_options_request_type import QueryVmfsDatastoreExpandOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVmfsDatastoreExpandOptionsRequestType from a JSON string
query_vmfs_datastore_expand_options_request_type_instance = QueryVmfsDatastoreExpandOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVmfsDatastoreExpandOptionsRequestType.to_json()

# convert the object into a dict
query_vmfs_datastore_expand_options_request_type_dict = query_vmfs_datastore_expand_options_request_type_instance.to_dict()
# create an instance of QueryVmfsDatastoreExpandOptionsRequestType from a dict
query_vmfs_datastore_expand_options_request_type_form_dict = query_vmfs_datastore_expand_options_request_type.from_dict(query_vmfs_datastore_expand_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


