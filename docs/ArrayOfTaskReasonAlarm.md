# ArrayOfTaskReasonAlarm

A boxed array of *TaskReasonAlarm*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskReasonAlarm]**](TaskReasonAlarm.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_reason_alarm import ArrayOfTaskReasonAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskReasonAlarm from a JSON string
array_of_task_reason_alarm_instance = ArrayOfTaskReasonAlarm.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskReasonAlarm.to_json()

# convert the object into a dict
array_of_task_reason_alarm_dict = array_of_task_reason_alarm_instance.to_dict()
# create an instance of ArrayOfTaskReasonAlarm from a dict
array_of_task_reason_alarm_form_dict = array_of_task_reason_alarm.from_dict(array_of_task_reason_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


