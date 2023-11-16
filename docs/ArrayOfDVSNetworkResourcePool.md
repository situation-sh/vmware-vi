# ArrayOfDVSNetworkResourcePool

A boxed array of *DVSNetworkResourcePool*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSNetworkResourcePool]**](DVSNetworkResourcePool.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_network_resource_pool import ArrayOfDVSNetworkResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSNetworkResourcePool from a JSON string
array_of_dvs_network_resource_pool_instance = ArrayOfDVSNetworkResourcePool.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSNetworkResourcePool.to_json()

# convert the object into a dict
array_of_dvs_network_resource_pool_dict = array_of_dvs_network_resource_pool_instance.to_dict()
# create an instance of ArrayOfDVSNetworkResourcePool from a dict
array_of_dvs_network_resource_pool_form_dict = array_of_dvs_network_resource_pool.from_dict(array_of_dvs_network_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


