# AllocateIpv4AddressRequestType

The parameters of *IpPoolManager.AllocateIpv4Address*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool_id** | **int** | The unique ID of the pool  | 
**allocation_id** | **str** | The unique ID for this allocation  | 

## Example

```python
from vmware_vi.models.allocate_ipv4_address_request_type import AllocateIpv4AddressRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AllocateIpv4AddressRequestType from a JSON string
allocate_ipv4_address_request_type_instance = AllocateIpv4AddressRequestType.from_json(json)
# print the JSON string representation of the object
print AllocateIpv4AddressRequestType.to_json()

# convert the object into a dict
allocate_ipv4_address_request_type_dict = allocate_ipv4_address_request_type_instance.to_dict()
# create an instance of AllocateIpv4AddressRequestType from a dict
allocate_ipv4_address_request_type_form_dict = allocate_ipv4_address_request_type.from_dict(allocate_ipv4_address_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


