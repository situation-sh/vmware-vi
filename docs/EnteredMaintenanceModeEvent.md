# EnteredMaintenanceModeEvent

This event records that the host has completely entered maintenance mode.  A host in this mode has no running virtual machines and no provisioning operations are occurring. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.entered_maintenance_mode_event import EnteredMaintenanceModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EnteredMaintenanceModeEvent from a JSON string
entered_maintenance_mode_event_instance = EnteredMaintenanceModeEvent.from_json(json)
# print the JSON string representation of the object
print EnteredMaintenanceModeEvent.to_json()

# convert the object into a dict
entered_maintenance_mode_event_dict = entered_maintenance_mode_event_instance.to_dict()
# create an instance of EnteredMaintenanceModeEvent from a dict
entered_maintenance_mode_event_form_dict = entered_maintenance_mode_event.from_dict(entered_maintenance_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


