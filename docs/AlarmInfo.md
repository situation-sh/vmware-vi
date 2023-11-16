# AlarmInfo

Attributes of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique key.  | 
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**last_modified_time** | **datetime** | The time the alarm was created or modified.  | 
**last_modified_user** | **str** | User name that modified the alarm most recently.  | 
**creation_event_id** | **int** | The event ID that records the alarm creation.  | 

## Example

```python
from vmware_vi.models.alarm_info import AlarmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmInfo from a JSON string
alarm_info_instance = AlarmInfo.from_json(json)
# print the JSON string representation of the object
print AlarmInfo.to_json()

# convert the object into a dict
alarm_info_dict = alarm_info_instance.to_dict()
# create an instance of AlarmInfo from a dict
alarm_info_form_dict = alarm_info.from_dict(alarm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


