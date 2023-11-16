# AlarmReconfiguredEvent

This event records the reconfiguration of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.alarm_reconfigured_event import AlarmReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmReconfiguredEvent from a JSON string
alarm_reconfigured_event_instance = AlarmReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print AlarmReconfiguredEvent.to_json()

# convert the object into a dict
alarm_reconfigured_event_dict = alarm_reconfigured_event_instance.to_dict()
# create an instance of AlarmReconfiguredEvent from a dict
alarm_reconfigured_event_form_dict = alarm_reconfigured_event.from_dict(alarm_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


