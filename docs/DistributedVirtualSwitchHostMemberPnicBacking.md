# DistributedVirtualSwitchHostMemberPnicBacking

The *DistributedVirtualSwitchHostMemberPnicBacking* data object specifies a set of physical NICs to use for a proxy switch.  When you add a host to a distributed virtual switch (*DistributedVirtualSwitchHostMemberConfigSpec*.*DistributedVirtualSwitchHostMemberConfigSpec.host*), the host creates a proxy switch that will use the pNICs as uplinks.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_spec** | [**List[DistributedVirtualSwitchHostMemberPnicSpec]**](DistributedVirtualSwitchHostMemberPnicSpec.md) | List of physical NIC specifications.  Each entry identifies a pNIC to the proxy switch and optionally specifies uplink portgroup and port connections for the pNIC.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_member_pnic_backing import DistributedVirtualSwitchHostMemberPnicBacking

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostMemberPnicBacking from a JSON string
distributed_virtual_switch_host_member_pnic_backing_instance = DistributedVirtualSwitchHostMemberPnicBacking.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostMemberPnicBacking.to_json()

# convert the object into a dict
distributed_virtual_switch_host_member_pnic_backing_dict = distributed_virtual_switch_host_member_pnic_backing_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostMemberPnicBacking from a dict
distributed_virtual_switch_host_member_pnic_backing_form_dict = distributed_virtual_switch_host_member_pnic_backing.from_dict(distributed_virtual_switch_host_member_pnic_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


