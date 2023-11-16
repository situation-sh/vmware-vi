# ArrayOfVirtualSriovEthernetCard

A boxed array of *VirtualSriovEthernetCard*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSriovEthernetCard]**](VirtualSriovEthernetCard.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_sriov_ethernet_card import ArrayOfVirtualSriovEthernetCard

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSriovEthernetCard from a JSON string
array_of_virtual_sriov_ethernet_card_instance = ArrayOfVirtualSriovEthernetCard.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSriovEthernetCard.to_json()

# convert the object into a dict
array_of_virtual_sriov_ethernet_card_dict = array_of_virtual_sriov_ethernet_card_instance.to_dict()
# create an instance of ArrayOfVirtualSriovEthernetCard from a dict
array_of_virtual_sriov_ethernet_card_form_dict = array_of_virtual_sriov_ethernet_card.from_dict(array_of_virtual_sriov_ethernet_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


