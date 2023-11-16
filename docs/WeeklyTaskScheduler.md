# WeeklyTaskScheduler

The *WeeklyTaskScheduler* data object sets the time for weekly task execution.  You can set the schedule for task execution on one or more days during the week, and you complete the schedule by setting the inherited properties for the hour and minute.  By default the scheduler executes the task according to the specified day(s) every week. If you set the interval to a value greater than 1, the task will execute at the specified weekly interval. (For example, an interval of 2 will cause the task to execute on the specified days every 2 weeks.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sunday** | **bool** | The day or days of the week when the scheduled task will run.  At least one of the days must be true.  | 
**monday** | **bool** |  | 
**tuesday** | **bool** |  | 
**wednesday** | **bool** |  | 
**thursday** | **bool** |  | 
**friday** | **bool** |  | 
**saturday** | **bool** |  | 

## Example

```python
from vmware_vi.models.weekly_task_scheduler import WeeklyTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyTaskScheduler from a JSON string
weekly_task_scheduler_instance = WeeklyTaskScheduler.from_json(json)
# print the JSON string representation of the object
print WeeklyTaskScheduler.to_json()

# convert the object into a dict
weekly_task_scheduler_dict = weekly_task_scheduler_instance.to_dict()
# create an instance of WeeklyTaskScheduler from a dict
weekly_task_scheduler_form_dict = weekly_task_scheduler.from_dict(weekly_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


