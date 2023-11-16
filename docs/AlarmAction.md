# AlarmAction

Action invoked by triggered alarm.  This is an abstract type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.alarm_action import AlarmAction

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmAction from a JSON string
alarm_action_instance = AlarmAction.from_json(json)
# print the JSON string representation of the object
print AlarmAction.to_json()

# convert the object into a dict
alarm_action_dict = alarm_action_instance.to_dict()
# create an instance of AlarmAction from a dict
alarm_action_form_dict = alarm_action.from_dict(alarm_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


