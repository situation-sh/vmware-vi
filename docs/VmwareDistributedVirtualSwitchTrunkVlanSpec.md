# VmwareDistributedVirtualSwitchTrunkVlanSpec

This data type specifies that the port uses trunk mode, which allows the guest operating system to manage its own VLAN tags.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | [**List[NumericRange]**](NumericRange.md) | The VlanId range for the trunk port.  The valid VlanId range is from 0 to 4094. Overlapping ranges are allowed.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vmware_distributed_virtual_switch_trunk_vlan_spec import VmwareDistributedVirtualSwitchTrunkVlanSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareDistributedVirtualSwitchTrunkVlanSpec from a JSON string
vmware_distributed_virtual_switch_trunk_vlan_spec_instance = VmwareDistributedVirtualSwitchTrunkVlanSpec.from_json(json)
# print the JSON string representation of the object
print VmwareDistributedVirtualSwitchTrunkVlanSpec.to_json()

# convert the object into a dict
vmware_distributed_virtual_switch_trunk_vlan_spec_dict = vmware_distributed_virtual_switch_trunk_vlan_spec_instance.to_dict()
# create an instance of VmwareDistributedVirtualSwitchTrunkVlanSpec from a dict
vmware_distributed_virtual_switch_trunk_vlan_spec_form_dict = vmware_distributed_virtual_switch_trunk_vlan_spec.from_dict(vmware_distributed_virtual_switch_trunk_vlan_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


