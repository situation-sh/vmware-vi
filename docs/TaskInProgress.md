# TaskInProgress

The TaskInProgress data object type represents a fault when an operation tries to access an entity that already has another (long) operation in progress. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.task_in_progress import TaskInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInProgress from a JSON string
task_in_progress_instance = TaskInProgress.from_json(json)
# print the JSON string representation of the object
print TaskInProgress.to_json()

# convert the object into a dict
task_in_progress_dict = task_in_progress_instance.to_dict()
# create an instance of TaskInProgress from a dict
task_in_progress_form_dict = task_in_progress.from_dict(task_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


