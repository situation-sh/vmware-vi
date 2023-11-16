# ArrayOfAlarmInfo

A boxed array of *AlarmInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmInfo]**](AlarmInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_info import ArrayOfAlarmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmInfo from a JSON string
array_of_alarm_info_instance = ArrayOfAlarmInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmInfo.to_json()

# convert the object into a dict
array_of_alarm_info_dict = array_of_alarm_info_instance.to_dict()
# create an instance of ArrayOfAlarmInfo from a dict
array_of_alarm_info_form_dict = array_of_alarm_info.from_dict(array_of_alarm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


