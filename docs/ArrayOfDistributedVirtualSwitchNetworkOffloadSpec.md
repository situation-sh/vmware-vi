# ArrayOfDistributedVirtualSwitchNetworkOffloadSpec

A boxed array of *DistributedVirtualSwitchNetworkOffloadSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchNetworkOffloadSpec]**](DistributedVirtualSwitchNetworkOffloadSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_network_offload_spec import ArrayOfDistributedVirtualSwitchNetworkOffloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchNetworkOffloadSpec from a JSON string
array_of_distributed_virtual_switch_network_offload_spec_instance = ArrayOfDistributedVirtualSwitchNetworkOffloadSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchNetworkOffloadSpec.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_network_offload_spec_dict = array_of_distributed_virtual_switch_network_offload_spec_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchNetworkOffloadSpec from a dict
array_of_distributed_virtual_switch_network_offload_spec_form_dict = array_of_distributed_virtual_switch_network_offload_spec.from_dict(array_of_distributed_virtual_switch_network_offload_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


