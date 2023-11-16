# ArrayOfTaskEvent

A boxed array of *TaskEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskEvent]**](TaskEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_event import ArrayOfTaskEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskEvent from a JSON string
array_of_task_event_instance = ArrayOfTaskEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskEvent.to_json()

# convert the object into a dict
array_of_task_event_dict = array_of_task_event_instance.to_dict()
# create an instance of ArrayOfTaskEvent from a dict
array_of_task_event_form_dict = array_of_task_event.from_dict(array_of_task_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


