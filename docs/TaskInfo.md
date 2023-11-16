# TaskInfo

This data object type contains all information about a task.  A task represents an operation performed by VirtualCenter or ESX. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique key for the task.  | 
**task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**description** | [**LocalizableMessage**](LocalizableMessage.md) |  | [optional] 
**name** | **str** | The name of the operation that created the task.  This is not set for internal tasks.  | [optional] 
**description_id** | **str** | An identifier for this operation.  This includes publicly visible internal tasks and is a lookup in the TaskDescription methodInfo data object.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**entity_name** | **str** | The name of the managed entity, locale-specific, retained for the history collector database.  | [optional] 
**locked** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If the state of the task is \&quot;running\&quot;, then this property is a list of managed entities that the operation has locked, with a shared lock.  Refers instances of *ManagedEntity*.  | [optional] 
**state** | [**TaskInfoStateEnum**](TaskInfoStateEnum.md) |  | 
**cancelled** | **bool** | Flag to indicate whether or not the client requested cancellation of the task.  | 
**cancelable** | **bool** | Flag to indicate whether or not the cancel task operation is supported.  | 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 
**result** | [**Any**](Any.md) |  | [optional] 
**progress** | **int** | If the task state is \&quot;running\&quot;, then this property contains a progress measurement, expressed as percentage completed, from 0 to 100.  If this property is not set, then the command does not report progress.  | [optional] 
**progress_details** | [**List[KeyAnyValue]**](KeyAnyValue.md) |  | [optional] 
**reason** | [**TaskReason**](TaskReason.md) |  | 
**queue_time** | **datetime** | Time stamp when the task was created.  | 
**start_time** | **datetime** | Time stamp when the task started running.  | [optional] 
**complete_time** | **datetime** | Time stamp when the task was completed (whether success or failure).  | [optional] 
**event_chain_id** | **int** | Event chain ID that leads to the corresponding events.  | 
**change_tag** | **str** | The user entered tag to identify the operations and their side effects  ***Since:*** vSphere API 4.0  | [optional] 
**parent_task_key** | **str** | Tasks can be created by another task.  This shows *TaskInfo.key* of the task spun off this task. This is to track causality between tasks.  ***Since:*** vSphere API 4.0  | [optional] 
**root_task_key** | **str** | Tasks can be created by another task and such creation can go on for multiple levels.  This is the *TaskInfo.key* of the task that started the chain of tasks.  ***Since:*** vSphere API 4.0  | [optional] 
**activation_id** | **str** | The activation Id is a client-provided token to link an API call with a task.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.task_info import TaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInfo from a JSON string
task_info_instance = TaskInfo.from_json(json)
# print the JSON string representation of the object
print TaskInfo.to_json()

# convert the object into a dict
task_info_dict = task_info_instance.to_dict()
# create an instance of TaskInfo from a dict
task_info_form_dict = task_info.from_dict(task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


