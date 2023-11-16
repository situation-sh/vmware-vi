# MonthlyByWeekdayTaskScheduler

The *MonthlyByWeekdayTaskScheduler* data object sets the time for monthly task execution.  You identify a single day for task execution by specifying the week of the month and day of the week, and you complete the schedule by setting the inherited properties for the hour and minute.  By default, the scheduler executes the task on the specified day every month. If you set the interval to a value greater than 1, the task will execute at the specified monthly interval. (For example, an interval of 2 will cause the task to execute on the specified day, hour, and minute every 2 months.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | [**WeekOfMonthEnum**](WeekOfMonthEnum.md) |  | 
**weekday** | [**DayOfWeekEnum**](DayOfWeekEnum.md) |  | 

## Example

```python
from vmware_vi.models.monthly_by_weekday_task_scheduler import MonthlyByWeekdayTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyByWeekdayTaskScheduler from a JSON string
monthly_by_weekday_task_scheduler_instance = MonthlyByWeekdayTaskScheduler.from_json(json)
# print the JSON string representation of the object
print MonthlyByWeekdayTaskScheduler.to_json()

# convert the object into a dict
monthly_by_weekday_task_scheduler_dict = monthly_by_weekday_task_scheduler_instance.to_dict()
# create an instance of MonthlyByWeekdayTaskScheduler from a dict
monthly_by_weekday_task_scheduler_form_dict = monthly_by_weekday_task_scheduler.from_dict(monthly_by_weekday_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


