# ScheduledTaskEmailFailedEvent

This event records the failure of an attempt to send a notification via email for a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The destination email address.  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.scheduled_task_email_failed_event import ScheduledTaskEmailFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEmailFailedEvent from a JSON string
scheduled_task_email_failed_event_instance = ScheduledTaskEmailFailedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskEmailFailedEvent.to_json()

# convert the object into a dict
scheduled_task_email_failed_event_dict = scheduled_task_email_failed_event_instance.to_dict()
# create an instance of ScheduledTaskEmailFailedEvent from a dict
scheduled_task_email_failed_event_form_dict = scheduled_task_email_failed_event.from_dict(scheduled_task_email_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


