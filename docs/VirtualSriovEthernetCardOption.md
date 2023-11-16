# VirtualSriovEthernetCardOption

The VirtualSriovEthernetCardOption data object contains the options for the VirtualSriovEthernetCard data object type.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sriov_ethernet_card_option import VirtualSriovEthernetCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSriovEthernetCardOption from a JSON string
virtual_sriov_ethernet_card_option_instance = VirtualSriovEthernetCardOption.from_json(json)
# print the JSON string representation of the object
print VirtualSriovEthernetCardOption.to_json()

# convert the object into a dict
virtual_sriov_ethernet_card_option_dict = virtual_sriov_ethernet_card_option_instance.to_dict()
# create an instance of VirtualSriovEthernetCardOption from a dict
virtual_sriov_ethernet_card_option_form_dict = virtual_sriov_ethernet_card_option.from_dict(virtual_sriov_ethernet_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


