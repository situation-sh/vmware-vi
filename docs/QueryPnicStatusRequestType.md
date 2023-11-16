# QueryPnicStatusRequestType

The parameters of *IscsiManager.QueryPnicStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_device** | **str** | Physical NIC device name to check the status for  | 

## Example

```python
from vmware_vi.models.query_pnic_status_request_type import QueryPnicStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPnicStatusRequestType from a JSON string
query_pnic_status_request_type_instance = QueryPnicStatusRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPnicStatusRequestType.to_json()

# convert the object into a dict
query_pnic_status_request_type_dict = query_pnic_status_request_type_instance.to_dict()
# create an instance of QueryPnicStatusRequestType from a dict
query_pnic_status_request_type_form_dict = query_pnic_status_request_type.from_dict(query_pnic_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


