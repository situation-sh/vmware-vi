# ScheduledTaskEvent

These events are scheduled task events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_task** | [**ScheduledTaskEventArgument**](ScheduledTaskEventArgument.md) |  | 
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.scheduled_task_event import ScheduledTaskEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEvent from a JSON string
scheduled_task_event_instance = ScheduledTaskEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskEvent.to_json()

# convert the object into a dict
scheduled_task_event_dict = scheduled_task_event_instance.to_dict()
# create an instance of ScheduledTaskEvent from a dict
scheduled_task_event_form_dict = scheduled_task_event.from_dict(scheduled_task_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


