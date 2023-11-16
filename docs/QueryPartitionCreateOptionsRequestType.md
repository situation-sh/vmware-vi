# QueryPartitionCreateOptionsRequestType

The parameters of *HostDiagnosticSystem.QueryPartitionCreateOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | **str** |  | 
**diagnostic_type** | **str** |  | 

## Example

```python
from vmware_vi.models.query_partition_create_options_request_type import QueryPartitionCreateOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPartitionCreateOptionsRequestType from a JSON string
query_partition_create_options_request_type_instance = QueryPartitionCreateOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPartitionCreateOptionsRequestType.to_json()

# convert the object into a dict
query_partition_create_options_request_type_dict = query_partition_create_options_request_type_instance.to_dict()
# create an instance of QueryPartitionCreateOptionsRequestType from a dict
query_partition_create_options_request_type_form_dict = query_partition_create_options_request_type.from_dict(query_partition_create_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


