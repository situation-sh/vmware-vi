# DrsExitedStandbyModeEvent

This event records that Distributed Power Management brings this host out from standby mode.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_exited_standby_mode_event import DrsExitedStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsExitedStandbyModeEvent from a JSON string
drs_exited_standby_mode_event_instance = DrsExitedStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print DrsExitedStandbyModeEvent.to_json()

# convert the object into a dict
drs_exited_standby_mode_event_dict = drs_exited_standby_mode_event_instance.to_dict()
# create an instance of DrsExitedStandbyModeEvent from a dict
drs_exited_standby_mode_event_form_dict = drs_exited_standby_mode_event.from_dict(drs_exited_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


