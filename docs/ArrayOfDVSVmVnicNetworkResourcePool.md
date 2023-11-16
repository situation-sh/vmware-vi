# ArrayOfDVSVmVnicNetworkResourcePool

A boxed array of *DVSVmVnicNetworkResourcePool*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSVmVnicNetworkResourcePool]**](DVSVmVnicNetworkResourcePool.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvsvm_vnic_network_resource_pool import ArrayOfDVSVmVnicNetworkResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSVmVnicNetworkResourcePool from a JSON string
array_of_dvsvm_vnic_network_resource_pool_instance = ArrayOfDVSVmVnicNetworkResourcePool.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSVmVnicNetworkResourcePool.to_json()

# convert the object into a dict
array_of_dvsvm_vnic_network_resource_pool_dict = array_of_dvsvm_vnic_network_resource_pool_instance.to_dict()
# create an instance of ArrayOfDVSVmVnicNetworkResourcePool from a dict
array_of_dvsvm_vnic_network_resource_pool_form_dict = array_of_dvsvm_vnic_network_resource_pool.from_dict(array_of_dvsvm_vnic_network_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


