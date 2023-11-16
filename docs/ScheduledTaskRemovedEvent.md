# ScheduledTaskRemovedEvent

This event records the removal of a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.scheduled_task_removed_event import ScheduledTaskRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskRemovedEvent from a JSON string
scheduled_task_removed_event_instance = ScheduledTaskRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskRemovedEvent.to_json()

# convert the object into a dict
scheduled_task_removed_event_dict = scheduled_task_removed_event_instance.to_dict()
# create an instance of ScheduledTaskRemovedEvent from a dict
scheduled_task_removed_event_form_dict = scheduled_task_removed_event.from_dict(scheduled_task_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


