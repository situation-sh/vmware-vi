# HourlyTaskScheduler

The *HourlyTaskScheduler* data object sets the time for hourly task execution.  By default, the scheduled task will run once every hour, at the specified minute.  If you set the interval to a value greater than 1, the task will execute at the specified hourly interval. (For example, an interval of 2 will cause the task to execute at the specified minute every 2 hours.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | **int** | The minute at which the *RecurrentTaskScheduler* runs the task.  Specify the minute value as a UTC (Coordinated Universal Time) value in the range 0 to 59.  For vCenter 2.x and prior releases, use the server&#39;s local time. For example, use Australia Northern Territory (UTC +9:30) or Indian (UTC +5:30) time values, rather than a UTC value.  | 

## Example

```python
from vmware_vi.models.hourly_task_scheduler import HourlyTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of HourlyTaskScheduler from a JSON string
hourly_task_scheduler_instance = HourlyTaskScheduler.from_json(json)
# print the JSON string representation of the object
print HourlyTaskScheduler.to_json()

# convert the object into a dict
hourly_task_scheduler_dict = hourly_task_scheduler_instance.to_dict()
# create an instance of HourlyTaskScheduler from a dict
hourly_task_scheduler_form_dict = hourly_task_scheduler.from_dict(hourly_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


