# AlarmExpression

Base type for the expressions specifying the conditions that define the status of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.alarm_expression import AlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmExpression from a JSON string
alarm_expression_instance = AlarmExpression.from_json(json)
# print the JSON string representation of the object
print AlarmExpression.to_json()

# convert the object into a dict
alarm_expression_dict = alarm_expression_instance.to_dict()
# create an instance of AlarmExpression from a dict
alarm_expression_form_dict = alarm_expression.from_dict(alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


