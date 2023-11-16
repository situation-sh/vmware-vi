# VcAgentUninstallFailedEvent

This event records when the VirtualCenter agent on a host failed to uninstall.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the uninstall failed, if known.  See *AgentInstallFailedReason_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vc_agent_uninstall_failed_event import VcAgentUninstallFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VcAgentUninstallFailedEvent from a JSON string
vc_agent_uninstall_failed_event_instance = VcAgentUninstallFailedEvent.from_json(json)
# print the JSON string representation of the object
print VcAgentUninstallFailedEvent.to_json()

# convert the object into a dict
vc_agent_uninstall_failed_event_dict = vc_agent_uninstall_failed_event_instance.to_dict()
# create an instance of VcAgentUninstallFailedEvent from a dict
vc_agent_uninstall_failed_event_form_dict = vc_agent_uninstall_failed_event.from_dict(vc_agent_uninstall_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


