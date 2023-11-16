# AlarmTriggeringAction

This data object type describes one or more triggering transitions and an action to be done when an alarm is triggered.  There are four triggering transitions; at least one of them must be provided. A gray state is considered the same as a green state, for the purpose of detecting transitions. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**transition_specs** | [**List[AlarmTriggeringActionTransitionSpec]**](AlarmTriggeringActionTransitionSpec.md) | Indicates on which transitions this action executes and repeats.  This is optional only for backwards compatibility.  ***Since:*** vSphere API 4.0  | [optional] 
**green2yellow** | **bool** | Deprecated as of vSphere API 4.0, use *AlarmTriggeringActionTransitionSpec* .  Flag to specify that the alarm should trigger on a transition from green to yellow.  | 
**yellow2red** | **bool** | Deprecated as of vSphere API 4.0, use *AlarmTriggeringActionTransitionSpec* .  Flag to specify that the alarm should trigger on a transition from yellow to red.  | 
**red2yellow** | **bool** | Deprecated as of vSphere API 4.0, use *AlarmTriggeringActionTransitionSpec* .  Flag to specify that the alarm should trigger on a transition from red to yellow.  | 
**yellow2green** | **bool** | Deprecated as of vSphere API 4.0, use *AlarmTriggeringActionTransitionSpec* .  Flag to specify that the alarm should trigger on a transition from yellow to green.  | 

## Example

```python
from vmware_vi.models.alarm_triggering_action import AlarmTriggeringAction

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmTriggeringAction from a JSON string
alarm_triggering_action_instance = AlarmTriggeringAction.from_json(json)
# print the JSON string representation of the object
print AlarmTriggeringAction.to_json()

# convert the object into a dict
alarm_triggering_action_dict = alarm_triggering_action_instance.to_dict()
# create an instance of AlarmTriggeringAction from a dict
alarm_triggering_action_form_dict = alarm_triggering_action.from_dict(alarm_triggering_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


