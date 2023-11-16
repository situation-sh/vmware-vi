# VirtualEthernetCardOpaqueNetworkBackingOption

This data object type contains the options for the virtual network card backing data object type.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ethernet_card_opaque_network_backing_option import VirtualEthernetCardOpaqueNetworkBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardOpaqueNetworkBackingOption from a JSON string
virtual_ethernet_card_opaque_network_backing_option_instance = VirtualEthernetCardOpaqueNetworkBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardOpaqueNetworkBackingOption.to_json()

# convert the object into a dict
virtual_ethernet_card_opaque_network_backing_option_dict = virtual_ethernet_card_opaque_network_backing_option_instance.to_dict()
# create an instance of VirtualEthernetCardOpaqueNetworkBackingOption from a dict
virtual_ethernet_card_opaque_network_backing_option_form_dict = virtual_ethernet_card_opaque_network_backing_option.from_dict(virtual_ethernet_card_opaque_network_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


