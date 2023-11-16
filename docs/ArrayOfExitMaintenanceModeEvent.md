# ArrayOfExitMaintenanceModeEvent

A boxed array of *ExitMaintenanceModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExitMaintenanceModeEvent]**](ExitMaintenanceModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_exit_maintenance_mode_event import ArrayOfExitMaintenanceModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExitMaintenanceModeEvent from a JSON string
array_of_exit_maintenance_mode_event_instance = ArrayOfExitMaintenanceModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfExitMaintenanceModeEvent.to_json()

# convert the object into a dict
array_of_exit_maintenance_mode_event_dict = array_of_exit_maintenance_mode_event_instance.to_dict()
# create an instance of ArrayOfExitMaintenanceModeEvent from a dict
array_of_exit_maintenance_mode_event_form_dict = array_of_exit_maintenance_mode_event.from_dict(array_of_exit_maintenance_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


