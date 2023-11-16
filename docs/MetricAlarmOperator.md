# MetricAlarmOperator

A boxed *MetricAlarmOperator_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**MetricAlarmOperatorEnum**](MetricAlarmOperatorEnum.md) |  | 

## Example

```python
from vmware_vi.models.metric_alarm_operator import MetricAlarmOperator

# TODO update the JSON string below
json = "{}"
# create an instance of MetricAlarmOperator from a JSON string
metric_alarm_operator_instance = MetricAlarmOperator.from_json(json)
# print the JSON string representation of the object
print MetricAlarmOperator.to_json()

# convert the object into a dict
metric_alarm_operator_dict = metric_alarm_operator_instance.to_dict()
# create an instance of MetricAlarmOperator from a dict
metric_alarm_operator_form_dict = metric_alarm_operator.from_dict(metric_alarm_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


