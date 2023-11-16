# NetworkProfile

The *NetworkProfile* data object contains a set of subprofiles for network configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vswitch** | [**List[VirtualSwitchProfile]**](VirtualSwitchProfile.md) | List of virtual switch subprofiles.  Use the *VirtualSwitchProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**vm_port_group** | [**List[VmPortGroupProfile]**](VmPortGroupProfile.md) | List of port groups for use by virtual machines.  Use the *VmPortGroupProfile*.*PortGroupProfile.key* property to access a port group in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**host_port_group** | [**List[HostPortGroupProfile]**](HostPortGroupProfile.md) | List of port groups for use by the host.  Use the *HostPortGroupProfile*.*PortGroupProfile.key* property to access port groups in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**service_console_port_group** | [**List[ServiceConsolePortGroupProfile]**](ServiceConsolePortGroupProfile.md) | List of port groups for use by the service console.  The Profile Engine uses this field only when applying a profile to a host that has a service console.  ***Since:*** vSphere API 4.0  | [optional] 
**dns_config** | [**NetworkProfileDnsConfigProfile**](NetworkProfileDnsConfigProfile.md) |  | [optional] 
**ip_route_config** | [**IpRouteProfile**](IpRouteProfile.md) |  | [optional] 
**console_ip_route_config** | [**IpRouteProfile**](IpRouteProfile.md) |  | [optional] 
**pnic** | [**List[PhysicalNicProfile]**](PhysicalNicProfile.md) | List of subprofiles that represent physical NIC configuration.  Use the *PhysicalNicProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**dvswitch** | [**List[DvsProfile]**](DvsProfile.md) | List of subprofiles for distributed virtual switches to which this host is connected.  Use the *DvsProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**dvs_service_console_nic** | [**List[DvsServiceConsoleVNicProfile]**](DvsServiceConsoleVNicProfile.md) | List of subprofiles for service console Virtual NICs connected to a distributed virtual switch.  Use the *DvsServiceConsoleVNicProfile*.*DvsVNicProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**dvs_host_nic** | [**List[DvsHostVNicProfile]**](DvsHostVNicProfile.md) | List of subprofiles for host Virtual NICs connected to a distributed virtual switch.  Use the *DvsHostVNicProfile*.*DvsVNicProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**nsx_host_nic** | [**List[NsxHostVNicProfile]**](NsxHostVNicProfile.md) | List of subprofiles for host Virtual NICs connected to a NSX logic switch.  Use the *NsxHostVNicProfile*.*NsxHostVNicProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 6.7  | [optional] 
**net_stack_instance** | [**List[NetStackInstanceProfile]**](NetStackInstanceProfile.md) | List of NetStackInstance subprofiles.  Use the *NetStackInstanceProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 5.5  | [optional] 
**opaque_switch** | [**OpaqueSwitchProfile**](OpaqueSwitchProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.network_profile import NetworkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProfile from a JSON string
network_profile_instance = NetworkProfile.from_json(json)
# print the JSON string representation of the object
print NetworkProfile.to_json()

# convert the object into a dict
network_profile_dict = network_profile_instance.to_dict()
# create an instance of NetworkProfile from a dict
network_profile_form_dict = network_profile.from_dict(network_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


