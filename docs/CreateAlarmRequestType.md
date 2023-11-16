# CreateAlarmRequestType

The parameters of *AlarmManager.CreateAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**AlarmSpec**](AlarmSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_alarm_request_type import CreateAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlarmRequestType from a JSON string
create_alarm_request_type_instance = CreateAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print CreateAlarmRequestType.to_json()

# convert the object into a dict
create_alarm_request_type_dict = create_alarm_request_type_instance.to_dict()
# create an instance of CreateAlarmRequestType from a dict
create_alarm_request_type_form_dict = create_alarm_request_type.from_dict(create_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


