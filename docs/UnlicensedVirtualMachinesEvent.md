# UnlicensedVirtualMachinesEvent

This event records that we have unlicensed virtual machines on the specified host.  This can be both a (@link vim.ManagedEntity.configIssue configIssue) and an entry in the event log.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlicensed** | **int** |  | 
**available** | **int** |  | 

## Example

```python
from vmware_vi.models.unlicensed_virtual_machines_event import UnlicensedVirtualMachinesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnlicensedVirtualMachinesEvent from a JSON string
unlicensed_virtual_machines_event_instance = UnlicensedVirtualMachinesEvent.from_json(json)
# print the JSON string representation of the object
print UnlicensedVirtualMachinesEvent.to_json()

# convert the object into a dict
unlicensed_virtual_machines_event_dict = unlicensed_virtual_machines_event_instance.to_dict()
# create an instance of UnlicensedVirtualMachinesEvent from a dict
unlicensed_virtual_machines_event_form_dict = unlicensed_virtual_machines_event.from_dict(unlicensed_virtual_machines_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


