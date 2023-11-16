# ScheduledTaskStartedEvent

This event records when a scheduled task started. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.scheduled_task_started_event import ScheduledTaskStartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskStartedEvent from a JSON string
scheduled_task_started_event_instance = ScheduledTaskStartedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskStartedEvent.to_json()

# convert the object into a dict
scheduled_task_started_event_dict = scheduled_task_started_event_instance.to_dict()
# create an instance of ScheduledTaskStartedEvent from a dict
scheduled_task_started_event_form_dict = scheduled_task_started_event.from_dict(scheduled_task_started_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


