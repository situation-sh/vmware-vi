# HostInternetScsiHbaIPProperties

The IP properties for the host bus adapter 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac** | **str** | The MAC address.  | [optional] 
**address** | **str** | The current IPv4 address.  | [optional] 
**dhcp_configuration_enabled** | **bool** | True if the host bus adapter fetches its IP using DHCP.  | 
**subnet_mask** | **str** | The current IPv4 subnet mask.  | [optional] 
**default_gateway** | **str** | The current IPv4 gateway.  | [optional] 
**primary_dns_server_address** | **str** | The current primary DNS address.  | [optional] 
**alternate_dns_server_address** | **str** | The current secondary DNS address.  | [optional] 
**ipv6_address** | **str** | Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 address.  ***Since:*** vSphere API 4.0  | [optional] 
**ipv6_subnet_mask** | **str** | Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 subnet mask.  ***Since:*** vSphere API 4.0  | [optional] 
**ipv6_default_gateway** | **str** | Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 default gateway.  ***Since:*** vSphere API 4.0  | [optional] 
**arp_redirect_enabled** | **bool** | True if ARP Redirect is enabled  ***Since:*** vSphere API 4.0  | [optional] 
**mtu** | **int** | True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc) Setting enableJumboFrames and not a numeric mtu value implies autoselection of appropriate MTU value for Jumbo Frames.  ***Since:*** vSphere API 4.0  | [optional] 
**jumbo_frames_enabled** | **bool** |  | [optional] 
**ipv4_enabled** | **bool** | True if IPv4 is enabled.  Unset value will keep existing IPv4 enabled state as is.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_enabled** | **bool** | True if IPv6 is enabled.  Unset value will keep existing IPv6 enabled state as is.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6properties** | [**HostInternetScsiHbaIPv6Properties**](HostInternetScsiHbaIPv6Properties.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_ip_properties import HostInternetScsiHbaIPProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaIPProperties from a JSON string
host_internet_scsi_hba_ip_properties_instance = HostInternetScsiHbaIPProperties.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaIPProperties.to_json()

# convert the object into a dict
host_internet_scsi_hba_ip_properties_dict = host_internet_scsi_hba_ip_properties_instance.to_dict()
# create an instance of HostInternetScsiHbaIPProperties from a dict
host_internet_scsi_hba_ip_properties_form_dict = host_internet_scsi_hba_ip_properties.from_dict(host_internet_scsi_hba_ip_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


