# ArrayOfVmwareDistributedVirtualSwitchVlanSpec

A boxed array of *VmwareDistributedVirtualSwitchVlanSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmwareDistributedVirtualSwitchVlanSpec]**](VmwareDistributedVirtualSwitchVlanSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmware_distributed_virtual_switch_vlan_spec import ArrayOfVmwareDistributedVirtualSwitchVlanSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmwareDistributedVirtualSwitchVlanSpec from a JSON string
array_of_vmware_distributed_virtual_switch_vlan_spec_instance = ArrayOfVmwareDistributedVirtualSwitchVlanSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmwareDistributedVirtualSwitchVlanSpec.to_json()

# convert the object into a dict
array_of_vmware_distributed_virtual_switch_vlan_spec_dict = array_of_vmware_distributed_virtual_switch_vlan_spec_instance.to_dict()
# create an instance of ArrayOfVmwareDistributedVirtualSwitchVlanSpec from a dict
array_of_vmware_distributed_virtual_switch_vlan_spec_form_dict = array_of_vmware_distributed_virtual_switch_vlan_spec.from_dict(array_of_vmware_distributed_virtual_switch_vlan_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


