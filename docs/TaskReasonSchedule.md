# TaskReasonSchedule

Indicates that the task was queued by a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scheduled task that queued this task.  | 
**scheduled_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.task_reason_schedule import TaskReasonSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TaskReasonSchedule from a JSON string
task_reason_schedule_instance = TaskReasonSchedule.from_json(json)
# print the JSON string representation of the object
print TaskReasonSchedule.to_json()

# convert the object into a dict
task_reason_schedule_dict = task_reason_schedule_instance.to_dict()
# create an instance of TaskReasonSchedule from a dict
task_reason_schedule_form_dict = task_reason_schedule.from_dict(task_reason_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


