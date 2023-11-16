# ScheduledTaskFailedEvent

This event records the failure of a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.scheduled_task_failed_event import ScheduledTaskFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskFailedEvent from a JSON string
scheduled_task_failed_event_instance = ScheduledTaskFailedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskFailedEvent.to_json()

# convert the object into a dict
scheduled_task_failed_event_dict = scheduled_task_failed_event_instance.to_dict()
# create an instance of ScheduledTaskFailedEvent from a dict
scheduled_task_failed_event_form_dict = scheduled_task_failed_event.from_dict(scheduled_task_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


