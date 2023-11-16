# TeamingMisMatchEvent

The teaming configuration of the uplink ports in the DVS does not match physical switch configuration.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.teaming_mis_match_event import TeamingMisMatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TeamingMisMatchEvent from a JSON string
teaming_mis_match_event_instance = TeamingMisMatchEvent.from_json(json)
# print the JSON string representation of the object
print TeamingMisMatchEvent.to_json()

# convert the object into a dict
teaming_mis_match_event_dict = teaming_mis_match_event_instance.to_dict()
# create an instance of TeamingMisMatchEvent from a dict
teaming_mis_match_event_form_dict = teaming_mis_match_event.from_dict(teaming_mis_match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


