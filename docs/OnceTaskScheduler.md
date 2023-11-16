# OnceTaskScheduler

The *OnceTaskScheduler* data object establishes the time for running a scheduled task only once. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_at** | **datetime** | The time a task will run.  If you do not set the time, it executes immediately.  | [optional] 

## Example

```python
from vmware_vi.models.once_task_scheduler import OnceTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of OnceTaskScheduler from a JSON string
once_task_scheduler_instance = OnceTaskScheduler.from_json(json)
# print the JSON string representation of the object
print OnceTaskScheduler.to_json()

# convert the object into a dict
once_task_scheduler_dict = once_task_scheduler_instance.to_dict()
# create an instance of OnceTaskScheduler from a dict
once_task_scheduler_form_dict = once_task_scheduler.from_dict(once_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


