# ArrayOfScheduledTaskDetail

A boxed array of *ScheduledTaskDetail*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledTaskDetail]**](ScheduledTaskDetail.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_task_detail import ArrayOfScheduledTaskDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledTaskDetail from a JSON string
array_of_scheduled_task_detail_instance = ArrayOfScheduledTaskDetail.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledTaskDetail.to_json()

# convert the object into a dict
array_of_scheduled_task_detail_dict = array_of_scheduled_task_detail_instance.to_dict()
# create an instance of ArrayOfScheduledTaskDetail from a dict
array_of_scheduled_task_detail_form_dict = array_of_scheduled_task_detail.from_dict(array_of_scheduled_task_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


