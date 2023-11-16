# VirtualEthernetCardDistributedVirtualPortBackingInfo

The *VirtualEthernetCardDistributedVirtualPortBackingInfo* data object defines backing for a virtual Ethernet card that connects to a distributed virtual switch port or portgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | [**DistributedVirtualSwitchPortConnection**](DistributedVirtualSwitchPortConnection.md) |  | 

## Example

```python
from vmware_vi.models.virtual_ethernet_card_distributed_virtual_port_backing_info import VirtualEthernetCardDistributedVirtualPortBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardDistributedVirtualPortBackingInfo from a JSON string
virtual_ethernet_card_distributed_virtual_port_backing_info_instance = VirtualEthernetCardDistributedVirtualPortBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardDistributedVirtualPortBackingInfo.to_json()

# convert the object into a dict
virtual_ethernet_card_distributed_virtual_port_backing_info_dict = virtual_ethernet_card_distributed_virtual_port_backing_info_instance.to_dict()
# create an instance of VirtualEthernetCardDistributedVirtualPortBackingInfo from a dict
virtual_ethernet_card_distributed_virtual_port_backing_info_form_dict = virtual_ethernet_card_distributed_virtual_port_backing_info.from_dict(virtual_ethernet_card_distributed_virtual_port_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


