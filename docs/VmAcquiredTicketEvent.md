# VmAcquiredTicketEvent

This event records a user successfully acquiring a ticket  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_type** | **str** | The type of the ticket @see VirtualMachine.TicketType  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.vm_acquired_ticket_event import VmAcquiredTicketEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmAcquiredTicketEvent from a JSON string
vm_acquired_ticket_event_instance = VmAcquiredTicketEvent.from_json(json)
# print the JSON string representation of the object
print VmAcquiredTicketEvent.to_json()

# convert the object into a dict
vm_acquired_ticket_event_dict = vm_acquired_ticket_event_instance.to_dict()
# create an instance of VmAcquiredTicketEvent from a dict
vm_acquired_ticket_event_form_dict = vm_acquired_ticket_event.from_dict(vm_acquired_ticket_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


