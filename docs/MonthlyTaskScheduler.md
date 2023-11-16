# MonthlyTaskScheduler

The *MonthlyTaskScheduler* data object is the base type for the monthly schedulers (*MonthlyByDayTaskScheduler* and *MonthlyByWeekdayTaskScheduler*). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.monthly_task_scheduler import MonthlyTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyTaskScheduler from a JSON string
monthly_task_scheduler_instance = MonthlyTaskScheduler.from_json(json)
# print the JSON string representation of the object
print MonthlyTaskScheduler.to_json()

# convert the object into a dict
monthly_task_scheduler_dict = monthly_task_scheduler_instance.to_dict()
# create an instance of MonthlyTaskScheduler from a dict
monthly_task_scheduler_form_dict = monthly_task_scheduler.from_dict(monthly_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


