# AllocateIpv6AddressRequestType

The parameters of *IpPoolManager.AllocateIpv6Address*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool_id** | **int** | The unique ID of the pool  | 
**allocation_id** | **str** | The unique ID for this allocation  | 

## Example

```python
from vmware_vi.models.allocate_ipv6_address_request_type import AllocateIpv6AddressRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AllocateIpv6AddressRequestType from a JSON string
allocate_ipv6_address_request_type_instance = AllocateIpv6AddressRequestType.from_json(json)
# print the JSON string representation of the object
print AllocateIpv6AddressRequestType.to_json()

# convert the object into a dict
allocate_ipv6_address_request_type_dict = allocate_ipv6_address_request_type_instance.to_dict()
# create an instance of AllocateIpv6AddressRequestType from a dict
allocate_ipv6_address_request_type_form_dict = allocate_ipv6_address_request_type.from_dict(allocate_ipv6_address_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


