# VirtualSriovEthernetCardSriovBackingOption

This data object contains the option for SriovBackingInfo data of the virtual network SR-IOV card object type.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sriov_ethernet_card_sriov_backing_option import VirtualSriovEthernetCardSriovBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSriovEthernetCardSriovBackingOption from a JSON string
virtual_sriov_ethernet_card_sriov_backing_option_instance = VirtualSriovEthernetCardSriovBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualSriovEthernetCardSriovBackingOption.to_json()

# convert the object into a dict
virtual_sriov_ethernet_card_sriov_backing_option_dict = virtual_sriov_ethernet_card_sriov_backing_option_instance.to_dict()
# create an instance of VirtualSriovEthernetCardSriovBackingOption from a dict
virtual_sriov_ethernet_card_sriov_backing_option_form_dict = virtual_sriov_ethernet_card_sriov_backing_option.from_dict(virtual_sriov_ethernet_card_sriov_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


