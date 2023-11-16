# TaskInfoState

A boxed *TaskInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TaskInfoStateEnum**](TaskInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.task_info_state import TaskInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInfoState from a JSON string
task_info_state_instance = TaskInfoState.from_json(json)
# print the JSON string representation of the object
print TaskInfoState.to_json()

# convert the object into a dict
task_info_state_dict = task_info_state_instance.to_dict()
# create an instance of TaskInfoState from a dict
task_info_state_form_dict = task_info_state.from_dict(task_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


