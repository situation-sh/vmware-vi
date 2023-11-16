# HostProxySwitch

The HostProxySwitch is a software entity which represents the component of a DistributedVirtualSwitch on a particular host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_uuid** | **str** | The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.  ***Since:*** vSphere API 4.0  | 
**dvs_name** | **str** | The name of the DistributedVirtualSwitch that the HostProxySwitch is part of.  ***Since:*** vSphere API 4.0  | 
**key** | **str** | The proxy switch key.  ***Since:*** vSphere API 4.0  | 
**num_ports** | **int** | The number of ports that this switch currently has.  ***Since:*** vSphere API 4.0  | 
**config_num_ports** | **int** | The configured number of ports that this switch has.  If configured number of ports is changed, a host reboot is required for the new value to take effect.  ***Since:*** vSphere API 5.0  | [optional] 
**num_ports_available** | **int** | The number of ports that are available on this virtual switch.  ***Since:*** vSphere API 4.0  | 
**uplink_port** | [**List[KeyValue]**](KeyValue.md) | The list of ports that can be potentially used by physical nics.  This property contains the keys and names of such ports.  ***Since:*** vSphere API 4.0  | [optional] 
**mtu** | **int** | The maximum transmission unit (MTU) associated with this switch in bytes.  ***Since:*** vSphere API 4.0  | [optional] 
**pnic** | [**List[PhysicalNic]**](PhysicalNic.md) | The set of physical network adapters associated with this switch.  ***Since:*** vSphere API 4.0  | [optional] 
**spec** | [**HostProxySwitchSpec**](HostProxySwitchSpec.md) |  | 
**host_lag** | [**List[HostProxySwitchHostLagConfig]**](HostProxySwitchHostLagConfig.md) | The Link Aggregation Control Protocol group and Uplink ports in the group.  ***Since:*** vSphere API 5.5  | [optional] 
**network_reservation_supported** | **bool** | Indicates whether network reservation is supported on this switch  ***Since:*** vSphere API 5.5  | [optional] 
**nsxt_enabled** | **bool** | Indicate whether NSX-T is enabled on this switch  ***Since:*** vSphere API 7.0  | [optional] 
**ens_enabled** | **bool** | Is ENS enabled on this switch  ***Since:*** vSphere API 7.0  | [optional] 
**ens_interrupt_enabled** | **bool** | Is ENS interrupt mode enabled on this switch  ***Since:*** vSphere API 7.0  | [optional] 
**transport_zones** | [**List[DistributedVirtualSwitchHostMemberTransportZoneInfo]**](DistributedVirtualSwitchHostMemberTransportZoneInfo.md) | Transport Zones this switch joined  ***Since:*** vSphere API 7.0  | [optional] 
**nsx_used_uplink_port** | **List[str]** | Uplink port names used by NSX-T  ***Since:*** vSphere API 7.0  | [optional] 
**nsxt_status** | **str** | NSX-T proxy switch status  ***Since:*** vSphere API 7.0  | [optional] 
**nsxt_status_detail** | **str** | Additional information regarding the NSX-T proxy switch status  ***Since:*** vSphere API 7.0  | [optional] 
**ens_info** | [**HostProxySwitchEnsInfo**](HostProxySwitchEnsInfo.md) |  | [optional] 
**network_offloading_enabled** | **bool** | Indicate if network offloading is enabled on the proxy switch of this host.  Unset implies that network offloading is disabled.  | [optional] 

## Example

```python
from vmware_vi.models.host_proxy_switch import HostProxySwitch

# TODO update the JSON string below
json = "{}"
# create an instance of HostProxySwitch from a JSON string
host_proxy_switch_instance = HostProxySwitch.from_json(json)
# print the JSON string representation of the object
print HostProxySwitch.to_json()

# convert the object into a dict
host_proxy_switch_dict = host_proxy_switch_instance.to_dict()
# create an instance of HostProxySwitch from a dict
host_proxy_switch_form_dict = host_proxy_switch.from_dict(host_proxy_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


