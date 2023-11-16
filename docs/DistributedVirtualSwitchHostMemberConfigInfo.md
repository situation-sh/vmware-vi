# DistributedVirtualSwitchHostMemberConfigInfo

The *DistributedVirtualSwitchHostMemberConfigInfo* data object contains membership configuration information for the ESXi host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**max_proxy_switch_ports** | **int** | Maximum number of ports than can be created in the proxy switch.  _ESXi 5.0 and earlier hosts_: If you change the maximum number of ports, you must reboot the host for the new value to take effect.  ***Since:*** vSphere API 4.0  | 
**vendor_specific_config** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**backing** | [**DistributedVirtualSwitchHostMemberBacking**](DistributedVirtualSwitchHostMemberBacking.md) |  | 
**nsx_switch** | **bool** | Indicate whether the proxy switch is used by NSX on this particular host member of the VDS.  ***Since:*** vSphere API 7.0  | [optional] 
**ens_enabled** | **bool** | Indicate if ENS is enabled for this particular host member of the VDS.  It is read only.  ***Since:*** vSphere API 7.0  | [optional] 
**ens_interrupt_enabled** | **bool** | Indicate if ENS interrupt mode is enabled for this particular host member of the VDS.  It is read only.  ***Since:*** vSphere API 7.0  | [optional] 
**transport_zones** | [**List[DistributedVirtualSwitchHostMemberTransportZoneInfo]**](DistributedVirtualSwitchHostMemberTransportZoneInfo.md) | Indicate which transport zones this host joins by this VDS.  ***Since:*** vSphere API 7.0  | [optional] 
**nsxt_used_uplink_names** | **List[str]** | Indicate which uplink ports are used by NSX-T.  ***Since:*** vSphere API 7.0  | [optional] 
**network_offloading_enabled** | **bool** | Indicate if network offloading is enabled for this particular host member of the VDS.  Unset implies that network offloading is disabled.  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_member_config_info import DistributedVirtualSwitchHostMemberConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostMemberConfigInfo from a JSON string
distributed_virtual_switch_host_member_config_info_instance = DistributedVirtualSwitchHostMemberConfigInfo.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostMemberConfigInfo.to_json()

# convert the object into a dict
distributed_virtual_switch_host_member_config_info_dict = distributed_virtual_switch_host_member_config_info_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostMemberConfigInfo from a dict
distributed_virtual_switch_host_member_config_info_form_dict = distributed_virtual_switch_host_member_config_info.from_dict(distributed_virtual_switch_host_member_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


