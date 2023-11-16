# MetricAlarmExpression

An alarm expression that uses a metric as the condition that triggers an alarm.  Base type.  There are two alarm operands: yellow and red. At least one of them must be set. The value of the alarm expression is determined as follows: - If the host is not connected, the host metric expression is gray. - If the vm is not connected, the vm metric expression is gray. - If red is set but yellow is not, the expression is red when   the metric is over (isAbove operator) or under (isBelow operator)   the red value. Otherwise, the expression is green. - If yellow is set but red is not, the expression is yellow when   the metric is over (isAbove) or under (isBelow)   the yellow value. Otherwise, the expression is green. - If both yellow and red are set, the value of the expression is red   when the metric is over (isAbove) or under (isBelow) the red value.   Otherwise, the expression is yellow when the metric is over (isAbove)   or under (isBelow) the yellow value. Otherwise, the expression is green. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**MetricAlarmOperatorEnum**](MetricAlarmOperatorEnum.md) |  | 
**type** | **str** | Name of the object type containing the property.  | 
**metric** | [**PerfMetricId**](PerfMetricId.md) |  | 
**yellow** | **int** | Whether or not to test for a yellow condition.  If not set, do not calculate yellow status. If set, it contains the threshold value that triggers yellow status.  | [optional] 
**yellow_interval** | **int** | Time interval in seconds for which the yellow condition must be true before the yellow status is triggered.  If unset, the yellow status is triggered immediately when the yellow condition becomes true.  ***Since:*** vSphere API 4.0  | [optional] 
**red** | **int** | Whether or not to test for a red condition.  If not set, do not calculate red status. If set, it contains the threshold value that triggers red status.  | [optional] 
**red_interval** | **int** | Time interval in seconds for which the red condition must be true before the red status is triggered.  If unset, the red status is triggered immediately when the red condition becomes true.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.metric_alarm_expression import MetricAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MetricAlarmExpression from a JSON string
metric_alarm_expression_instance = MetricAlarmExpression.from_json(json)
# print the JSON string representation of the object
print MetricAlarmExpression.to_json()

# convert the object into a dict
metric_alarm_expression_dict = metric_alarm_expression_instance.to_dict()
# create an instance of MetricAlarmExpression from a dict
metric_alarm_expression_form_dict = metric_alarm_expression.from_dict(metric_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


