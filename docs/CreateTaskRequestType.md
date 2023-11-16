# CreateTaskRequestType

The parameters of *TaskManager.CreateTask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**task_type_id** | **str** | Extension registered task type identifier for type of task being created  | 
**initiated_by** | **str** | The name of the user on whose behalf the Extension is creating the task  | [optional] 
**cancelable** | **bool** | True if the task should be cancelable, false otherwise  | 
**parent_task_key** | **str** | Key of the task that is the parent of this task  | [optional] 
**activation_id** | **str** | Activation Id is a client-provided token to link an API call with a task. When provided, the activationId is added to the *TaskInfo*  | [optional] 

## Example

```python
from vmware_vi.models.create_task_request_type import CreateTaskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskRequestType from a JSON string
create_task_request_type_instance = CreateTaskRequestType.from_json(json)
# print the JSON string representation of the object
print CreateTaskRequestType.to_json()

# convert the object into a dict
create_task_request_type_dict = create_task_request_type_instance.to_dict()
# create an instance of CreateTaskRequestType from a dict
create_task_request_type_form_dict = create_task_request_type.from_dict(create_task_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


