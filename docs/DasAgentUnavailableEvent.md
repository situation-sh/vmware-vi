# DasAgentUnavailableEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that VirtualCenter cannot contact any primary host in this HA cluster.  HA designates some hosts as primary hosts in the HA cluster. When adding a new host to an existing cluster, HA needs to contact one of the primary hosts to finish the configuration. VirtualCenter has lost contact with all primary nodes in the connected state. Attempts to configure HA on a host in this cluster will fail until a DasAgentFoundEvent is logged or unless this is the first node to be configured. For example, if all the other hosts are disconnected first. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_agent_unavailable_event import DasAgentUnavailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasAgentUnavailableEvent from a JSON string
das_agent_unavailable_event_instance = DasAgentUnavailableEvent.from_json(json)
# print the JSON string representation of the object
print DasAgentUnavailableEvent.to_json()

# convert the object into a dict
das_agent_unavailable_event_dict = das_agent_unavailable_event_instance.to_dict()
# create an instance of DasAgentUnavailableEvent from a dict
das_agent_unavailable_event_form_dict = das_agent_unavailable_event.from_dict(das_agent_unavailable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


