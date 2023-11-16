# HostNetCapabilities

Capability vector indicating the available product features. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_set_physical_nic_link_speed** | **bool** | The flag to indicate whether or not a physical network adapter&#39;s link speed and duplex settings can be changed through this API.  For a hosted product, the host uses its physical network adapters for network connectivity. Configuration of link speed is done through regular host operations. In ESX Server, the configuration can be changed through this API.  | 
**supports_nic_teaming** | **bool** | The flag to indicate whether or not network adapter teaming is available.  Multiple network adapters can be bridged to a virtual switch through a BondBridge. Also, network adapter teaming policies such as failover order and detection are enabled.  | 
**nic_teaming_policy** | **List[str]** | The available teaming policies if the platform supports network adapter teaming.  | [optional] 
**supports_vlan** | **bool** | The flag to indicate whether or not VLANs can be configured on PortGroups attached to VirtualSwitch objects.  This allows VLANs for virtual machines without requiring special VLAN capable hardware switches.  | 
**uses_service_console_nic** | **bool** | The flag to indicate whether or not a service console network adapter is used or required.  This means that the system software has two TCP/IP stacks. As a result, at least two types of VirtualNics may be created -- the normal VirtualNic and the service console VirtualNic. If this is not set, then only the VirtualNic type is supported.  | 
**supports_network_hints** | **bool** | The flag to indicate whether or not the host is able to support the querying of network hints.  | 
**max_port_groups_per_vswitch** | **int** | The maximum number of port groups supported per virtual switch.  This property will not be set if this value is unlimited.  ***Since:*** VI API 2.5  | [optional] 
**vswitch_config_supported** | **bool** | The flag to indicate whether virtual switch configuration is supported.  This means that operations to add, remove, update virtual switches are supported.  ***Since:*** VI API 2.5  | 
**vnic_config_supported** | **bool** | The flag to indicate whether Virtual NIC configuration is supported.  This means that operations to add, remove, update virtualNic are supported.  ***Since:*** VI API 2.5  | 
**ip_route_config_supported** | **bool** | The flag to indicate whether ip route configuration for the host is supported.  ***Since:*** VI API 2.5  | 
**dns_config_supported** | **bool** | The flag to indicate whether DNS configuration for the host is supported.  ***Since:*** VI API 2.5  | 
**dhcp_on_vnic_supported** | **bool** | This flag indicates whether or not the host is able to support dhcp configuration for vnics.  ***Since:*** VI API 2.5  | 
**ip_v6_supported** | **bool** | The flag to indicate whether the host is capable of communicating using ipv6 protocol  ***Since:*** vSphere API 4.0  | 
**backup_nfc_nioc_supported** | **bool** | The flag to indicate whether the host supports Backup NFC NIOC system traffic, Unset means Backup NFC NIOC system traffic is not supported.  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.host_net_capabilities import HostNetCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetCapabilities from a JSON string
host_net_capabilities_instance = HostNetCapabilities.from_json(json)
# print the JSON string representation of the object
print HostNetCapabilities.to_json()

# convert the object into a dict
host_net_capabilities_dict = host_net_capabilities_instance.to_dict()
# create an instance of HostNetCapabilities from a dict
host_net_capabilities_form_dict = host_net_capabilities.from_dict(host_net_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


