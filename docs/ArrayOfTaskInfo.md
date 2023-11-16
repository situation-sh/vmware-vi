# ArrayOfTaskInfo

A boxed array of *TaskInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskInfo]**](TaskInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_info import ArrayOfTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskInfo from a JSON string
array_of_task_info_instance = ArrayOfTaskInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskInfo.to_json()

# convert the object into a dict
array_of_task_info_dict = array_of_task_info_instance.to_dict()
# create an instance of ArrayOfTaskInfo from a dict
array_of_task_info_form_dict = array_of_task_info.from_dict(array_of_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


