# HostFibreChannelOverEthernetTargetTransport

Fibre Channel Over Ethernet transport information about a SCSI target.  FCoE transport information is that of: the regular FC World Wide Node and Port Names; the VNPort MAC address and FCF MAC address which constitute a VN\\_Port to VF\\_Port Virtual Link; and the VLAN on which an FCoE target resides. More FCoE information can be found in the working draft of the T11's Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnport_mac** | **str** | VNPort MAC address.  This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | 
**fcf_mac** | **str** | FCF MAC address.  This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | 
**vlan_id** | **int** | VLAN ID.  Valid VLAN IDs fall within the range \\[0,4094\\].  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_fibre_channel_over_ethernet_target_transport import HostFibreChannelOverEthernetTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostFibreChannelOverEthernetTargetTransport from a JSON string
host_fibre_channel_over_ethernet_target_transport_instance = HostFibreChannelOverEthernetTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostFibreChannelOverEthernetTargetTransport.to_json()

# convert the object into a dict
host_fibre_channel_over_ethernet_target_transport_dict = host_fibre_channel_over_ethernet_target_transport_instance.to_dict()
# create an instance of HostFibreChannelOverEthernetTargetTransport from a dict
host_fibre_channel_over_ethernet_target_transport_form_dict = host_fibre_channel_over_ethernet_target_transport.from_dict(host_fibre_channel_over_ethernet_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


