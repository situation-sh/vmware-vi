# TaskFilterSpec

This data object type defines the specification for the task filter used to query tasks in the history collector database.  The client creates a task history collector with a filter specification, then retrieves the tasks from the task history collector. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**TaskFilterSpecByEntity**](TaskFilterSpecByEntity.md) |  | [optional] 
**time** | [**TaskFilterSpecByTime**](TaskFilterSpecByTime.md) |  | [optional] 
**user_name** | [**TaskFilterSpecByUsername**](TaskFilterSpecByUsername.md) |  | [optional] 
**activation_id** | **List[str]** | This property, if provided, limits the set of collected tasks to those associated with the specified activation Ids.  ***Since:*** vSphere API 6.0  | [optional] 
**state** | [**List[TaskInfoStateEnum]**](TaskInfoStateEnum.md) | This property, if provided, limits the set of collected tasks by their states.  Task states are enumerated in *State*. If not provided, tasks are collected regardless of their state.  | [optional] 
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**scheduled_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**event_chain_id** | **List[int]** | The filter specification for retrieving tasks by chain ID.  If it is set, tasks not with the given *TaskInfo.eventChainId* will be filtered out. If the property is not set, tasks&#39; chain ID is disregarded for filtering purposes.  ***Since:*** vSphere API 4.0  | [optional] 
**tag** | **List[str]** | The filter specification for retrieving tasks by *tag*.  If it is set, tasks not with the given tag(s) will be filtered out. If the property is not set, tasks&#39; tag is disregarded for filtering purposes. If it is set, and includes an empty string, tasks without a tag will be returned.  ***Since:*** vSphere API 4.0  | [optional] 
**parent_task_key** | **List[str]** | The filter specification for retrieving tasks by *TaskInfo.parentTaskKey*.  If it is set, tasks not with the given parentTaskKey(s) will be filtered out. If the property is not set, tasks&#39; parentTaskKey is disregarded for filtering purposes.  ***Since:*** vSphere API 4.0  | [optional] 
**root_task_key** | **List[str]** | The filter specification for retrieving tasks by *TaskInfo.rootTaskKey*.  If it is set, tasks not with the given rootTaskKey(s) will be filtered out. If the property is not set, tasks&#39; rootTaskKey is disregarded for filtering purposes.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.task_filter_spec import TaskFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFilterSpec from a JSON string
task_filter_spec_instance = TaskFilterSpec.from_json(json)
# print the JSON string representation of the object
print TaskFilterSpec.to_json()

# convert the object into a dict
task_filter_spec_dict = task_filter_spec_instance.to_dict()
# create an instance of TaskFilterSpec from a dict
task_filter_spec_form_dict = task_filter_spec.from_dict(task_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


