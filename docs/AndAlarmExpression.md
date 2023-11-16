# AndAlarmExpression

A data object type that links multiple alarm expressions with AND operators. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**List[AlarmExpression]**](AlarmExpression.md) | List of alarm expressions that define the overall status of the alarm. - The state of the alarm expression is gray if all subexpressions are gray.   Otherwise, gray subexpressions are ignored. - The state is red if all subexpressions are red. - Otherwise, the state is yellow if all subexpressions are red or yellow. - Otherwise, the state of the alarm expression is green.  | 

## Example

```python
from vmware_vi.models.and_alarm_expression import AndAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of AndAlarmExpression from a JSON string
and_alarm_expression_instance = AndAlarmExpression.from_json(json)
# print the JSON string representation of the object
print AndAlarmExpression.to_json()

# convert the object into a dict
and_alarm_expression_dict = and_alarm_expression_instance.to_dict()
# create an instance of AndAlarmExpression from a dict
and_alarm_expression_form_dict = and_alarm_expression.from_dict(and_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


