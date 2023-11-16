# ScheduledTaskCompletedEvent

This event records the completion of a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.scheduled_task_completed_event import ScheduledTaskCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskCompletedEvent from a JSON string
scheduled_task_completed_event_instance = ScheduledTaskCompletedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskCompletedEvent.to_json()

# convert the object into a dict
scheduled_task_completed_event_dict = scheduled_task_completed_event_instance.to_dict()
# create an instance of ScheduledTaskCompletedEvent from a dict
scheduled_task_completed_event_form_dict = scheduled_task_completed_event.from_dict(scheduled_task_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


