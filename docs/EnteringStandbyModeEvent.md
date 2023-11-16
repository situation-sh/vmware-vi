# EnteringStandbyModeEvent

This event records that a host has begun the process of entering standby mode.  All virtual machine operations are blocked, except the following: - MigrateVM - PowerOffVM - SuspendVM - ShutdownGuest - StandbyGuest    ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.entering_standby_mode_event import EnteringStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EnteringStandbyModeEvent from a JSON string
entering_standby_mode_event_instance = EnteringStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print EnteringStandbyModeEvent.to_json()

# convert the object into a dict
entering_standby_mode_event_dict = entering_standby_mode_event_instance.to_dict()
# create an instance of EnteringStandbyModeEvent from a dict
entering_standby_mode_event_form_dict = entering_standby_mode_event.from_dict(entering_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


