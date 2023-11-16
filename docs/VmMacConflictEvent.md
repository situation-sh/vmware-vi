# VmMacConflictEvent

This event records a MAC address conflict for a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicted_vm** | [**VmEventArgument**](VmEventArgument.md) |  | 
**mac** | **str** | The MAC address that is in conflict.  | 

## Example

```python
from vmware_vi.models.vm_mac_conflict_event import VmMacConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMacConflictEvent from a JSON string
vm_mac_conflict_event_instance = VmMacConflictEvent.from_json(json)
# print the JSON string representation of the object
print VmMacConflictEvent.to_json()

# convert the object into a dict
vm_mac_conflict_event_dict = vm_mac_conflict_event_instance.to_dict()
# create an instance of VmMacConflictEvent from a dict
vm_mac_conflict_event_form_dict = vm_mac_conflict_event.from_dict(vm_mac_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


