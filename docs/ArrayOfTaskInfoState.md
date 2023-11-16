# ArrayOfTaskInfoState

A boxed array of *TaskInfoState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskInfoStateEnum]**](TaskInfoStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_info_state import ArrayOfTaskInfoState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskInfoState from a JSON string
array_of_task_info_state_instance = ArrayOfTaskInfoState.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskInfoState.to_json()

# convert the object into a dict
array_of_task_info_state_dict = array_of_task_info_state_instance.to_dict()
# create an instance of ArrayOfTaskInfoState from a dict
array_of_task_info_state_form_dict = array_of_task_info_state.from_dict(array_of_task_info_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


