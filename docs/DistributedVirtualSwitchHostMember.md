# DistributedVirtualSwitchHostMember

The *DistributedVirtualSwitchHostMember* data object represents an ESXi host that is a member of a distributed virtual switch.  When you add a host to a switch (*DistributedVirtualSwitchHostMemberConfigSpec*.*DistributedVirtualSwitchHostMemberConfigSpec.host*), the Server creates a proxy switch (*HostProxySwitch*). The host member object contains information about the configuration and state of the proxy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**runtime_state** | [**DistributedVirtualSwitchHostMemberRuntimeState**](DistributedVirtualSwitchHostMemberRuntimeState.md) |  | [optional] 
**config** | [**DistributedVirtualSwitchHostMemberConfigInfo**](DistributedVirtualSwitchHostMemberConfigInfo.md) |  | 
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 
**uplink_port_key** | **List[str]** | Port keys of the uplink ports created for the host member.  These ports will be deleted after the host leaves the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**status** | **str** | Deprecated as of vSphere API 5.1, use *HostMemberRuntimeInfo*.*HostMemberRuntimeInfo.status* instead.  The host DistributedVirtualSwitch component status.  See *HostComponentState* for valid values.  ***Since:*** vSphere API 4.0  | 
**status_detail** | **str** | Deprecated as of vSphere API 5.1, use *HostMemberRuntimeInfo*.*HostMemberRuntimeInfo.statusDetail* instead.  Additional information regarding the host&#39;s current status.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_member import DistributedVirtualSwitchHostMember

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostMember from a JSON string
distributed_virtual_switch_host_member_instance = DistributedVirtualSwitchHostMember.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostMember.to_json()

# convert the object into a dict
distributed_virtual_switch_host_member_dict = distributed_virtual_switch_host_member_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostMember from a dict
distributed_virtual_switch_host_member_form_dict = distributed_virtual_switch_host_member.from_dict(distributed_virtual_switch_host_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


