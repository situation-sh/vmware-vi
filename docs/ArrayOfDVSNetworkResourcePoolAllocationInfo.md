# ArrayOfDVSNetworkResourcePoolAllocationInfo

A boxed array of *DVSNetworkResourcePoolAllocationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSNetworkResourcePoolAllocationInfo]**](DVSNetworkResourcePoolAllocationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_network_resource_pool_allocation_info import ArrayOfDVSNetworkResourcePoolAllocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSNetworkResourcePoolAllocationInfo from a JSON string
array_of_dvs_network_resource_pool_allocation_info_instance = ArrayOfDVSNetworkResourcePoolAllocationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSNetworkResourcePoolAllocationInfo.to_json()

# convert the object into a dict
array_of_dvs_network_resource_pool_allocation_info_dict = array_of_dvs_network_resource_pool_allocation_info_instance.to_dict()
# create an instance of ArrayOfDVSNetworkResourcePoolAllocationInfo from a dict
array_of_dvs_network_resource_pool_allocation_info_form_dict = array_of_dvs_network_resource_pool_allocation_info.from_dict(array_of_dvs_network_resource_pool_allocation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


