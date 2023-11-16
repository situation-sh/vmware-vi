# ArrayOfCreateTaskAction

A boxed array of *CreateTaskAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CreateTaskAction]**](CreateTaskAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_create_task_action import ArrayOfCreateTaskAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCreateTaskAction from a JSON string
array_of_create_task_action_instance = ArrayOfCreateTaskAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfCreateTaskAction.to_json()

# convert the object into a dict
array_of_create_task_action_dict = array_of_create_task_action_instance.to_dict()
# create an instance of ArrayOfCreateTaskAction from a dict
array_of_create_task_action_form_dict = array_of_create_task_action.from_dict(array_of_create_task_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


