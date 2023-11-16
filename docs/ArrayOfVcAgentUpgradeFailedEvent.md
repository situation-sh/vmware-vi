# ArrayOfVcAgentUpgradeFailedEvent

A boxed array of *VcAgentUpgradeFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VcAgentUpgradeFailedEvent]**](VcAgentUpgradeFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vc_agent_upgrade_failed_event import ArrayOfVcAgentUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVcAgentUpgradeFailedEvent from a JSON string
array_of_vc_agent_upgrade_failed_event_instance = ArrayOfVcAgentUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVcAgentUpgradeFailedEvent.to_json()

# convert the object into a dict
array_of_vc_agent_upgrade_failed_event_dict = array_of_vc_agent_upgrade_failed_event_instance.to_dict()
# create an instance of ArrayOfVcAgentUpgradeFailedEvent from a dict
array_of_vc_agent_upgrade_failed_event_form_dict = array_of_vc_agent_upgrade_failed_event.from_dict(array_of_vc_agent_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


