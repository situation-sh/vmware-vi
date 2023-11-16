# VirtualEthernetCardNetworkBackingInfo

The *VirtualEthernetCardNetworkBackingInfo* data object defines network backing for a virtual Ethernet card. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**in_passthrough_mode** | **bool** | Deprecated as of vSphere API 4.0, this property is not supported. &amp;nbsp;.  &amp;nbsp;  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_ethernet_card_network_backing_info import VirtualEthernetCardNetworkBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardNetworkBackingInfo from a JSON string
virtual_ethernet_card_network_backing_info_instance = VirtualEthernetCardNetworkBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardNetworkBackingInfo.to_json()

# convert the object into a dict
virtual_ethernet_card_network_backing_info_dict = virtual_ethernet_card_network_backing_info_instance.to_dict()
# create an instance of VirtualEthernetCardNetworkBackingInfo from a dict
virtual_ethernet_card_network_backing_info_form_dict = virtual_ethernet_card_network_backing_info.from_dict(virtual_ethernet_card_network_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


