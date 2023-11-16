# AlarmStatusChangedEvent

This event records a status change for an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**var_from** | **str** | The original alarm status.  | 
**to** | **str** | The new alarm status.  | 

## Example

```python
from vmware_vi.models.alarm_status_changed_event import AlarmStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmStatusChangedEvent from a JSON string
alarm_status_changed_event_instance = AlarmStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmStatusChangedEvent.to_json()

# convert the object into a dict
alarm_status_changed_event_dict = alarm_status_changed_event_instance.to_dict()
# create an instance of AlarmStatusChangedEvent from a dict
alarm_status_changed_event_form_dict = alarm_status_changed_event.from_dict(alarm_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


