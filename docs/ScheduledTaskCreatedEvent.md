# ScheduledTaskCreatedEvent

This event records the creation of a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.scheduled_task_created_event import ScheduledTaskCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskCreatedEvent from a JSON string
scheduled_task_created_event_instance = ScheduledTaskCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskCreatedEvent.to_json()

# convert the object into a dict
scheduled_task_created_event_dict = scheduled_task_created_event_instance.to_dict()
# create an instance of ScheduledTaskCreatedEvent from a dict
scheduled_task_created_event_form_dict = scheduled_task_created_event.from_dict(scheduled_task_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


