# UpdatedAgentBeingRestartedEvent

This event records that the agent has been patched and will be restarted.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.updated_agent_being_restarted_event import UpdatedAgentBeingRestartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedAgentBeingRestartedEvent from a JSON string
updated_agent_being_restarted_event_instance = UpdatedAgentBeingRestartedEvent.from_json(json)
# print the JSON string representation of the object
print UpdatedAgentBeingRestartedEvent.to_json()

# convert the object into a dict
updated_agent_being_restarted_event_dict = updated_agent_being_restarted_event_instance.to_dict()
# create an instance of UpdatedAgentBeingRestartedEvent from a dict
updated_agent_being_restarted_event_form_dict = updated_agent_being_restarted_event.from_dict(updated_agent_being_restarted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


