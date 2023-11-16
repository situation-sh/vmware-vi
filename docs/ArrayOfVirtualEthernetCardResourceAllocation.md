# ArrayOfVirtualEthernetCardResourceAllocation

A boxed array of *VirtualEthernetCardResourceAllocation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualEthernetCardResourceAllocation]**](VirtualEthernetCardResourceAllocation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_ethernet_card_resource_allocation import ArrayOfVirtualEthernetCardResourceAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualEthernetCardResourceAllocation from a JSON string
array_of_virtual_ethernet_card_resource_allocation_instance = ArrayOfVirtualEthernetCardResourceAllocation.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualEthernetCardResourceAllocation.to_json()

# convert the object into a dict
array_of_virtual_ethernet_card_resource_allocation_dict = array_of_virtual_ethernet_card_resource_allocation_instance.to_dict()
# create an instance of ArrayOfVirtualEthernetCardResourceAllocation from a dict
array_of_virtual_ethernet_card_resource_allocation_form_dict = array_of_virtual_ethernet_card_resource_allocation.from_dict(array_of_virtual_ethernet_card_resource_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


