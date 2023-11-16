# EnteringMaintenanceModeEvent

This event records that a host has begun the process of entering maintenance mode.  All virtual machine operations are blocked, except the following: - MigrateVM - PowerOffVM - SuspendVM - ShutdownGuest - StandbyGuest 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.entering_maintenance_mode_event import EnteringMaintenanceModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EnteringMaintenanceModeEvent from a JSON string
entering_maintenance_mode_event_instance = EnteringMaintenanceModeEvent.from_json(json)
# print the JSON string representation of the object
print EnteringMaintenanceModeEvent.to_json()

# convert the object into a dict
entering_maintenance_mode_event_dict = entering_maintenance_mode_event_instance.to_dict()
# create an instance of EnteringMaintenanceModeEvent from a dict
entering_maintenance_mode_event_form_dict = entering_maintenance_mode_event.from_dict(entering_maintenance_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


