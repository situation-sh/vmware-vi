# TaskReasonUser

Indicates that the task was queued by a specific user. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Name of the user that queued the task.  | 

## Example

```python
from vmware_vi.models.task_reason_user import TaskReasonUser

# TODO update the JSON string below
json = "{}"
# create an instance of TaskReasonUser from a JSON string
task_reason_user_instance = TaskReasonUser.from_json(json)
# print the JSON string representation of the object
print TaskReasonUser.to_json()

# convert the object into a dict
task_reason_user_dict = task_reason_user_instance.to_dict()
# create an instance of TaskReasonUser from a dict
task_reason_user_form_dict = task_reason_user.from_dict(task_reason_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


