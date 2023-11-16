# ArrayOfExitingStandbyModeEvent

A boxed array of *ExitingStandbyModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExitingStandbyModeEvent]**](ExitingStandbyModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_exiting_standby_mode_event import ArrayOfExitingStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExitingStandbyModeEvent from a JSON string
array_of_exiting_standby_mode_event_instance = ArrayOfExitingStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfExitingStandbyModeEvent.to_json()

# convert the object into a dict
array_of_exiting_standby_mode_event_dict = array_of_exiting_standby_mode_event_instance.to_dict()
# create an instance of ArrayOfExitingStandbyModeEvent from a dict
array_of_exiting_standby_mode_event_form_dict = array_of_exiting_standby_mode_event.from_dict(array_of_exiting_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


