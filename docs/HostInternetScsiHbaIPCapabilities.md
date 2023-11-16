# HostInternetScsiHbaIPCapabilities

The IP Capabilities for the host bus adapter 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_settable** | **bool** | True if the host bus adapter supports setting its IPv4 address.  | 
**ip_configuration_method_settable** | **bool** | True if the host bus adapter supports DHCPv4.  | 
**subnet_mask_settable** | **bool** | True if the host bus adapter supports setting its IPv4 subnet mask.  | 
**default_gateway_settable** | **bool** | True if the host bus adapter supports setting its IPv4 gateway.  | 
**primary_dns_server_address_settable** | **bool** | True if the host bus adapter supports setting its primary DNS.  | 
**alternate_dns_server_address_settable** | **bool** | True if the host bus adapter supports setting its secondary DNS.  | 
**ipv6_supported** | **bool** | True if the host bus adapter supports the use of IPv6 addresses  ***Since:*** vSphere API 4.0  | [optional] 
**arp_redirect_settable** | **bool** | True if the host bus adapter supports setting its ARP Redirect value  ***Since:*** vSphere API 4.0  | [optional] 
**mtu_settable** | **bool** | True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)  ***Since:*** vSphere API 4.0  | [optional] 
**host_name_as_target_address** | **bool** | True if the discovery and static targets can be configured with a host name as opposed to an IP address.  ***Since:*** vSphere API 4.0  | [optional] 
**name_alias_settable** | **bool** | True if the host bus adapter supports setting its name and alias  ***Since:*** vSphere API 4.1  | [optional] 
**ipv4_enable_settable** | **bool** | True if IPv4 addresssing can be enabled or disabled on the host bus adapter.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_enable_settable** | **bool** | True if IPv6 addresssing can be enabled or disabled on the host bus adapter.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_prefix_length_settable** | **bool** | True if the Host bus adapter supports setting IPv6 Prefix Length.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_prefix_length** | **int** | Provides the value that user should be using if host bus adapter does not support changing of prefix length.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_dhcp_configuration_settable** | **bool** | True if the Host bus adapter supports DHCPv6 configuration.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_link_local_auto_configuration_settable** | **bool** | True if the Host bus adapter supports setting configuration of its IPv6 link local address User can specify link local static address if link local auto configuration is set to false.  link local address usually starts with fe80: and has prefix 64.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_router_advertisement_configuration_settable** | **bool** | True if the Host bus adapter supports router advertisement configuration method.  Note: Currently Qlogic adapter does not support plumbing of any user specified static address if router advertisement method is enabled.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_default_gateway_settable** | **bool** | True if the Host bus adapter supports setting its IPv6 default gateway.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_max_static_addresses_supported** | **int** | The maximum number of supported IPv6 static addresses on the host bus adapter that user can set.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_ip_capabilities import HostInternetScsiHbaIPCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaIPCapabilities from a JSON string
host_internet_scsi_hba_ip_capabilities_instance = HostInternetScsiHbaIPCapabilities.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaIPCapabilities.to_json()

# convert the object into a dict
host_internet_scsi_hba_ip_capabilities_dict = host_internet_scsi_hba_ip_capabilities_instance.to_dict()
# create an instance of HostInternetScsiHbaIPCapabilities from a dict
host_internet_scsi_hba_ip_capabilities_form_dict = host_internet_scsi_hba_ip_capabilities.from_dict(host_internet_scsi_hba_ip_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


