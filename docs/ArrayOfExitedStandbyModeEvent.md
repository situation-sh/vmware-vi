# ArrayOfExitedStandbyModeEvent

A boxed array of *ExitedStandbyModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExitedStandbyModeEvent]**](ExitedStandbyModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_exited_standby_mode_event import ArrayOfExitedStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExitedStandbyModeEvent from a JSON string
array_of_exited_standby_mode_event_instance = ArrayOfExitedStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfExitedStandbyModeEvent.to_json()

# convert the object into a dict
array_of_exited_standby_mode_event_dict = array_of_exited_standby_mode_event_instance.to_dict()
# create an instance of ArrayOfExitedStandbyModeEvent from a dict
array_of_exited_standby_mode_event_form_dict = array_of_exited_standby_mode_event.from_dict(array_of_exited_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


