# DasAgentFoundEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that VirtualCenter has re-established contact with a primary host in this HA cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_agent_found_event import DasAgentFoundEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasAgentFoundEvent from a JSON string
das_agent_found_event_instance = DasAgentFoundEvent.from_json(json)
# print the JSON string representation of the object
print DasAgentFoundEvent.to_json()

# convert the object into a dict
das_agent_found_event_dict = das_agent_found_event_instance.to_dict()
# create an instance of DasAgentFoundEvent from a dict
das_agent_found_event_form_dict = das_agent_found_event.from_dict(das_agent_found_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


