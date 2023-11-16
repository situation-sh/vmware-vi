# ArrayOfDailyTaskScheduler

A boxed array of *DailyTaskScheduler*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DailyTaskScheduler]**](DailyTaskScheduler.md) |  | 

## Example

```python
from vmware_vi.models.array_of_daily_task_scheduler import ArrayOfDailyTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDailyTaskScheduler from a JSON string
array_of_daily_task_scheduler_instance = ArrayOfDailyTaskScheduler.from_json(json)
# print the JSON string representation of the object
print ArrayOfDailyTaskScheduler.to_json()

# convert the object into a dict
array_of_daily_task_scheduler_dict = array_of_daily_task_scheduler_instance.to_dict()
# create an instance of ArrayOfDailyTaskScheduler from a dict
array_of_daily_task_scheduler_form_dict = array_of_daily_task_scheduler.from_dict(array_of_daily_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


