# OrAlarmExpression

A data object type that links multiple alarm expressions with OR operators. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**List[AlarmExpression]**](AlarmExpression.md) | List of alarm expressions that define the overall status of the alarm. - The state of the alarm expression is gray if all subexpressions are gray.   Otherwise, gray subexpressions are ignored. - The state is red if any subexpression is red. - Otherwise, the state is yellow if any subexpression is yellow. - Otherwise, the state of the alarm expression is green.  | 

## Example

```python
from vmware_vi.models.or_alarm_expression import OrAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of OrAlarmExpression from a JSON string
or_alarm_expression_instance = OrAlarmExpression.from_json(json)
# print the JSON string representation of the object
print OrAlarmExpression.to_json()

# convert the object into a dict
or_alarm_expression_dict = or_alarm_expression_instance.to_dict()
# create an instance of OrAlarmExpression from a dict
or_alarm_expression_form_dict = or_alarm_expression.from_dict(or_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


