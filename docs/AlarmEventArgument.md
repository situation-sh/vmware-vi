# AlarmEventArgument

The event argument is an Alarm object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.alarm_event_argument import AlarmEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEventArgument from a JSON string
alarm_event_argument_instance = AlarmEventArgument.from_json(json)
# print the JSON string representation of the object
print AlarmEventArgument.to_json()

# convert the object into a dict
alarm_event_argument_dict = alarm_event_argument_instance.to_dict()
# create an instance of AlarmEventArgument from a dict
alarm_event_argument_form_dict = alarm_event_argument.from_dict(alarm_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


