# ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec

A boxed array of *VmwareDistributedVirtualSwitchVlanIdSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmwareDistributedVirtualSwitchVlanIdSpec]**](VmwareDistributedVirtualSwitchVlanIdSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmware_distributed_virtual_switch_vlan_id_spec import ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec from a JSON string
array_of_vmware_distributed_virtual_switch_vlan_id_spec_instance = ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec.to_json()

# convert the object into a dict
array_of_vmware_distributed_virtual_switch_vlan_id_spec_dict = array_of_vmware_distributed_virtual_switch_vlan_id_spec_instance.to_dict()
# create an instance of ArrayOfVmwareDistributedVirtualSwitchVlanIdSpec from a dict
array_of_vmware_distributed_virtual_switch_vlan_id_spec_form_dict = array_of_vmware_distributed_virtual_switch_vlan_id_spec.from_dict(array_of_vmware_distributed_virtual_switch_vlan_id_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


