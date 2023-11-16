# ArrayOfTaskReasonSchedule

A boxed array of *TaskReasonSchedule*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskReasonSchedule]**](TaskReasonSchedule.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_reason_schedule import ArrayOfTaskReasonSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskReasonSchedule from a JSON string
array_of_task_reason_schedule_instance = ArrayOfTaskReasonSchedule.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskReasonSchedule.to_json()

# convert the object into a dict
array_of_task_reason_schedule_dict = array_of_task_reason_schedule_instance.to_dict()
# create an instance of ArrayOfTaskReasonSchedule from a dict
array_of_task_reason_schedule_form_dict = array_of_task_reason_schedule.from_dict(array_of_task_reason_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


