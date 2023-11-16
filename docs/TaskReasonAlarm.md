# TaskReasonAlarm

Indicates that the task was queued by an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm_name** | **str** | The name of the alarm that queued the task, retained in the history collector database.  | 
**alarm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity_name** | **str** | The name of the managed entity on which the alarm is triggered, retained in the history collector database.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.task_reason_alarm import TaskReasonAlarm

# TODO update the JSON string below
json = "{}"
# create an instance of TaskReasonAlarm from a JSON string
task_reason_alarm_instance = TaskReasonAlarm.from_json(json)
# print the JSON string representation of the object
print TaskReasonAlarm.to_json()

# convert the object into a dict
task_reason_alarm_dict = task_reason_alarm_instance.to_dict()
# create an instance of TaskReasonAlarm from a dict
task_reason_alarm_form_dict = task_reason_alarm.from_dict(task_reason_alarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


