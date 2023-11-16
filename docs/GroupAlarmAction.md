# GroupAlarmAction

This data object type describes a group of actions that occur when the alarm is triggered.  These actions are not necessarily executed in order. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**List[AlarmAction]**](AlarmAction.md) | The list of alarm actions that occur when the alarm is triggered.  | 

## Example

```python
from vmware_vi.models.group_alarm_action import GroupAlarmAction

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAlarmAction from a JSON string
group_alarm_action_instance = GroupAlarmAction.from_json(json)
# print the JSON string representation of the object
print GroupAlarmAction.to_json()

# convert the object into a dict
group_alarm_action_dict = group_alarm_action_instance.to_dict()
# create an instance of GroupAlarmAction from a dict
group_alarm_action_form_dict = group_alarm_action.from_dict(group_alarm_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


