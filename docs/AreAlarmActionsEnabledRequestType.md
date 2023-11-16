# AreAlarmActionsEnabledRequestType

The parameters of *AlarmManager.AreAlarmActionsEnabled*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.are_alarm_actions_enabled_request_type import AreAlarmActionsEnabledRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AreAlarmActionsEnabledRequestType from a JSON string
are_alarm_actions_enabled_request_type_instance = AreAlarmActionsEnabledRequestType.from_json(json)
# print the JSON string representation of the object
print AreAlarmActionsEnabledRequestType.to_json()

# convert the object into a dict
are_alarm_actions_enabled_request_type_dict = are_alarm_actions_enabled_request_type_instance.to_dict()
# create an instance of AreAlarmActionsEnabledRequestType from a dict
are_alarm_actions_enabled_request_type_form_dict = are_alarm_actions_enabled_request_type.from_dict(are_alarm_actions_enabled_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


