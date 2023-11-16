# DailyTaskScheduler

The *DailyTaskScheduler* data object sets the time for daily task execution.  You set the hour and the inherited minute property to complete the schedule. By default, the scheduled task will run once every day at the specified hour and minute.  If you set the interval to a value greater than 1, the task will execute at the specified daily interval. (For example, an interval of 2 will cause the task to execute at the specified hour and minute every 2 days.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | The hour at which the *RecurrentTaskScheduler* runs the task.  Use UTC (Coordinated Universal Time) values in the range 0 to 23, where 0 &#x3D; 12:00 a.m. (UTC) and 12 &#x3D; 12:00 p.m. (UTC).  For vCenter 2.x and prior releases, use the server&#39;s local time. For example, use Eastern Standard Time (EST) or Pacific Daylight Time (PDT), rather than UTC.  | 

## Example

```python
from vmware_vi.models.daily_task_scheduler import DailyTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of DailyTaskScheduler from a JSON string
daily_task_scheduler_instance = DailyTaskScheduler.from_json(json)
# print the JSON string representation of the object
print DailyTaskScheduler.to_json()

# convert the object into a dict
daily_task_scheduler_dict = daily_task_scheduler_instance.to_dict()
# create an instance of DailyTaskScheduler from a dict
daily_task_scheduler_form_dict = daily_task_scheduler.from_dict(daily_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


