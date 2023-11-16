# AlarmTriggeringActionTransitionSpec

Specification indicating which on transitions this action fires.  The existence of a Spec indicates that this action fires on transitions from that Spec's startState to finalState.  There are six acceptable {startState, finalState} pairs: {green, yellow}, {green, red}, {yellow, red}, {red, yellow}, {red, green} and {yellow, green}. Direct transitions have precedence over indirect. At least one of these pairs must be specified. Any deviation from the above will render the enclosing AlarmSpec invalid.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_state** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**final_state** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**repeats** | **bool** | Whether or not the action repeats, as per the actionFrequency defined in the enclosing Alarm.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.alarm_triggering_action_transition_spec import AlarmTriggeringActionTransitionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmTriggeringActionTransitionSpec from a JSON string
alarm_triggering_action_transition_spec_instance = AlarmTriggeringActionTransitionSpec.from_json(json)
# print the JSON string representation of the object
print AlarmTriggeringActionTransitionSpec.to_json()

# convert the object into a dict
alarm_triggering_action_transition_spec_dict = alarm_triggering_action_transition_spec_instance.to_dict()
# create an instance of AlarmTriggeringActionTransitionSpec from a dict
alarm_triggering_action_transition_spec_form_dict = alarm_triggering_action_transition_spec.from_dict(alarm_triggering_action_transition_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


