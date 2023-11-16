# QueryIPAllocationsRequestType

The parameters of *IpPoolManager.QueryIPAllocations*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool_id** | **int** | The unique ID of the pool  | 
**extension_key** | **str** | The key of the extension  | 

## Example

```python
from vmware_vi.models.query_ip_allocations_request_type import QueryIPAllocationsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryIPAllocationsRequestType from a JSON string
query_ip_allocations_request_type_instance = QueryIPAllocationsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryIPAllocationsRequestType.to_json()

# convert the object into a dict
query_ip_allocations_request_type_dict = query_ip_allocations_request_type_instance.to_dict()
# create an instance of QueryIPAllocationsRequestType from a dict
query_ip_allocations_request_type_form_dict = query_ip_allocations_request_type.from_dict(query_ip_allocations_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


