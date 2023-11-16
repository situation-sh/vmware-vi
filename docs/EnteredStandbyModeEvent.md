# EnteredStandbyModeEvent

This event records that the host has successfully entered standby mode.  A host in this mode has no running virtual machines and no provisioning operations are occurring.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.entered_standby_mode_event import EnteredStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EnteredStandbyModeEvent from a JSON string
entered_standby_mode_event_instance = EnteredStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print EnteredStandbyModeEvent.to_json()

# convert the object into a dict
entered_standby_mode_event_dict = entered_standby_mode_event_instance.to_dict()
# create an instance of EnteredStandbyModeEvent from a dict
entered_standby_mode_event_form_dict = entered_standby_mode_event.from_dict(entered_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


