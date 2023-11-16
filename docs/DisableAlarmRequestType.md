# DisableAlarmRequestType

The parameters of *AlarmManager.DisableAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.disable_alarm_request_type import DisableAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisableAlarmRequestType from a JSON string
disable_alarm_request_type_instance = DisableAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print DisableAlarmRequestType.to_json()

# convert the object into a dict
disable_alarm_request_type_dict = disable_alarm_request_type_instance.to_dict()
# create an instance of DisableAlarmRequestType from a dict
disable_alarm_request_type_form_dict = disable_alarm_request_type.from_dict(disable_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


