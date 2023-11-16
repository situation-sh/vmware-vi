# UnlicensedVirtualMachinesFoundEvent

This event records that we discovered unlicensed virtual machines on the specified host.  After this event is entered into the event log, we expect to see a corresponding (@link vim.event.Event.UnlicensedVirtualMachinesEvent UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue configIssue) on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** |  | 

## Example

```python
from vmware_vi.models.unlicensed_virtual_machines_found_event import UnlicensedVirtualMachinesFoundEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnlicensedVirtualMachinesFoundEvent from a JSON string
unlicensed_virtual_machines_found_event_instance = UnlicensedVirtualMachinesFoundEvent.from_json(json)
# print the JSON string representation of the object
print UnlicensedVirtualMachinesFoundEvent.to_json()

# convert the object into a dict
unlicensed_virtual_machines_found_event_dict = unlicensed_virtual_machines_found_event_instance.to_dict()
# create an instance of UnlicensedVirtualMachinesFoundEvent from a dict
unlicensed_virtual_machines_found_event_form_dict = unlicensed_virtual_machines_found_event.from_dict(unlicensed_virtual_machines_found_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


