# ArrayOfTaskScheduler

A boxed array of *TaskScheduler*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskScheduler]**](TaskScheduler.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_scheduler import ArrayOfTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskScheduler from a JSON string
array_of_task_scheduler_instance = ArrayOfTaskScheduler.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskScheduler.to_json()

# convert the object into a dict
array_of_task_scheduler_dict = array_of_task_scheduler_instance.to_dict()
# create an instance of ArrayOfTaskScheduler from a dict
array_of_task_scheduler_form_dict = array_of_task_scheduler.from_dict(array_of_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


