# QueryVmfsDatastoreExtendOptionsRequestType

The parameters of *HostDatastoreSystem.QueryVmfsDatastoreExtendOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**device_path** | **str** | The devicePath of the disk on which datastore extension options are generated.  | 
**suppress_expand_candidates** | **bool** | Indicates whether to exclude options that can be used for extent expansion also. Free space can be used for adding an extent or expanding an existing extent. If this parameter is set to true, the list of options returned will not include free space that can be used for expansion.  | [optional] 

## Example

```python
from vmware_vi.models.query_vmfs_datastore_extend_options_request_type import QueryVmfsDatastoreExtendOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVmfsDatastoreExtendOptionsRequestType from a JSON string
query_vmfs_datastore_extend_options_request_type_instance = QueryVmfsDatastoreExtendOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVmfsDatastoreExtendOptionsRequestType.to_json()

# convert the object into a dict
query_vmfs_datastore_extend_options_request_type_dict = query_vmfs_datastore_extend_options_request_type_instance.to_dict()
# create an instance of QueryVmfsDatastoreExtendOptionsRequestType from a dict
query_vmfs_datastore_extend_options_request_type_form_dict = query_vmfs_datastore_extend_options_request_type.from_dict(query_vmfs_datastore_extend_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


