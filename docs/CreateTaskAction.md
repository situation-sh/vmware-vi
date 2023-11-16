# CreateTaskAction

This data object type specifies the type of task to be created when this action is triggered.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_type_id** | **str** | Extension registered task type identifier for type of task being created.  ***Since:*** VI API 2.5  | 
**cancelable** | **bool** | Whether the task should be cancelable.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.create_task_action import CreateTaskAction

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskAction from a JSON string
create_task_action_instance = CreateTaskAction.from_json(json)
# print the JSON string representation of the object
print CreateTaskAction.to_json()

# convert the object into a dict
create_task_action_dict = create_task_action_instance.to_dict()
# create an instance of CreateTaskAction from a dict
create_task_action_form_dict = create_task_action.from_dict(create_task_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


