# ArrayOfTeamingMatchEvent

A boxed array of *TeamingMatchEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TeamingMatchEvent]**](TeamingMatchEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_teaming_match_event import ArrayOfTeamingMatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTeamingMatchEvent from a JSON string
array_of_teaming_match_event_instance = ArrayOfTeamingMatchEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTeamingMatchEvent.to_json()

# convert the object into a dict
array_of_teaming_match_event_dict = array_of_teaming_match_event_instance.to_dict()
# create an instance of ArrayOfTeamingMatchEvent from a dict
array_of_teaming_match_event_form_dict = array_of_teaming_match_event.from_dict(array_of_teaming_match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


