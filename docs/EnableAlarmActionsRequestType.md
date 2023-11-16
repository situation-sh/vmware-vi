# EnableAlarmActionsRequestType

The parameters of *AlarmManager.EnableAlarmActions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**enabled** | **bool** | true, if alarms are enabled during the schedule.  | 

## Example

```python
from vmware_vi.models.enable_alarm_actions_request_type import EnableAlarmActionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableAlarmActionsRequestType from a JSON string
enable_alarm_actions_request_type_instance = EnableAlarmActionsRequestType.from_json(json)
# print the JSON string representation of the object
print EnableAlarmActionsRequestType.to_json()

# convert the object into a dict
enable_alarm_actions_request_type_dict = enable_alarm_actions_request_type_instance.to_dict()
# create an instance of EnableAlarmActionsRequestType from a dict
enable_alarm_actions_request_type_form_dict = enable_alarm_actions_request_type.from_dict(enable_alarm_actions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


