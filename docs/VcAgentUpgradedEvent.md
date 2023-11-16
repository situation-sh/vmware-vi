# VcAgentUpgradedEvent

This event records when the VirtualCenter agent on a host upgraded. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vc_agent_upgraded_event import VcAgentUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VcAgentUpgradedEvent from a JSON string
vc_agent_upgraded_event_instance = VcAgentUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print VcAgentUpgradedEvent.to_json()

# convert the object into a dict
vc_agent_upgraded_event_dict = vc_agent_upgraded_event_instance.to_dict()
# create an instance of VcAgentUpgradedEvent from a dict
vc_agent_upgraded_event_form_dict = vc_agent_upgraded_event.from_dict(vc_agent_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


