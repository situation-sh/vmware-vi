# HostNetworkInfo

This data object type describes networking host configuration data objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch** | [**List[HostVirtualSwitch]**](HostVirtualSwitch.md) | Virtual switches configured on the host.  | [optional] 
**proxy_switch** | [**List[HostProxySwitch]**](HostProxySwitch.md) | Proxy switches configured on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**portgroup** | [**List[HostPortGroup]**](HostPortGroup.md) | Port groups configured on the host.  | [optional] 
**pnic** | [**List[PhysicalNic]**](PhysicalNic.md) | Physical network adapters as seen by the primary operating system.  | [optional] 
**rdma_device** | [**List[HostRdmaDevice]**](HostRdmaDevice.md) | Remote direct memory access devices, if any are present on the host.  ***Since:*** vSphere API 7.0  | [optional] 
**vnic** | [**List[HostVirtualNic]**](HostVirtualNic.md) | Virtual network adapters configured on the host (hosted products) or the vmkernel.  In the hosted architecture, these network adapters are used by the host to communicate with the virtual machines running on that host. In the VMkernel architecture, these virtual network adapters provide the ESX Server with external network access through a virtual switch that is bridged to a physical network adapter. The VMkernel uses these network adapters for features such as VMotion, NAS, iSCSI, and remote MKS connections.  | [optional] 
**console_vnic** | [**List[HostVirtualNic]**](HostVirtualNic.md) | Virtual network adapters configured for use by the service console.  The service console uses this network access for system management and bootstrapping services like network boot. The two sets of virtual network adapters are mutually exclusive. A virtual network adapter in this list cannot be used for things like VMotion. Likewise, a virtual network adapter in the other list cannot be used by the service console.  | [optional] 
**dns_config** | [**HostDnsConfig**](HostDnsConfig.md) |  | [optional] 
**ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 
**console_ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 
**route_table_info** | [**HostIpRouteTableInfo**](HostIpRouteTableInfo.md) |  | [optional] 
**dhcp** | [**List[HostDhcpService]**](HostDhcpService.md) | DHCP Service instances configured on the host.  ***Since:*** VI API 2.5  | [optional] 
**nat** | [**List[HostNatService]**](HostNatService.md) | NAT service instances configured on the host.  ***Since:*** VI API 2.5  | [optional] 
**ip_v6_enabled** | **bool** | Enable or disable IPv6 protocol on this system.  ***Since:*** vSphere API 4.0  | [optional] 
**at_boot_ip_v6_enabled** | **bool** | If true then dual IPv4/IPv6 stack enabled else IPv4 only.  ***Since:*** vSphere API 4.1  | [optional] 
**net_stack_instance** | [**List[HostNetStackInstance]**](HostNetStackInstance.md) | List of NetStackInstances  ***Since:*** vSphere API 5.5  | [optional] 
**opaque_switch** | [**List[HostOpaqueSwitch]**](HostOpaqueSwitch.md) | List of opaque switches configured on the host.  ***Since:*** vSphere API 5.5  | [optional] 
**opaque_network** | [**List[HostOpaqueNetworkInfo]**](HostOpaqueNetworkInfo.md) | List of opaque networks  ***Since:*** vSphere API 5.5  | [optional] 
**nsx_transport_node_id** | **str** | The nsx transport node Id  ***Since:*** vSphere API 7.0  | [optional] 
**nvds_to_vds_migration_required** | **bool** | Whether NSX N-VDS to VDS migration is required  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**migration_status** | **str** | Current status of NVDS to VDS migration.  See *HostNetworkConfig*.*HostNetworkConfigMigrationStatus_enum* for supported values.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.host_network_info import HostNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkInfo from a JSON string
host_network_info_instance = HostNetworkInfo.from_json(json)
# print the JSON string representation of the object
print HostNetworkInfo.to_json()

# convert the object into a dict
host_network_info_dict = host_network_info_instance.to_dict()
# create an instance of HostNetworkInfo from a dict
host_network_info_form_dict = host_network_info.from_dict(host_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


