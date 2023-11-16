# HostFibreChannelOverEthernetHbaLinkInfo

Represents FCoE link information.  The link information represents a VNPort to VFPort Virtual Link, as described in the FC-BB-5 standard, with the addition of the VLAN ID over which a link exists.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnport_mac** | **str** | VNPort MAC address, as defined by the FC-BB-5 standard.  This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | 
**fcf_mac** | **str** | FCF MAC address, also known as the VFPort MAC address in the FC-BB-5 standard.  This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | 
**vlan_id** | **int** | VLAN ID.  This field represents the VLAN on which an FCoE HBA was discovered. Valid numbers fall into the range \\[0,4094\\].  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_fibre_channel_over_ethernet_hba_link_info import HostFibreChannelOverEthernetHbaLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFibreChannelOverEthernetHbaLinkInfo from a JSON string
host_fibre_channel_over_ethernet_hba_link_info_instance = HostFibreChannelOverEthernetHbaLinkInfo.from_json(json)
# print the JSON string representation of the object
print HostFibreChannelOverEthernetHbaLinkInfo.to_json()

# convert the object into a dict
host_fibre_channel_over_ethernet_hba_link_info_dict = host_fibre_channel_over_ethernet_hba_link_info_instance.to_dict()
# create an instance of HostFibreChannelOverEthernetHbaLinkInfo from a dict
host_fibre_channel_over_ethernet_hba_link_info_form_dict = host_fibre_channel_over_ethernet_hba_link_info.from_dict(host_fibre_channel_over_ethernet_hba_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


