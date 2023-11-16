# VirtualEthernetCardDVPortBackingOption

This data object type contains the options for using a distributed virtual port virtual network card backing data object type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ethernet_card_dv_port_backing_option import VirtualEthernetCardDVPortBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardDVPortBackingOption from a JSON string
virtual_ethernet_card_dv_port_backing_option_instance = VirtualEthernetCardDVPortBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardDVPortBackingOption.to_json()

# convert the object into a dict
virtual_ethernet_card_dv_port_backing_option_dict = virtual_ethernet_card_dv_port_backing_option_instance.to_dict()
# create an instance of VirtualEthernetCardDVPortBackingOption from a dict
virtual_ethernet_card_dv_port_backing_option_form_dict = virtual_ethernet_card_dv_port_backing_option.from_dict(virtual_ethernet_card_dv_port_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


