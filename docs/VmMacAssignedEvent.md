# VmMacAssignedEvent

This event records the assignment of a new MAC address to a virtual network adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter** | **str** | The name of the virtual adapter.  | 
**mac** | **str** | The new MAC address.  | 

## Example

```python
from vmware_vi.models.vm_mac_assigned_event import VmMacAssignedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMacAssignedEvent from a JSON string
vm_mac_assigned_event_instance = VmMacAssignedEvent.from_json(json)
# print the JSON string representation of the object
print VmMacAssignedEvent.to_json()

# convert the object into a dict
vm_mac_assigned_event_dict = vm_mac_assigned_event_instance.to_dict()
# create an instance of VmMacAssignedEvent from a dict
vm_mac_assigned_event_form_dict = vm_mac_assigned_event.from_dict(vm_mac_assigned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


