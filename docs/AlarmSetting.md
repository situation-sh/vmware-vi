# AlarmSetting

Tolerance and frequency limits of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tolerance_range** | **int** | Tolerance range for the metric triggers, measured in one hundredth percentage.  A zero value means that the alarm triggers whenever the metric value is above or below the specified value. A nonzero value means that the alarm triggers only after reaching a certain percentage above or below the nominal trigger value.  | 
**reporting_frequency** | **int** | How often the alarm is triggered, measured in seconds.  A zero value means that the alarm is allowed to trigger as often as possible. A nonzero value means that any subsequent triggers are suppressed for a period of seconds following a reported trigger.  | 

## Example

```python
from vmware_vi.models.alarm_setting import AlarmSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmSetting from a JSON string
alarm_setting_instance = AlarmSetting.from_json(json)
# print the JSON string representation of the object
print AlarmSetting.to_json()

# convert the object into a dict
alarm_setting_dict = alarm_setting_instance.to_dict()
# create an instance of AlarmSetting from a dict
alarm_setting_form_dict = alarm_setting.from_dict(alarm_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


