# ArrayOfEnteredStandbyModeEvent

A boxed array of *EnteredStandbyModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EnteredStandbyModeEvent]**](EnteredStandbyModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_entered_standby_mode_event import ArrayOfEnteredStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEnteredStandbyModeEvent from a JSON string
array_of_entered_standby_mode_event_instance = ArrayOfEnteredStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfEnteredStandbyModeEvent.to_json()

# convert the object into a dict
array_of_entered_standby_mode_event_dict = array_of_entered_standby_mode_event_instance.to_dict()
# create an instance of ArrayOfEnteredStandbyModeEvent from a dict
array_of_entered_standby_mode_event_form_dict = array_of_entered_standby_mode_event.from_dict(array_of_entered_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


