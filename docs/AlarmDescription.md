# AlarmDescription

Static strings for alarms. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expr** | [**List[TypeDescription]**](TypeDescription.md) | Descriptions of expression types for a trigger.  | 
**state_operator** | [**List[ElementDescription]**](ElementDescription.md) | *State Operator enum description*  | 
**metric_operator** | [**List[ElementDescription]**](ElementDescription.md) | *MetricAlarmExpression Metric Operator enum description*  | 
**host_system_connection_state** | [**List[ElementDescription]**](ElementDescription.md) | *Host System Connection State enum description*  | 
**virtual_machine_power_state** | [**List[ElementDescription]**](ElementDescription.md) | *Virtual Machine Power State enum description*  | 
**datastore_connection_state** | [**List[ElementDescription]**](ElementDescription.md) | *DatastoreSummary.accessible* and *description*  ***Since:*** vSphere API 4.0  | 
**host_system_power_state** | [**List[ElementDescription]**](ElementDescription.md) | *Host System Power State enum description*  ***Since:*** vSphere API 4.0  | 
**virtual_machine_guest_heartbeat_status** | [**List[ElementDescription]**](ElementDescription.md) | *Guest Heartbeat Status enum description*  ***Since:*** vSphere API 4.0  | 
**entity_status** | [**List[ElementDescription]**](ElementDescription.md) | *ManagedEntity Status enum description*  | 
**action** | [**List[TypeDescription]**](TypeDescription.md) | Action class descriptions for an alarm.  | 

## Example

```python
from vmware_vi.models.alarm_description import AlarmDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmDescription from a JSON string
alarm_description_instance = AlarmDescription.from_json(json)
# print the JSON string representation of the object
print AlarmDescription.to_json()

# convert the object into a dict
alarm_description_dict = alarm_description_instance.to_dict()
# create an instance of AlarmDescription from a dict
alarm_description_form_dict = alarm_description.from_dict(alarm_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


