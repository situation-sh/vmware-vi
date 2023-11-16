# VmwareDistributedVirtualSwitchPvlanSpec

This data type defines the configuration when PVLAN id is to be used for the ports.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pvlan_id** | **int** | The *VMwareDVSPvlanMapEntry.secondaryVlanId*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vmware_distributed_virtual_switch_pvlan_spec import VmwareDistributedVirtualSwitchPvlanSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareDistributedVirtualSwitchPvlanSpec from a JSON string
vmware_distributed_virtual_switch_pvlan_spec_instance = VmwareDistributedVirtualSwitchPvlanSpec.from_json(json)
# print the JSON string representation of the object
print VmwareDistributedVirtualSwitchPvlanSpec.to_json()

# convert the object into a dict
vmware_distributed_virtual_switch_pvlan_spec_dict = vmware_distributed_virtual_switch_pvlan_spec_instance.to_dict()
# create an instance of VmwareDistributedVirtualSwitchPvlanSpec from a dict
vmware_distributed_virtual_switch_pvlan_spec_form_dict = vmware_distributed_virtual_switch_pvlan_spec.from_dict(vmware_distributed_virtual_switch_pvlan_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


