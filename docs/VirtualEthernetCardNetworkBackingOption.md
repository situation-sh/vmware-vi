# VirtualEthernetCardNetworkBackingOption

This data object type contains the options for the virtual network card backing data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ethernet_card_network_backing_option import VirtualEthernetCardNetworkBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardNetworkBackingOption from a JSON string
virtual_ethernet_card_network_backing_option_instance = VirtualEthernetCardNetworkBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardNetworkBackingOption.to_json()

# convert the object into a dict
virtual_ethernet_card_network_backing_option_dict = virtual_ethernet_card_network_backing_option_instance.to_dict()
# create an instance of VirtualEthernetCardNetworkBackingOption from a dict
virtual_ethernet_card_network_backing_option_form_dict = virtual_ethernet_card_network_backing_option.from_dict(virtual_ethernet_card_network_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


