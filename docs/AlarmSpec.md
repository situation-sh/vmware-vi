# AlarmSpec

Parameters for alarm creation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the alarm.  | 
**system_name** | **str** | System name of the alarm.  This is set only for predefined Alarms - i.e. Alarms created by the server or extensions automatically. After creation this value cannot be modified. User-created Alarms do not have a systemName at all.  The purpose of this field is to identify system-created Alarms reliably, even if they are edited by users.  When creating Alarms with systemName, the systemName and the name of the alarm should be equal.  When reconfiguring an Alarm with systemName, the same systemName should be passed in the new AlarmSpec. Renaming Alarms with systemName is not allowed, i.e. when reconfiguring, the name passed in the new AlarmSpec should be equal to either the systemName or its localized version (the current name in the Alarm&#39;s info).  ***Since:*** vSphere API 5.0  | [optional] 
**description** | **str** | Description of the alarm.  | 
**enabled** | **bool** | Flag to indicate whether or not the alarm is enabled or disabled.  | 
**expression** | [**AlarmExpression**](AlarmExpression.md) |  | 
**action** | [**AlarmAction**](AlarmAction.md) |  | [optional] 
**action_frequency** | **int** | Frequency in seconds, which specifies how often appropriate actions should repeat when an alarm does not change state.  ***Since:*** vSphere API 4.0  | [optional] 
**setting** | [**AlarmSetting**](AlarmSetting.md) |  | [optional] 

## Example

```python
from vmware_vi.models.alarm_spec import AlarmSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmSpec from a JSON string
alarm_spec_instance = AlarmSpec.from_json(json)
# print the JSON string representation of the object
print AlarmSpec.to_json()

# convert the object into a dict
alarm_spec_dict = alarm_spec_instance.to_dict()
# create an instance of AlarmSpec from a dict
alarm_spec_form_dict = alarm_spec.from_dict(alarm_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


