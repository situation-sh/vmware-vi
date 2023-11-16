# VirtualSriovEthernetCard

The *VirtualSriovEthernetCard* data object defines the properties of a SR-IOV enabled Ethernet card attached to a virtual machine.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_guest_os_mtu_change** | **bool** | Indicates whether MTU can be changed from guest OS.  ***Since:*** vSphere API 5.5  | [optional] 
**sriov_backing** | [**VirtualSriovEthernetCardSriovBackingInfo**](VirtualSriovEthernetCardSriovBackingInfo.md) |  | [optional] 
**dvx_backing_info** | [**VirtualPCIPassthroughDvxBackingInfo**](VirtualPCIPassthroughDvxBackingInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_sriov_ethernet_card import VirtualSriovEthernetCard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSriovEthernetCard from a JSON string
virtual_sriov_ethernet_card_instance = VirtualSriovEthernetCard.from_json(json)
# print the JSON string representation of the object
print VirtualSriovEthernetCard.to_json()

# convert the object into a dict
virtual_sriov_ethernet_card_dict = virtual_sriov_ethernet_card_instance.to_dict()
# create an instance of VirtualSriovEthernetCard from a dict
virtual_sriov_ethernet_card_form_dict = virtual_sriov_ethernet_card.from_dict(virtual_sriov_ethernet_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


