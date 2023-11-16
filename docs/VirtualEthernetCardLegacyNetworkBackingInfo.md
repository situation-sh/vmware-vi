# VirtualEthernetCardLegacyNetworkBackingInfo

The *VirtualEthernetCardLegacyNetworkBackingInfo* data object provides legacy backing for a virtual Ethernet card. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ethernet_card_legacy_network_backing_info import VirtualEthernetCardLegacyNetworkBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardLegacyNetworkBackingInfo from a JSON string
virtual_ethernet_card_legacy_network_backing_info_instance = VirtualEthernetCardLegacyNetworkBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardLegacyNetworkBackingInfo.to_json()

# convert the object into a dict
virtual_ethernet_card_legacy_network_backing_info_dict = virtual_ethernet_card_legacy_network_backing_info_instance.to_dict()
# create an instance of VirtualEthernetCardLegacyNetworkBackingInfo from a dict
virtual_ethernet_card_legacy_network_backing_info_form_dict = virtual_ethernet_card_legacy_network_backing_info.from_dict(virtual_ethernet_card_legacy_network_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


