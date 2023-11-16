# DrsExitStandbyModeFailedEvent

This event records that Distributed Power Management tried to bring a host out from standby mode, but the host failed to exit standby mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_exit_standby_mode_failed_event import DrsExitStandbyModeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsExitStandbyModeFailedEvent from a JSON string
drs_exit_standby_mode_failed_event_instance = DrsExitStandbyModeFailedEvent.from_json(json)
# print the JSON string representation of the object
print DrsExitStandbyModeFailedEvent.to_json()

# convert the object into a dict
drs_exit_standby_mode_failed_event_dict = drs_exit_standby_mode_failed_event_instance.to_dict()
# create an instance of DrsExitStandbyModeFailedEvent from a dict
drs_exit_standby_mode_failed_event_form_dict = drs_exit_standby_mode_failed_event.from_dict(drs_exit_standby_mode_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


