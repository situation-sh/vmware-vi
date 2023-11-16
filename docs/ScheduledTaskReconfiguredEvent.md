# ScheduledTaskReconfiguredEvent

This event records the reconfiguration of a scheduled task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.scheduled_task_reconfigured_event import ScheduledTaskReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskReconfiguredEvent from a JSON string
scheduled_task_reconfigured_event_instance = ScheduledTaskReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskReconfiguredEvent.to_json()

# convert the object into a dict
scheduled_task_reconfigured_event_dict = scheduled_task_reconfigured_event_instance.to_dict()
# create an instance of ScheduledTaskReconfiguredEvent from a dict
scheduled_task_reconfigured_event_form_dict = scheduled_task_reconfigured_event.from_dict(scheduled_task_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


