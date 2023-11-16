# ArrayOfTaskReason

A boxed array of *TaskReason*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskReason]**](TaskReason.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_reason import ArrayOfTaskReason

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskReason from a JSON string
array_of_task_reason_instance = ArrayOfTaskReason.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskReason.to_json()

# convert the object into a dict
array_of_task_reason_dict = array_of_task_reason_instance.to_dict()
# create an instance of ArrayOfTaskReason from a dict
array_of_task_reason_form_dict = array_of_task_reason.from_dict(array_of_task_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


