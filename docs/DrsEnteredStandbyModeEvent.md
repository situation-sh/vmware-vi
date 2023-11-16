# DrsEnteredStandbyModeEvent

This event records that the host has successfully entered standby mode initiated by Distributed Power Management.  A host in this mode has no running virtual machines and no provisioning operations are occurring.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_entered_standby_mode_event import DrsEnteredStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsEnteredStandbyModeEvent from a JSON string
drs_entered_standby_mode_event_instance = DrsEnteredStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print DrsEnteredStandbyModeEvent.to_json()

# convert the object into a dict
drs_entered_standby_mode_event_dict = drs_entered_standby_mode_event_instance.to_dict()
# create an instance of DrsEnteredStandbyModeEvent from a dict
drs_entered_standby_mode_event_form_dict = drs_entered_standby_mode_event.from_dict(drs_entered_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


