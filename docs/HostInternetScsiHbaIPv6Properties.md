# HostInternetScsiHbaIPv6Properties

The IPv6 properties for the host bus adapter.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iscsi_ipv6_address** | [**List[HostInternetScsiHbaIscsiIpv6Address]**](HostInternetScsiHbaIscsiIpv6Address.md) | There can be multiple IPv6 addressed plumbed onto the Host Bus Adapter.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_dhcp_configuration_enabled** | **bool** | True if DHCPv6 is enabled on the host bus adapter.  User can keep this field unset while changing other IPv6 properties without altering current DHCP configuration.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_link_local_auto_configuration_enabled** | **bool** | True if auto configuration of link local address is enabled on the host bus adapter.  User can keep this field unset while changing other IPv6 properties without altering current link local auto configuration.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_router_advertisement_configuration_enabled** | **bool** | True if the router advertisement configuration is enabled on the host bus adapter.  User can keep this field unset while changing other IPv6 properties without altering current router advertisement configuration.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_default_gateway** | **str** | The current IPv6 default gateway.  User can keep this field unset while changing other IPv6 properties without altering current default gateway configuration.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_ipv6_properties import HostInternetScsiHbaIPv6Properties

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaIPv6Properties from a JSON string
host_internet_scsi_hba_ipv6_properties_instance = HostInternetScsiHbaIPv6Properties.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaIPv6Properties.to_json()

# convert the object into a dict
host_internet_scsi_hba_ipv6_properties_dict = host_internet_scsi_hba_ipv6_properties_instance.to_dict()
# create an instance of HostInternetScsiHbaIPv6Properties from a dict
host_internet_scsi_hba_ipv6_properties_form_dict = host_internet_scsi_hba_ipv6_properties.from_dict(host_internet_scsi_hba_ipv6_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


