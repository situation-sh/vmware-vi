# AlarmState

Information about the alarm's state. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique key that identifies the alarm.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**time** | **datetime** | Time the alarm triggered.  | 
**acknowledged** | **bool** | Flag to indicate if the alarm&#39;s actions have been acknowledged for the associated ManagedEntity.  ***Since:*** vSphere API 4.0  | [optional] 
**acknowledged_by_user** | **str** | The user who acknowledged this triggering.  If the triggering has not been acknowledged, then the value is not valid.  ***Since:*** vSphere API 4.0  | [optional] 
**acknowledged_time** | **datetime** | The time this triggering was acknowledged.  If the triggering has not been acknowledged, then the value is not valid.  ***Since:*** vSphere API 4.0  | [optional] 
**event_key** | **int** | Contains the key of the event that has triggered the alarm.  The value is set only for event based alarms. The value is not set for gray or manually reset alarms (via vim.AlarmManager.setAlarmStatus).  ***Since:*** vSphere API 6.0  | [optional] 
**disabled** | **bool** | Flag to indicate if the alarm is disabled for the associated ManagedEntity.  ***Since:*** vSphere API 6.9.1  | [optional] 

## Example

```python
from vmware_vi.models.alarm_state import AlarmState

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmState from a JSON string
alarm_state_instance = AlarmState.from_json(json)
# print the JSON string representation of the object
print AlarmState.to_json()

# convert the object into a dict
alarm_state_dict = alarm_state_instance.to_dict()
# create an instance of AlarmState from a dict
alarm_state_form_dict = alarm_state.from_dict(alarm_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


