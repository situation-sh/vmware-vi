# ScheduledTaskEmailCompletedEvent

This event records the sending of a notification via email for a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The destination email address.  | 

## Example

```python
from vmware_vi.models.scheduled_task_email_completed_event import ScheduledTaskEmailCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEmailCompletedEvent from a JSON string
scheduled_task_email_completed_event_instance = ScheduledTaskEmailCompletedEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskEmailCompletedEvent.to_json()

# convert the object into a dict
scheduled_task_email_completed_event_dict = scheduled_task_email_completed_event_instance.to_dict()
# create an instance of ScheduledTaskEmailCompletedEvent from a dict
scheduled_task_email_completed_event_form_dict = scheduled_task_email_completed_event.from_dict(scheduled_task_email_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


