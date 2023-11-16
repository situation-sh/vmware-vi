# ArrayOfTaskReasonUser

A boxed array of *TaskReasonUser*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskReasonUser]**](TaskReasonUser.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_reason_user import ArrayOfTaskReasonUser

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskReasonUser from a JSON string
array_of_task_reason_user_instance = ArrayOfTaskReasonUser.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskReasonUser.to_json()

# convert the object into a dict
array_of_task_reason_user_dict = array_of_task_reason_user_instance.to_dict()
# create an instance of ArrayOfTaskReasonUser from a dict
array_of_task_reason_user_form_dict = array_of_task_reason_user.from_dict(array_of_task_reason_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


