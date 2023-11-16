# TaskTimeoutEvent

This event records when a task is cleaned up b/c of timeout  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.task_timeout_event import TaskTimeoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTimeoutEvent from a JSON string
task_timeout_event_instance = TaskTimeoutEvent.from_json(json)
# print the JSON string representation of the object
print TaskTimeoutEvent.to_json()

# convert the object into a dict
task_timeout_event_dict = task_timeout_event_instance.to_dict()
# create an instance of TaskTimeoutEvent from a dict
task_timeout_event_form_dict = task_timeout_event.from_dict(task_timeout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


