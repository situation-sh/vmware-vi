# ArrayOfAlarmSetting

A boxed array of *AlarmSetting*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmSetting]**](AlarmSetting.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_setting import ArrayOfAlarmSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmSetting from a JSON string
array_of_alarm_setting_instance = ArrayOfAlarmSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmSetting.to_json()

# convert the object into a dict
array_of_alarm_setting_dict = array_of_alarm_setting_instance.to_dict()
# create an instance of ArrayOfAlarmSetting from a dict
array_of_alarm_setting_form_dict = array_of_alarm_setting.from_dict(array_of_alarm_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


