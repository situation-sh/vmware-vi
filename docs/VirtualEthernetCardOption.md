# VirtualEthernetCardOption

This data object type contains the options for the virtual ethernet card data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_oui** | [**ChoiceOption**](ChoiceOption.md) |  | 
**mac_type** | [**ChoiceOption**](ChoiceOption.md) |  | 
**wake_on_lan_enabled** | [**BoolOption**](BoolOption.md) |  | 
**vm_direct_path_gen2_supported** | **bool** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Flag to indicate whether VMDirectPath Gen 2 is available on this device.  ***Since:*** vSphere API 4.1  | [optional] 
**upt_compatibility_enabled** | [**BoolOption**](BoolOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_ethernet_card_option import VirtualEthernetCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardOption from a JSON string
virtual_ethernet_card_option_instance = VirtualEthernetCardOption.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardOption.to_json()

# convert the object into a dict
virtual_ethernet_card_option_dict = virtual_ethernet_card_option_instance.to_dict()
# create an instance of VirtualEthernetCardOption from a dict
virtual_ethernet_card_option_form_dict = virtual_ethernet_card_option.from_dict(virtual_ethernet_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


