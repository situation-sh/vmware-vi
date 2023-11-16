# ArrayOfScheduledTaskInfo

A boxed array of *ScheduledTaskInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledTaskInfo]**](ScheduledTaskInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_task_info import ArrayOfScheduledTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledTaskInfo from a JSON string
array_of_scheduled_task_info_instance = ArrayOfScheduledTaskInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledTaskInfo.to_json()

# convert the object into a dict
array_of_scheduled_task_info_dict = array_of_scheduled_task_info_instance.to_dict()
# create an instance of ArrayOfScheduledTaskInfo from a dict
array_of_scheduled_task_info_form_dict = array_of_scheduled_task_info.from_dict(array_of_scheduled_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


