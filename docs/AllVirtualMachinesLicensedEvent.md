# AllVirtualMachinesLicensedEvent

This event records that the previously unlicensed virtual machines on the specified host are now licensed.  After this event is entered into the event log, we expect to see that the (@link vim.event.Event.UnlicensedVirtualMachinesEvent UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue configIssue) is removed from the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.all_virtual_machines_licensed_event import AllVirtualMachinesLicensedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AllVirtualMachinesLicensedEvent from a JSON string
all_virtual_machines_licensed_event_instance = AllVirtualMachinesLicensedEvent.from_json(json)
# print the JSON string representation of the object
print AllVirtualMachinesLicensedEvent.to_json()

# convert the object into a dict
all_virtual_machines_licensed_event_dict = all_virtual_machines_licensed_event_instance.to_dict()
# create an instance of AllVirtualMachinesLicensedEvent from a dict
all_virtual_machines_licensed_event_form_dict = all_virtual_machines_licensed_event.from_dict(all_virtual_machines_licensed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


