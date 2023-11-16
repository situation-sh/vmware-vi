# EventAlarmExpressionComparison

Encapsulates Comparison of an event's attribute to a value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The attribute of the event to compare  ***Since:*** vSphere API 4.0  | 
**operator** | **str** | An operator from the list above  ***Since:*** vSphere API 4.0  | 
**value** | **str** | The value to compare against  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.event_alarm_expression_comparison import EventAlarmExpressionComparison

# TODO update the JSON string below
json = "{}"
# create an instance of EventAlarmExpressionComparison from a JSON string
event_alarm_expression_comparison_instance = EventAlarmExpressionComparison.from_json(json)
# print the JSON string representation of the object
print EventAlarmExpressionComparison.to_json()

# convert the object into a dict
event_alarm_expression_comparison_dict = event_alarm_expression_comparison_instance.to_dict()
# create an instance of EventAlarmExpressionComparison from a dict
event_alarm_expression_comparison_form_dict = event_alarm_expression_comparison.from_dict(event_alarm_expression_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


