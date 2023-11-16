# ArrayOfAlarmTriggeringAction

A boxed array of *AlarmTriggeringAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmTriggeringAction]**](AlarmTriggeringAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_triggering_action import ArrayOfAlarmTriggeringAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmTriggeringAction from a JSON string
array_of_alarm_triggering_action_instance = ArrayOfAlarmTriggeringAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmTriggeringAction.to_json()

# convert the object into a dict
array_of_alarm_triggering_action_dict = array_of_alarm_triggering_action_instance.to_dict()
# create an instance of ArrayOfAlarmTriggeringAction from a dict
array_of_alarm_triggering_action_form_dict = array_of_alarm_triggering_action.from_dict(array_of_alarm_triggering_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


