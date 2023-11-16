# ExitStandbyModeFailedEvent

This event records that the host failed to exit standby mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.exit_standby_mode_failed_event import ExitStandbyModeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExitStandbyModeFailedEvent from a JSON string
exit_standby_mode_failed_event_instance = ExitStandbyModeFailedEvent.from_json(json)
# print the JSON string representation of the object
print ExitStandbyModeFailedEvent.to_json()

# convert the object into a dict
exit_standby_mode_failed_event_dict = exit_standby_mode_failed_event_instance.to_dict()
# create an instance of ExitStandbyModeFailedEvent from a dict
exit_standby_mode_failed_event_form_dict = exit_standby_mode_failed_event.from_dict(exit_standby_mode_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


