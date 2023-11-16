# ArrayOfAfterStartupTaskScheduler

A boxed array of *AfterStartupTaskScheduler*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AfterStartupTaskScheduler]**](AfterStartupTaskScheduler.md) |  | 

## Example

```python
from vmware_vi.models.array_of_after_startup_task_scheduler import ArrayOfAfterStartupTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAfterStartupTaskScheduler from a JSON string
array_of_after_startup_task_scheduler_instance = ArrayOfAfterStartupTaskScheduler.from_json(json)
# print the JSON string representation of the object
print ArrayOfAfterStartupTaskScheduler.to_json()

# convert the object into a dict
array_of_after_startup_task_scheduler_dict = array_of_after_startup_task_scheduler_instance.to_dict()
# create an instance of ArrayOfAfterStartupTaskScheduler from a dict
array_of_after_startup_task_scheduler_form_dict = array_of_after_startup_task_scheduler.from_dict(array_of_after_startup_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


