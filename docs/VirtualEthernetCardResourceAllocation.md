# VirtualEthernetCardResourceAllocation

This class specifies the network resource requirement.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | **int** | Amount of network bandwidth that is guaranteed to the virtual network adapter.  If utilization is less than reservation, the resource can be used by other virtual network adapters. Reservation is not allowed to exceed the value of *VirtualEthernetCardResourceAllocation.limit* if *VirtualEthernetCardResourceAllocation.limit* is set. Units in Mbits/sec.  ***Since:*** vSphere API 6.0  | [optional] 
**share** | [**SharesInfo**](SharesInfo.md) |  | 
**limit** | **int** | The bandwidth limit for the virtual network adapter.  The utilization of the virtual network adapter will not exceed this limit, even if there are available resources. To clear the value of this property and revert it to unset, set the vaule to \&quot;-1\&quot; in an update operation. Units in Mbits/sec.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_ethernet_card_resource_allocation import VirtualEthernetCardResourceAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEthernetCardResourceAllocation from a JSON string
virtual_ethernet_card_resource_allocation_instance = VirtualEthernetCardResourceAllocation.from_json(json)
# print the JSON string representation of the object
print VirtualEthernetCardResourceAllocation.to_json()

# convert the object into a dict
virtual_ethernet_card_resource_allocation_dict = virtual_ethernet_card_resource_allocation_instance.to_dict()
# create an instance of VirtualEthernetCardResourceAllocation from a dict
virtual_ethernet_card_resource_allocation_form_dict = virtual_ethernet_card_resource_allocation.from_dict(virtual_ethernet_card_resource_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


