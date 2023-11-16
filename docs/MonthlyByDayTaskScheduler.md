# MonthlyByDayTaskScheduler

The *MonthlyByDayTaskScheduler* data object sets the time for monthly task execution.  You can set the schedule for task execution on one day during the month, and you complete the schedule by setting the inherited properties for the hour and minute.  By default the scheduler executes the task on the specified day every month. If you set the interval to a value greater than 1, the task will execute at the specified monthly interval. (For example, an interval of 2 will cause the task to execute on the specified day, hour, and minute every 2 months.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | The day in every month to run the scheduled task.  Valid values are 1 to 31.  In any month where the value of \&quot;day\&quot; exceeds the total number of days in the month, the scheduled task will run on the last day of the month.  | 

## Example

```python
from vmware_vi.models.monthly_by_day_task_scheduler import MonthlyByDayTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyByDayTaskScheduler from a JSON string
monthly_by_day_task_scheduler_instance = MonthlyByDayTaskScheduler.from_json(json)
# print the JSON string representation of the object
print MonthlyByDayTaskScheduler.to_json()

# convert the object into a dict
monthly_by_day_task_scheduler_dict = monthly_by_day_task_scheduler_instance.to_dict()
# create an instance of MonthlyByDayTaskScheduler from a dict
monthly_by_day_task_scheduler_form_dict = monthly_by_day_task_scheduler.from_dict(monthly_by_day_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


