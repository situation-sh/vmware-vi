# ArrayOfOnceTaskScheduler

A boxed array of *OnceTaskScheduler*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OnceTaskScheduler]**](OnceTaskScheduler.md) |  | 

## Example

```python
from vmware_vi.models.array_of_once_task_scheduler import ArrayOfOnceTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOnceTaskScheduler from a JSON string
array_of_once_task_scheduler_instance = ArrayOfOnceTaskScheduler.from_json(json)
# print the JSON string representation of the object
print ArrayOfOnceTaskScheduler.to_json()

# convert the object into a dict
array_of_once_task_scheduler_dict = array_of_once_task_scheduler_instance.to_dict()
# create an instance of ArrayOfOnceTaskScheduler from a dict
array_of_once_task_scheduler_form_dict = array_of_once_task_scheduler.from_dict(array_of_once_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


