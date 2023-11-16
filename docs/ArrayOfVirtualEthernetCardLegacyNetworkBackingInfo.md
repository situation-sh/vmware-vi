# ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo

A boxed array of *VirtualEthernetCardLegacyNetworkBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualEthernetCardLegacyNetworkBackingInfo]**](VirtualEthernetCardLegacyNetworkBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_ethernet_card_legacy_network_backing_info import ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo from a JSON string
array_of_virtual_ethernet_card_legacy_network_backing_info_instance = ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_ethernet_card_legacy_network_backing_info_dict = array_of_virtual_ethernet_card_legacy_network_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualEthernetCardLegacyNetworkBackingInfo from a dict
array_of_virtual_ethernet_card_legacy_network_backing_info_form_dict = array_of_virtual_ethernet_card_legacy_network_backing_info.from_dict(array_of_virtual_ethernet_card_legacy_network_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


