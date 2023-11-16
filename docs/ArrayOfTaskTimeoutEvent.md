# ArrayOfTaskTimeoutEvent

A boxed array of *TaskTimeoutEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskTimeoutEvent]**](TaskTimeoutEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_timeout_event import ArrayOfTaskTimeoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskTimeoutEvent from a JSON string
array_of_task_timeout_event_instance = ArrayOfTaskTimeoutEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskTimeoutEvent.to_json()

# convert the object into a dict
array_of_task_timeout_event_dict = array_of_task_timeout_event_instance.to_dict()
# create an instance of ArrayOfTaskTimeoutEvent from a dict
array_of_task_timeout_event_form_dict = array_of_task_timeout_event.from_dict(array_of_task_timeout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


