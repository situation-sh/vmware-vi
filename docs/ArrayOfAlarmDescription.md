# ArrayOfAlarmDescription

A boxed array of *AlarmDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmDescription]**](AlarmDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_description import ArrayOfAlarmDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmDescription from a JSON string
array_of_alarm_description_instance = ArrayOfAlarmDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmDescription.to_json()

# convert the object into a dict
array_of_alarm_description_dict = array_of_alarm_description_instance.to_dict()
# create an instance of ArrayOfAlarmDescription from a dict
array_of_alarm_description_form_dict = array_of_alarm_description.from_dict(array_of_alarm_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


