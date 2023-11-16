# AcknowledgeAlarmRequestType

The parameters of *AlarmManager.AcknowledgeAlarm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.acknowledge_alarm_request_type import AcknowledgeAlarmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeAlarmRequestType from a JSON string
acknowledge_alarm_request_type_instance = AcknowledgeAlarmRequestType.from_json(json)
# print the JSON string representation of the object
print AcknowledgeAlarmRequestType.to_json()

# convert the object into a dict
acknowledge_alarm_request_type_dict = acknowledge_alarm_request_type_instance.to_dict()
# create an instance of AcknowledgeAlarmRequestType from a dict
acknowledge_alarm_request_type_form_dict = acknowledge_alarm_request_type.from_dict(acknowledge_alarm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


