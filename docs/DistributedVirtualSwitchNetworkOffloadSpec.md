# DistributedVirtualSwitchNetworkOffloadSpec

Describe the network offload specification of a *VmwareDistributedVirtualSwitch*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the specification.  | 
**name** | **str** | Name of the specification.  | [optional] 
**types** | **List[str]** | DPU types supported in the specification.  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_network_offload_spec import DistributedVirtualSwitchNetworkOffloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchNetworkOffloadSpec from a JSON string
distributed_virtual_switch_network_offload_spec_instance = DistributedVirtualSwitchNetworkOffloadSpec.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchNetworkOffloadSpec.to_json()

# convert the object into a dict
distributed_virtual_switch_network_offload_spec_dict = distributed_virtual_switch_network_offload_spec_instance.to_dict()
# create an instance of DistributedVirtualSwitchNetworkOffloadSpec from a dict
distributed_virtual_switch_network_offload_spec_form_dict = distributed_virtual_switch_network_offload_spec.from_dict(distributed_virtual_switch_network_offload_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


