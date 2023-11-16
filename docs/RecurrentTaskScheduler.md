# RecurrentTaskScheduler

The *RecurrentTaskScheduler* data object is the base type for the hierarchy that includes hourly, daily, weekly, and monthly task schedulers. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | How often to run the scheduled task.  The value must be greater than or equal to 1 and less than 1000. The default value is 1. The interval acts as a multiplier for the unit of time associated with a particular scheduler (hours, days, weeks, or months). For example, setting the *HourlyTaskScheduler* interval to 4 causes the task to run every 4 hours.  | 

## Example

```python
from vmware_vi.models.recurrent_task_scheduler import RecurrentTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrentTaskScheduler from a JSON string
recurrent_task_scheduler_instance = RecurrentTaskScheduler.from_json(json)
# print the JSON string representation of the object
print RecurrentTaskScheduler.to_json()

# convert the object into a dict
recurrent_task_scheduler_dict = recurrent_task_scheduler_instance.to_dict()
# create an instance of RecurrentTaskScheduler from a dict
recurrent_task_scheduler_form_dict = recurrent_task_scheduler.from_dict(recurrent_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


