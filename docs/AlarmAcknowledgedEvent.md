# AlarmAcknowledgedEvent

This event records the acknowledgement of an Alarm  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_acknowledged_event import AlarmAcknowledgedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmAcknowledgedEvent from a JSON string
alarm_acknowledged_event_instance = AlarmAcknowledgedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmAcknowledgedEvent.to_json()

# convert the object into a dict
alarm_acknowledged_event_dict = alarm_acknowledged_event_instance.to_dict()
# create an instance of AlarmAcknowledgedEvent from a dict
alarm_acknowledged_event_form_dict = alarm_acknowledged_event.from_dict(alarm_acknowledged_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


