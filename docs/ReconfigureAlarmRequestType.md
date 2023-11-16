# ReconfigureAlarmRequestType

The parameters of *Alarm.ReconfigureAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**AlarmSpec**](AlarmSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_alarm_request_type import ReconfigureAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureAlarmRequestType from a JSON string
reconfigure_alarm_request_type_instance = ReconfigureAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureAlarmRequestType.to_json()

# convert the object into a dict
reconfigure_alarm_request_type_dict = reconfigure_alarm_request_type_instance.to_dict()
# create an instance of ReconfigureAlarmRequestType from a dict
reconfigure_alarm_request_type_form_dict = reconfigure_alarm_request_type.from_dict(reconfigure_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


