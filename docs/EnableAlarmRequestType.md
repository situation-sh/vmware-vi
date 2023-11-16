# EnableAlarmRequestType

The parameters of *AlarmManager.EnableAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.enable_alarm_request_type import EnableAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableAlarmRequestType from a JSON string
enable_alarm_request_type_instance = EnableAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print EnableAlarmRequestType.to_json()

# convert the object into a dict
enable_alarm_request_type_dict = enable_alarm_request_type_instance.to_dict()
# create an instance of EnableAlarmRequestType from a dict
enable_alarm_request_type_form_dict = enable_alarm_request_type.from_dict(enable_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


