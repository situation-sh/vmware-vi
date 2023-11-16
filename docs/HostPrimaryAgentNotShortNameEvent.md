# HostPrimaryAgentNotShortNameEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that the primary agent specified is not a short name.  The name of the primary agent is usually stored as a short name. You should not normally see this error. Please check the network configurations of your hosts.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_agent** | **str** |  | 

## Example

```python
from vmware_vi.models.host_primary_agent_not_short_name_event import HostPrimaryAgentNotShortNameEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostPrimaryAgentNotShortNameEvent from a JSON string
host_primary_agent_not_short_name_event_instance = HostPrimaryAgentNotShortNameEvent.from_json(json)
# print the JSON string representation of the object
print HostPrimaryAgentNotShortNameEvent.to_json()

# convert the object into a dict
host_primary_agent_not_short_name_event_dict = host_primary_agent_not_short_name_event_instance.to_dict()
# create an instance of HostPrimaryAgentNotShortNameEvent from a dict
host_primary_agent_not_short_name_event_form_dict = host_primary_agent_not_short_name_event.from_dict(host_primary_agent_not_short_name_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


