# ScheduledTaskDescription

Static strings for scheduled tasks.  These strings are locale-specific. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**List[TypeDescription]**](TypeDescription.md) | Action class descriptions for a scheduled task.  | 
**scheduler_info** | [**List[ScheduledTaskDetail]**](ScheduledTaskDetail.md) | Scheduler class description details.  | 
**state** | [**List[ElementDescription]**](ElementDescription.md) | *TaskInfo State enum*  | 
**day_of_week** | [**List[ElementDescription]**](ElementDescription.md) | *MonthlyByWeekdayTaskScheduler Days of the week enum description*  | 
**week_of_month** | [**List[ElementDescription]**](ElementDescription.md) | *MonthlyByWeekdayTaskScheduler Week of the month enum description*  | 

## Example

```python
from vmware_vi.models.scheduled_task_description import ScheduledTaskDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskDescription from a JSON string
scheduled_task_description_instance = ScheduledTaskDescription.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskDescription.to_json()

# convert the object into a dict
scheduled_task_description_dict = scheduled_task_description_instance.to_dict()
# create an instance of ScheduledTaskDescription from a dict
scheduled_task_description_form_dict = scheduled_task_description.from_dict(scheduled_task_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


