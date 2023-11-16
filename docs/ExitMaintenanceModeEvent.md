# ExitMaintenanceModeEvent

This event records that the host is no longer in maintenance mode. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.exit_maintenance_mode_event import ExitMaintenanceModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExitMaintenanceModeEvent from a JSON string
exit_maintenance_mode_event_instance = ExitMaintenanceModeEvent.from_json(json)
# print the JSON string representation of the object
print ExitMaintenanceModeEvent.to_json()

# convert the object into a dict
exit_maintenance_mode_event_dict = exit_maintenance_mode_event_instance.to_dict()
# create an instance of ExitMaintenanceModeEvent from a dict
exit_maintenance_mode_event_form_dict = exit_maintenance_mode_event.from_dict(exit_maintenance_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


