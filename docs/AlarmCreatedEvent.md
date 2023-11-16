# AlarmCreatedEvent

This event records the creation of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_created_event import AlarmCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmCreatedEvent from a JSON string
alarm_created_event_instance = AlarmCreatedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmCreatedEvent.to_json()

# convert the object into a dict
alarm_created_event_dict = alarm_created_event_instance.to_dict()
# create an instance of AlarmCreatedEvent from a dict
alarm_created_event_form_dict = alarm_created_event.from_dict(alarm_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


