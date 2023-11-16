# VcAgentUninstalledEvent

This event records when the VirtualCenter agent on a host is uninstalled.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vc_agent_uninstalled_event import VcAgentUninstalledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VcAgentUninstalledEvent from a JSON string
vc_agent_uninstalled_event_instance = VcAgentUninstalledEvent.from_json(json)
# print the JSON string representation of the object
print VcAgentUninstalledEvent.to_json()

# convert the object into a dict
vc_agent_uninstalled_event_dict = vc_agent_uninstalled_event_instance.to_dict()
# create an instance of VcAgentUninstalledEvent from a dict
vc_agent_uninstalled_event_form_dict = vc_agent_uninstalled_event.from_dict(vc_agent_uninstalled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


