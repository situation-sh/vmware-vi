# ClearTriggeredAlarmsRequestType

The parameters of *AlarmManager.ClearTriggeredAlarms*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AlarmFilterSpec**](AlarmFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.clear_triggered_alarms_request_type import ClearTriggeredAlarmsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ClearTriggeredAlarmsRequestType from a JSON string
clear_triggered_alarms_request_type_instance = ClearTriggeredAlarmsRequestType.from_json(json)
# print the JSON string representation of the object
print ClearTriggeredAlarmsRequestType.to_json()

# convert the object into a dict
clear_triggered_alarms_request_type_dict = clear_triggered_alarms_request_type_instance.to_dict()
# create an instance of ClearTriggeredAlarmsRequestType from a dict
clear_triggered_alarms_request_type_form_dict = clear_triggered_alarms_request_type.from_dict(clear_triggered_alarms_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


