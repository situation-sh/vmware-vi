# ExitedStandbyModeEvent

This event records that the host is no longer in standby mode.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.exited_standby_mode_event import ExitedStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExitedStandbyModeEvent from a JSON string
exited_standby_mode_event_instance = ExitedStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ExitedStandbyModeEvent.to_json()

# convert the object into a dict
exited_standby_mode_event_dict = exited_standby_mode_event_instance.to_dict()
# create an instance of ExitedStandbyModeEvent from a dict
exited_standby_mode_event_form_dict = exited_standby_mode_event.from_dict(exited_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


