# AfterStartupTaskScheduler

The *AfterStartupTaskScheduler* data object establishes the time that a scheduled task will run after the vCenter server restarts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | **int** | The delay in minutes after vCenter server is restarted.  The value must be greater than or equal to 0.  | 

## Example

```python
from vmware_vi.models.after_startup_task_scheduler import AfterStartupTaskScheduler

# TODO update the JSON string below
json = "{}"
# create an instance of AfterStartupTaskScheduler from a JSON string
after_startup_task_scheduler_instance = AfterStartupTaskScheduler.from_json(json)
# print the JSON string representation of the object
print AfterStartupTaskScheduler.to_json()

# convert the object into a dict
after_startup_task_scheduler_dict = after_startup_task_scheduler_instance.to_dict()
# create an instance of AfterStartupTaskScheduler from a dict
after_startup_task_scheduler_form_dict = after_startup_task_scheduler.from_dict(after_startup_task_scheduler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


