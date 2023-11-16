# ArrayOfExitStandbyModeFailedEvent

A boxed array of *ExitStandbyModeFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExitStandbyModeFailedEvent]**](ExitStandbyModeFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_exit_standby_mode_failed_event import ArrayOfExitStandbyModeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExitStandbyModeFailedEvent from a JSON string
array_of_exit_standby_mode_failed_event_instance = ArrayOfExitStandbyModeFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfExitStandbyModeFailedEvent.to_json()

# convert the object into a dict
array_of_exit_standby_mode_failed_event_dict = array_of_exit_standby_mode_failed_event_instance.to_dict()
# create an instance of ArrayOfExitStandbyModeFailedEvent from a dict
array_of_exit_standby_mode_failed_event_form_dict = array_of_exit_standby_mode_failed_event.from_dict(array_of_exit_standby_mode_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


