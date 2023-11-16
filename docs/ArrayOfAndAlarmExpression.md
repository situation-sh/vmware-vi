# ArrayOfAndAlarmExpression

A boxed array of *AndAlarmExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AndAlarmExpression]**](AndAlarmExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_and_alarm_expression import ArrayOfAndAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAndAlarmExpression from a JSON string
array_of_and_alarm_expression_instance = ArrayOfAndAlarmExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfAndAlarmExpression.to_json()

# convert the object into a dict
array_of_and_alarm_expression_dict = array_of_and_alarm_expression_instance.to_dict()
# create an instance of ArrayOfAndAlarmExpression from a dict
array_of_and_alarm_expression_form_dict = array_of_and_alarm_expression.from_dict(array_of_and_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


