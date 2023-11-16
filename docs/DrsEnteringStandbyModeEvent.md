# DrsEnteringStandbyModeEvent

This event records that a host has begun the process of entering standby mode initiated by Distributed Power Management.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_entering_standby_mode_event import DrsEnteringStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsEnteringStandbyModeEvent from a JSON string
drs_entering_standby_mode_event_instance = DrsEnteringStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print DrsEnteringStandbyModeEvent.to_json()

# convert the object into a dict
drs_entering_standby_mode_event_dict = drs_entering_standby_mode_event_instance.to_dict()
# create an instance of DrsEnteringStandbyModeEvent from a dict
drs_entering_standby_mode_event_form_dict = drs_entering_standby_mode_event.from_dict(drs_entering_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


