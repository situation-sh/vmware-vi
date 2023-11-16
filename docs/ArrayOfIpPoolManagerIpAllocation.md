# ArrayOfIpPoolManagerIpAllocation

A boxed array of *IpPoolManagerIpAllocation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpPoolManagerIpAllocation]**](IpPoolManagerIpAllocation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_pool_manager_ip_allocation import ArrayOfIpPoolManagerIpAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpPoolManagerIpAllocation from a JSON string
array_of_ip_pool_manager_ip_allocation_instance = ArrayOfIpPoolManagerIpAllocation.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpPoolManagerIpAllocation.to_json()

# convert the object into a dict
array_of_ip_pool_manager_ip_allocation_dict = array_of_ip_pool_manager_ip_allocation_instance.to_dict()
# create an instance of ArrayOfIpPoolManagerIpAllocation from a dict
array_of_ip_pool_manager_ip_allocation_form_dict = array_of_ip_pool_manager_ip_allocation.from_dict(array_of_ip_pool_manager_ip_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


