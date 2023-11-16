# QueryPartitionCreateDescRequestType

The parameters of *HostDiagnosticSystem.QueryPartitionCreateDesc*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_uuid** | **str** |  | 
**diagnostic_type** | **str** |  | 

## Example

```python
from vmware_vi.models.query_partition_create_desc_request_type import QueryPartitionCreateDescRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPartitionCreateDescRequestType from a JSON string
query_partition_create_desc_request_type_instance = QueryPartitionCreateDescRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPartitionCreateDescRequestType.to_json()

# convert the object into a dict
query_partition_create_desc_request_type_dict = query_partition_create_desc_request_type_instance.to_dict()
# create an instance of QueryPartitionCreateDescRequestType from a dict
query_partition_create_desc_request_type_form_dict = query_partition_create_desc_request_type.from_dict(query_partition_create_desc_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


