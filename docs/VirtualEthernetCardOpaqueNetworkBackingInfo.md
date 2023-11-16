# VirtualEthernetCardOpaqueNetworkBackingInfo

This class defines backing for a virtual Ethernet card that connects to an opaque network.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque_network_id** | **str** | The opaque network ID  ***Since:*** vSphere API 5.5  | 
**opaque_network_type** | **str** | The opaque network type  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.virtual_ethernet_card_opaque_network_backing_info import VirtualEthernetCardOpaqueNetworkBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardOpaqueNetworkBackingInfo from a JSON string
virtual_ethernet_card_opaque_network_backing_info_instance = VirtualEthernetCardOpaqueNetworkBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardOpaqueNetworkBackingInfo.to_json()

# convert the object into a dict
virtual_ethernet_card_opaque_network_backing_info_dict = virtual_ethernet_card_opaque_network_backing_info_instance.to_dict()
# create an instance of VirtualEthernetCardOpaqueNetworkBackingInfo from a dict
virtual_ethernet_card_opaque_network_backing_info_form_dict = virtual_ethernet_card_opaque_network_backing_info.from_dict(virtual_ethernet_card_opaque_network_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


