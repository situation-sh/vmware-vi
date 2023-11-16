# ArrayOfStateAlarmExpression

A boxed array of *StateAlarmExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StateAlarmExpression]**](StateAlarmExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_state_alarm_expression import ArrayOfStateAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStateAlarmExpression from a JSON string
array_of_state_alarm_expression_instance = ArrayOfStateAlarmExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfStateAlarmExpression.to_json()

# convert the object into a dict
array_of_state_alarm_expression_dict = array_of_state_alarm_expression_instance.to_dict()
# create an instance of ArrayOfStateAlarmExpression from a dict
array_of_state_alarm_expression_form_dict = array_of_state_alarm_expression.from_dict(array_of_state_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


