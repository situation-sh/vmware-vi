# ArrayOfScheduledTaskDescription

A boxed array of *ScheduledTaskDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledTaskDescription]**](ScheduledTaskDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_task_description import ArrayOfScheduledTaskDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledTaskDescription from a JSON string
array_of_scheduled_task_description_instance = ArrayOfScheduledTaskDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledTaskDescription.to_json()

# convert the object into a dict
array_of_scheduled_task_description_dict = array_of_scheduled_task_description_instance.to_dict()
# create an instance of ArrayOfScheduledTaskDescription from a dict
array_of_scheduled_task_description_form_dict = array_of_scheduled_task_description.from_dict(array_of_scheduled_task_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


