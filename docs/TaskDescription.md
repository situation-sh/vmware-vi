# TaskDescription

Static strings for task objects.  These strings are locale-specific. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_info** | [**List[ElementDescription]**](ElementDescription.md) | Display label and summary for all tasks  | 
**state** | [**List[ElementDescription]**](ElementDescription.md) | *TaskInfo State enum*  | 
**reason** | [**List[TypeDescription]**](TypeDescription.md) | Kind of entity responsible for creating this task.  | 

## Example

```python
from vmware_vi.models.task_description import TaskDescription

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDescription from a JSON string
task_description_instance = TaskDescription.from_json(json)
# print the JSON string representation of the object
print TaskDescription.to_json()

# convert the object into a dict
task_description_dict = task_description_instance.to_dict()
# create an instance of TaskDescription from a dict
task_description_form_dict = task_description.from_dict(task_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


