# ScheduledTaskInfo

The scheduled task details. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**last_modified_time** | **datetime** | The time the scheduled task is created or modified.  | 
**last_modified_user** | **str** | Last user that modified the scheduled task.  | 
**next_run_time** | **datetime** | The next time the scheduled task will run.  | [optional] 
**prev_run_time** | **datetime** | The last time the scheduled task ran.  | [optional] 
**state** | [**TaskInfoStateEnum**](TaskInfoStateEnum.md) |  | 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 
**result** | [**Any**](Any.md) |  | [optional] 
**progress** | **int** | The task progress when the scheduled task state is \&quot;running\&quot;.  | [optional] 
**active_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**task_object** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.scheduled_task_info import ScheduledTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskInfo from a JSON string
scheduled_task_info_instance = ScheduledTaskInfo.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskInfo.to_json()

# convert the object into a dict
scheduled_task_info_dict = scheduled_task_info_instance.to_dict()
# create an instance of ScheduledTaskInfo from a dict
scheduled_task_info_form_dict = scheduled_task_info.from_dict(scheduled_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


