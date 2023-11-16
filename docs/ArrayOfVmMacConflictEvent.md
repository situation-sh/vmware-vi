# ArrayOfVmMacConflictEvent

A boxed array of *VmMacConflictEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMacConflictEvent]**](VmMacConflictEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_mac_conflict_event import ArrayOfVmMacConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMacConflictEvent from a JSON string
array_of_vm_mac_conflict_event_instance = ArrayOfVmMacConflictEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMacConflictEvent.to_json()

# convert the object into a dict
array_of_vm_mac_conflict_event_dict = array_of_vm_mac_conflict_event_instance.to_dict()
# create an instance of ArrayOfVmMacConflictEvent from a dict
array_of_vm_mac_conflict_event_form_dict = array_of_vm_mac_conflict_event.from_dict(array_of_vm_mac_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


