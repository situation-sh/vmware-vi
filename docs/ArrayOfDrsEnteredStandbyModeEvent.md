# ArrayOfDrsEnteredStandbyModeEvent

A boxed array of *DrsEnteredStandbyModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsEnteredStandbyModeEvent]**](DrsEnteredStandbyModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_entered_standby_mode_event import ArrayOfDrsEnteredStandbyModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsEnteredStandbyModeEvent from a JSON string
array_of_drs_entered_standby_mode_event_instance = ArrayOfDrsEnteredStandbyModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsEnteredStandbyModeEvent.to_json()

# convert the object into a dict
array_of_drs_entered_standby_mode_event_dict = array_of_drs_entered_standby_mode_event_instance.to_dict()
# create an instance of ArrayOfDrsEnteredStandbyModeEvent from a dict
array_of_drs_entered_standby_mode_event_form_dict = array_of_drs_entered_standby_mode_event.from_dict(array_of_drs_entered_standby_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


