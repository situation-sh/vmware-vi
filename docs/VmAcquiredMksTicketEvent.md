# VmAcquiredMksTicketEvent

This event records a user successfully acquiring an MKS ticket  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_acquired_mks_ticket_event import VmAcquiredMksTicketEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmAcquiredMksTicketEvent from a JSON string
vm_acquired_mks_ticket_event_instance = VmAcquiredMksTicketEvent.from_json(json)
# print the JSON string representation of the object
print VmAcquiredMksTicketEvent.to_json()

# convert the object into a dict
vm_acquired_mks_ticket_event_dict = vm_acquired_mks_ticket_event_instance.to_dict()
# create an instance of VmAcquiredMksTicketEvent from a dict
vm_acquired_mks_ticket_event_form_dict = vm_acquired_mks_ticket_event.from_dict(vm_acquired_mks_ticket_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


