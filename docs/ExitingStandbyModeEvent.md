# ExitingStandbyModeEvent

This event records that a host has begun the process of exiting standby mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.exiting_standby_mode_event import ExitingStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExitingStandbyModeEvent from a JSON string
exiting_standby_mode_event_instance = ExitingStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ExitingStandbyModeEvent.to_json()

# convert the object into a dict
exiting_standby_mode_event_dict = exiting_standby_mode_event_instance.to_dict()
# create an instance of ExitingStandbyModeEvent from a dict
exiting_standby_mode_event_form_dict = exiting_standby_mode_event.from_dict(exiting_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


