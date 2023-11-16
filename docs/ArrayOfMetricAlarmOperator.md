# ArrayOfMetricAlarmOperator

A boxed array of *MetricAlarmOperator_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MetricAlarmOperatorEnum]**](MetricAlarmOperatorEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_metric_alarm_operator import ArrayOfMetricAlarmOperator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMetricAlarmOperator from a JSON string
array_of_metric_alarm_operator_instance = ArrayOfMetricAlarmOperator.from_json(json)
# print the JSON string representation of the object
print ArrayOfMetricAlarmOperator.to_json()

# convert the object into a dict
array_of_metric_alarm_operator_dict = array_of_metric_alarm_operator_instance.to_dict()
# create an instance of ArrayOfMetricAlarmOperator from a dict
array_of_metric_alarm_operator_form_dict = array_of_metric_alarm_operator.from_dict(array_of_metric_alarm_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


