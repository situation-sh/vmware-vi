# VmwareDistributedVirtualSwitchVlanIdSpec

This data type defines the configuration when single vlanId is used for the port.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | The VLAN ID for ports.  Possible values: - A value of 0 specifies that you do not want the port associated   with a VLAN. - A value from 1 to 4094 specifies a VLAN ID for the port.      ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vmware_distributed_virtual_switch_vlan_id_spec import VmwareDistributedVirtualSwitchVlanIdSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareDistributedVirtualSwitchVlanIdSpec from a JSON string
vmware_distributed_virtual_switch_vlan_id_spec_instance = VmwareDistributedVirtualSwitchVlanIdSpec.from_json(json)
# print the JSON string representation of the object
print VmwareDistributedVirtualSwitchVlanIdSpec.to_json()

# convert the object into a dict
vmware_distributed_virtual_switch_vlan_id_spec_dict = vmware_distributed_virtual_switch_vlan_id_spec_instance.to_dict()
# create an instance of VmwareDistributedVirtualSwitchVlanIdSpec from a dict
vmware_distributed_virtual_switch_vlan_id_spec_form_dict = vmware_distributed_virtual_switch_vlan_id_spec.from_dict(vmware_distributed_virtual_switch_vlan_id_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


