# ArrayOfGroupAlarmAction

A boxed array of *GroupAlarmAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GroupAlarmAction]**](GroupAlarmAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_group_alarm_action import ArrayOfGroupAlarmAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGroupAlarmAction from a JSON string
array_of_group_alarm_action_instance = ArrayOfGroupAlarmAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfGroupAlarmAction.to_json()

# convert the object into a dict
array_of_group_alarm_action_dict = array_of_group_alarm_action_instance.to_dict()
# create an instance of ArrayOfGroupAlarmAction from a dict
array_of_group_alarm_action_form_dict = array_of_group_alarm_action.from_dict(array_of_group_alarm_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


