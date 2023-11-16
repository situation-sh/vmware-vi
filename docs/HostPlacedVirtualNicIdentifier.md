# HostPlacedVirtualNicIdentifier

This data type describes the Virtual Machine and Virtual NIC to identify virtual adapters placed on a physical NIC  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vnic_key** | **str** | The virtual NIC key  ***Since:*** vSphere API 6.0  | 
**reservation** | **int** | The virtual NIC reservation  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_placed_virtual_nic_identifier import HostPlacedVirtualNicIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of HostPlacedVirtualNicIdentifier from a JSON string
host_placed_virtual_nic_identifier_instance = HostPlacedVirtualNicIdentifier.from_json(json)
# print the JSON string representation of the object
print HostPlacedVirtualNicIdentifier.to_json()

# convert the object into a dict
host_placed_virtual_nic_identifier_dict = host_placed_virtual_nic_identifier_instance.to_dict()
# create an instance of HostPlacedVirtualNicIdentifier from a dict
host_placed_virtual_nic_identifier_form_dict = host_placed_virtual_nic_identifier.from_dict(host_placed_virtual_nic_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


