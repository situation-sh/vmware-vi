# ArrayOfEventAlarmExpression

A boxed array of *EventAlarmExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventAlarmExpression]**](EventAlarmExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_alarm_expression import ArrayOfEventAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventAlarmExpression from a JSON string
array_of_event_alarm_expression_instance = ArrayOfEventAlarmExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventAlarmExpression.to_json()

# convert the object into a dict
array_of_event_alarm_expression_dict = array_of_event_alarm_expression_instance.to_dict()
# create an instance of ArrayOfEventAlarmExpression from a dict
array_of_event_alarm_expression_form_dict = array_of_event_alarm_expression.from_dict(array_of_event_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


