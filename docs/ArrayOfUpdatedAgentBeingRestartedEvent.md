# ArrayOfUpdatedAgentBeingRestartedEvent

A boxed array of *UpdatedAgentBeingRestartedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UpdatedAgentBeingRestartedEvent]**](UpdatedAgentBeingRestartedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_updated_agent_being_restarted_event import ArrayOfUpdatedAgentBeingRestartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUpdatedAgentBeingRestartedEvent from a JSON string
array_of_updated_agent_being_restarted_event_instance = ArrayOfUpdatedAgentBeingRestartedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUpdatedAgentBeingRestartedEvent.to_json()

# convert the object into a dict
array_of_updated_agent_being_restarted_event_dict = array_of_updated_agent_being_restarted_event_instance.to_dict()
# create an instance of ArrayOfUpdatedAgentBeingRestartedEvent from a dict
array_of_updated_agent_being_restarted_event_form_dict = array_of_updated_agent_being_restarted_event.from_dict(array_of_updated_agent_being_restarted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


