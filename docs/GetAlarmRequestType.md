# GetAlarmRequestType

The parameters of *AlarmManager.GetAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.get_alarm_request_type import GetAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlarmRequestType from a JSON string
get_alarm_request_type_instance = GetAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print GetAlarmRequestType.to_json()

# convert the object into a dict
get_alarm_request_type_dict = get_alarm_request_type_instance.to_dict()
# create an instance of GetAlarmRequestType from a dict
get_alarm_request_type_form_dict = get_alarm_request_type.from_dict(get_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


