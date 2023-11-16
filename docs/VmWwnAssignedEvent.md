# VmWwnAssignedEvent

This event records the assignment of a new WWN (World Wide Name) to a virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_wwns** | **List[int]** | The new node WWN.  ***Since:*** VI API 2.5  | 
**port_wwns** | **List[int]** | The new port WWN.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.vm_wwn_assigned_event import VmWwnAssignedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmWwnAssignedEvent from a JSON string
vm_wwn_assigned_event_instance = VmWwnAssignedEvent.from_json(json)
# print the JSON string representation of the object
print VmWwnAssignedEvent.to_json()

# convert the object into a dict
vm_wwn_assigned_event_dict = vm_wwn_assigned_event_instance.to_dict()
# create an instance of VmWwnAssignedEvent from a dict
vm_wwn_assigned_event_form_dict = vm_wwn_assigned_event.from_dict(vm_wwn_assigned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


