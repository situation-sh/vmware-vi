# QueryVmfsDatastoreCreateOptionsRequestType

The parameters of *HostDatastoreSystem.QueryVmfsDatastoreCreateOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The devicePath of the disk on which datastore creation options are generated.  | 
**vmfs_major_version** | **int** | major version of VMFS to be used for formatting the datastore. If this parameter is not specified, then the highest *supported VMFS major version* for the host is used.  | [optional] 

## Example

```python
from vmware_vi.models.query_vmfs_datastore_create_options_request_type import QueryVmfsDatastoreCreateOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVmfsDatastoreCreateOptionsRequestType from a JSON string
query_vmfs_datastore_create_options_request_type_instance = QueryVmfsDatastoreCreateOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVmfsDatastoreCreateOptionsRequestType.to_json()

# convert the object into a dict
query_vmfs_datastore_create_options_request_type_dict = query_vmfs_datastore_create_options_request_type_instance.to_dict()
# create an instance of QueryVmfsDatastoreCreateOptionsRequestType from a dict
query_vmfs_datastore_create_options_request_type_form_dict = query_vmfs_datastore_create_options_request_type.from_dict(query_vmfs_datastore_create_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


