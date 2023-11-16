# QueryIpPoolsRequestType

The parameters of *IpPoolManager.QueryIpPools*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_ip_pools_request_type import QueryIpPoolsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryIpPoolsRequestType from a JSON string
query_ip_pools_request_type_instance = QueryIpPoolsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryIpPoolsRequestType.to_json()

# convert the object into a dict
query_ip_pools_request_type_dict = query_ip_pools_request_type_instance.to_dict()
# create an instance of QueryIpPoolsRequestType from a dict
query_ip_pools_request_type_form_dict = query_ip_pools_request_type.from_dict(query_ip_pools_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


