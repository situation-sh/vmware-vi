# ArrayOfAlarmTriggeringActionTransitionSpec

A boxed array of *AlarmTriggeringActionTransitionSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmTriggeringActionTransitionSpec]**](AlarmTriggeringActionTransitionSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_triggering_action_transition_spec import ArrayOfAlarmTriggeringActionTransitionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmTriggeringActionTransitionSpec from a JSON string
array_of_alarm_triggering_action_transition_spec_instance = ArrayOfAlarmTriggeringActionTransitionSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmTriggeringActionTransitionSpec.to_json()

# convert the object into a dict
array_of_alarm_triggering_action_transition_spec_dict = array_of_alarm_triggering_action_transition_spec_instance.to_dict()
# create an instance of ArrayOfAlarmTriggeringActionTransitionSpec from a dict
array_of_alarm_triggering_action_transition_spec_form_dict = array_of_alarm_triggering_action_transition_spec.from_dict(array_of_alarm_triggering_action_transition_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


