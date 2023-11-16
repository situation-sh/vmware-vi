# ScheduledTaskEventArgument

The event argument is a scheduled task object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.scheduled_task_event_argument import ScheduledTaskEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEventArgument from a JSON string
scheduled_task_event_argument_instance = ScheduledTaskEventArgument.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskEventArgument.to_json()

# convert the object into a dict
scheduled_task_event_argument_dict = scheduled_task_event_argument_instance.to_dict()
# create an instance of ScheduledTaskEventArgument from a dict
scheduled_task_event_argument_form_dict = scheduled_task_event_argument.from_dict(scheduled_task_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


