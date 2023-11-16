# VcAgentUpgradeFailedEvent

This event records when the VirtualCenter agent on a host failed to upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the upgrade failed, if known.  See *AgentInstallFailedReason_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vc_agent_upgrade_failed_event import VcAgentUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VcAgentUpgradeFailedEvent from a JSON string
vc_agent_upgrade_failed_event_instance = VcAgentUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print VcAgentUpgradeFailedEvent.to_json()

# convert the object into a dict
vc_agent_upgrade_failed_event_dict = vc_agent_upgrade_failed_event_instance.to_dict()
# create an instance of VcAgentUpgradeFailedEvent from a dict
vc_agent_upgrade_failed_event_form_dict = vc_agent_upgrade_failed_event.from_dict(vc_agent_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


