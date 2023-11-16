# ArrayOfDasAgentFoundEvent

A boxed array of *DasAgentFoundEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DasAgentFoundEvent]**](DasAgentFoundEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_das_agent_found_event import ArrayOfDasAgentFoundEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDasAgentFoundEvent from a JSON string
array_of_das_agent_found_event_instance = ArrayOfDasAgentFoundEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDasAgentFoundEvent.to_json()

# convert the object into a dict
array_of_das_agent_found_event_dict = array_of_das_agent_found_event_instance.to_dict()
# create an instance of ArrayOfDasAgentFoundEvent from a dict
array_of_das_agent_found_event_form_dict = array_of_das_agent_found_event.from_dict(array_of_das_agent_found_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


