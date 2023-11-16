# ArrayOfVirtualEthernetCardOption

A boxed array of *VirtualEthernetCardOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualEthernetCardOption]**](VirtualEthernetCardOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_ethernet_card_option import ArrayOfVirtualEthernetCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualEthernetCardOption from a JSON string
array_of_virtual_ethernet_card_option_instance = ArrayOfVirtualEthernetCardOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualEthernetCardOption.to_json()

# convert the object into a dict
array_of_virtual_ethernet_card_option_dict = array_of_virtual_ethernet_card_option_instance.to_dict()
# create an instance of ArrayOfVirtualEthernetCardOption from a dict
array_of_virtual_ethernet_card_option_form_dict = array_of_virtual_ethernet_card_option.from_dict(array_of_virtual_ethernet_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


