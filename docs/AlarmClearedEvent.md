# AlarmClearedEvent

This event records the manual clearing of an Alarm  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**var_from** | **str** | The original alarm status from which it was cleared  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.alarm_cleared_event import AlarmClearedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmClearedEvent from a JSON string
alarm_cleared_event_instance = AlarmClearedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmClearedEvent.to_json()

# convert the object into a dict
alarm_cleared_event_dict = alarm_cleared_event_instance.to_dict()
# create an instance of AlarmClearedEvent from a dict
alarm_cleared_event_form_dict = alarm_cleared_event.from_dict(alarm_cleared_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


