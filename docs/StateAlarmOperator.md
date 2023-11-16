# StateAlarmOperator

A boxed *StateAlarmOperator_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**StateAlarmOperatorEnum**](StateAlarmOperatorEnum.md) |  | 

## Example

```python
from vmware_vi.models.state_alarm_operator import StateAlarmOperator

# TODO update the JSON string below
json = "{}"
# create an instance of StateAlarmOperator from a JSON string
state_alarm_operator_instance = StateAlarmOperator.from_json(json)
# print the JSON string representation of the object
print StateAlarmOperator.to_json()

# convert the object into a dict
state_alarm_operator_dict = state_alarm_operator_instance.to_dict()
# create an instance of StateAlarmOperator from a dict
state_alarm_operator_form_dict = state_alarm_operator.from_dict(state_alarm_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


