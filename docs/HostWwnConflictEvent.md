# HostWwnConflictEvent

This event records a conflict of host WWNs (World Wide Name).  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicted_vms** | [**List[VmEventArgument]**](VmEventArgument.md) | The virtual machine whose WWN conflicts with the current host&#39;s WWN.  ***Since:*** VI API 2.5  | [optional] 
**conflicted_hosts** | [**List[HostEventArgument]**](HostEventArgument.md) | The host whose physical WWN conflicts with the current host&#39;s WWN.  ***Since:*** VI API 2.5  | [optional] 
**wwn** | **int** | The WWN in conflict.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_wwn_conflict_event import HostWwnConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostWwnConflictEvent from a JSON string
host_wwn_conflict_event_instance = HostWwnConflictEvent.from_json(json)
# print the JSON string representation of the object
print HostWwnConflictEvent.to_json()

# convert the object into a dict
host_wwn_conflict_event_dict = host_wwn_conflict_event_instance.to_dict()
# create an instance of HostWwnConflictEvent from a dict
host_wwn_conflict_event_form_dict = host_wwn_conflict_event.from_dict(host_wwn_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


