# ArrayOfVmAcquiredMksTicketEvent

A boxed array of *VmAcquiredMksTicketEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmAcquiredMksTicketEvent]**](VmAcquiredMksTicketEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_acquired_mks_ticket_event import ArrayOfVmAcquiredMksTicketEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmAcquiredMksTicketEvent from a JSON string
array_of_vm_acquired_mks_ticket_event_instance = ArrayOfVmAcquiredMksTicketEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmAcquiredMksTicketEvent.to_json()

# convert the object into a dict
array_of_vm_acquired_mks_ticket_event_dict = array_of_vm_acquired_mks_ticket_event_instance.to_dict()
# create an instance of ArrayOfVmAcquiredMksTicketEvent from a dict
array_of_vm_acquired_mks_ticket_event_form_dict = array_of_vm_acquired_mks_ticket_event.from_dict(array_of_vm_acquired_mks_ticket_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


