# TaskEvent

This event records the creation of a Task.  Note that the embedded TaskInfo object is a _snapshot_ of the Task state at the time of its creation, so its state will always be \"queued\". To find the current status of the task, query for the current state of the Task using the eventChainId in the embedded TaskInfo object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**TaskInfo**](TaskInfo.md) |  | 

## Example

```python
from vmware_vi.models.task_event import TaskEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TaskEvent from a JSON string
task_event_instance = TaskEvent.from_json(json)
# print the JSON string representation of the object
print TaskEvent.to_json()

# convert the object into a dict
task_event_dict = task_event_instance.to_dict()
# create an instance of TaskEvent from a dict
task_event_form_dict = task_event.from_dict(task_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


