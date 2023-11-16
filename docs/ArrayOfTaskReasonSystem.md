# ArrayOfTaskReasonSystem

A boxed array of *TaskReasonSystem*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskReasonSystem]**](TaskReasonSystem.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_reason_system import ArrayOfTaskReasonSystem

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskReasonSystem from a JSON string
array_of_task_reason_system_instance = ArrayOfTaskReasonSystem.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskReasonSystem.to_json()

# convert the object into a dict
array_of_task_reason_system_dict = array_of_task_reason_system_instance.to_dict()
# create an instance of ArrayOfTaskReasonSystem from a dict
array_of_task_reason_system_form_dict = array_of_task_reason_system.from_dict(array_of_task_reason_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


