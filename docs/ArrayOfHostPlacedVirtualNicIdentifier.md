# ArrayOfHostPlacedVirtualNicIdentifier

A boxed array of *HostPlacedVirtualNicIdentifier*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPlacedVirtualNicIdentifier]**](HostPlacedVirtualNicIdentifier.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_placed_virtual_nic_identifier import ArrayOfHostPlacedVirtualNicIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPlacedVirtualNicIdentifier from a JSON string
array_of_host_placed_virtual_nic_identifier_instance = ArrayOfHostPlacedVirtualNicIdentifier.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPlacedVirtualNicIdentifier.to_json()

# convert the object into a dict
array_of_host_placed_virtual_nic_identifier_dict = array_of_host_placed_virtual_nic_identifier_instance.to_dict()
# create an instance of ArrayOfHostPlacedVirtualNicIdentifier from a dict
array_of_host_placed_virtual_nic_identifier_form_dict = array_of_host_placed_virtual_nic_identifier.from_dict(array_of_host_placed_virtual_nic_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


