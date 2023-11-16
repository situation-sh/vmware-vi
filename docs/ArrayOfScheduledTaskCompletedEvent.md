# ArrayOfScheduledTaskCompletedEvent

A boxed array of *ScheduledTaskCompletedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledTaskCompletedEvent]**](ScheduledTaskCompletedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_task_completed_event import ArrayOfScheduledTaskCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledTaskCompletedEvent from a JSON string
array_of_scheduled_task_completed_event_instance = ArrayOfScheduledTaskCompletedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledTaskCompletedEvent.to_json()

# convert the object into a dict
array_of_scheduled_task_completed_event_dict = array_of_scheduled_task_completed_event_instance.to_dict()
# create an instance of ArrayOfScheduledTaskCompletedEvent from a dict
array_of_scheduled_task_completed_event_form_dict = array_of_scheduled_task_completed_event.from_dict(array_of_scheduled_task_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


