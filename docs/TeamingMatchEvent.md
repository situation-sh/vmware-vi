# TeamingMatchEvent

The teaming configuration of the uplink ports in the DVS matches physical switch configuration.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.teaming_match_event import TeamingMatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TeamingMatchEvent from a JSON string
teaming_match_event_instance = TeamingMatchEvent.from_json(json)
# print the JSON string representation of the object
print TeamingMatchEvent.to_json()

# convert the object into a dict
teaming_match_event_dict = teaming_match_event_instance.to_dict()
# create an instance of TeamingMatchEvent from a dict
teaming_match_event_form_dict = teaming_match_event.from_dict(teaming_match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


