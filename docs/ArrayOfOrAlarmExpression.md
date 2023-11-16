# ArrayOfOrAlarmExpression

A boxed array of *OrAlarmExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OrAlarmExpression]**](OrAlarmExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_or_alarm_expression import ArrayOfOrAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOrAlarmExpression from a JSON string
array_of_or_alarm_expression_instance = ArrayOfOrAlarmExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfOrAlarmExpression.to_json()

# convert the object into a dict
array_of_or_alarm_expression_dict = array_of_or_alarm_expression_instance.to_dict()
# create an instance of ArrayOfOrAlarmExpression from a dict
array_of_or_alarm_expression_form_dict = array_of_or_alarm_expression.from_dict(array_of_or_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


