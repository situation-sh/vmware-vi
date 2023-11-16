# AlarmEmailCompletedEvent

This event records the completion of an alarm email notification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**to** | **str** | The destination email address.  | 

## Example

```python
from vmware_vi.models.alarm_email_completed_event import AlarmEmailCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEmailCompletedEvent from a JSON string
alarm_email_completed_event_instance = AlarmEmailCompletedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmEmailCompletedEvent.to_json()

# convert the object into a dict
alarm_email_completed_event_dict = alarm_email_completed_event_instance.to_dict()
# create an instance of AlarmEmailCompletedEvent from a dict
alarm_email_completed_event_form_dict = alarm_email_completed_event.from_dict(alarm_email_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


