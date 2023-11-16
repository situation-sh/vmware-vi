# HostNetworkConfig

This data object type describes networking host configuration data objects.  These objects contain only the configuration information for networking. The runtime information is available from the *NetworkInfo* data object type.  See also *HostNetworkInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch** | [**List[HostVirtualSwitchConfig]**](HostVirtualSwitchConfig.md) | Virtual switches configured on the host.  | [optional] 
**proxy_switch** | [**List[HostProxySwitchConfig]**](HostProxySwitchConfig.md) | Host proxy switches configured on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**portgroup** | [**List[HostPortGroupConfig]**](HostPortGroupConfig.md) | Port groups configured on the host.  | [optional] 
**pnic** | [**List[PhysicalNicConfig]**](PhysicalNicConfig.md) | Physical network adapters as seen by the primary operating system.  | [optional] 
**vnic** | [**List[HostVirtualNicConfig]**](HostVirtualNicConfig.md) | Virtual network adapters configured for use by the host operating system network adapter.  | [optional] 
**console_vnic** | [**List[HostVirtualNicConfig]**](HostVirtualNicConfig.md) | Virtual network adapters configured for use by the Service Console.  | [optional] 
**dns_config** | [**HostDnsConfig**](HostDnsConfig.md) |  | [optional] 
**ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 
**console_ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 
**route_table_config** | [**HostIpRouteTableConfig**](HostIpRouteTableConfig.md) |  | [optional] 
**dhcp** | [**List[HostDhcpServiceConfig]**](HostDhcpServiceConfig.md) | Dynamic Host Control Protocol (DHCP) Service instances configured on the host.  ***Since:*** VI API 2.5  | [optional] 
**nat** | [**List[HostNatServiceConfig]**](HostNatServiceConfig.md) | Network address translation (NAT) Service instances configured on the host.  ***Since:*** VI API 2.5  | [optional] 
**ip_v6_enabled** | **bool** | Enable or disable IPv6 protocol on this system.  This property must be set by itself, no other property can accompany this change. Following the successful change, the system should be rebooted to have the change take effect.  ***Since:*** vSphere API 4.0  | [optional] 
**net_stack_spec** | [**List[HostNetworkConfigNetStackSpec]**](HostNetworkConfigNetStackSpec.md) | The list of network stack instance spec  ***Since:*** vSphere API 5.5  | [optional] 
**migration_status** | **str** | Current status of NVDS to VDS migration.  See *HostNetworkConfig*.*HostNetworkConfigMigrationStatus_enum* for supported values.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.host_network_config import HostNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkConfig from a JSON string
host_network_config_instance = HostNetworkConfig.from_json(json)
# print the JSON string representation of the object
print HostNetworkConfig.to_json()

# convert the object into a dict
host_network_config_dict = host_network_config_instance.to_dict()
# create an instance of HostNetworkConfig from a dict
host_network_config_form_dict = host_network_config.from_dict(host_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


