# RetrieveObjectScheduledTaskRequestType

The parameters of *ScheduledTaskManager.RetrieveObjectScheduledTask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_object_scheduled_task_request_type import RetrieveObjectScheduledTaskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveObjectScheduledTaskRequestType from a JSON string
retrieve_object_scheduled_task_request_type_instance = RetrieveObjectScheduledTaskRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveObjectScheduledTaskRequestType.to_json()

# convert the object into a dict
retrieve_object_scheduled_task_request_type_dict = retrieve_object_scheduled_task_request_type_instance.to_dict()
# create an instance of RetrieveObjectScheduledTaskRequestType from a dict
retrieve_object_scheduled_task_request_type_form_dict = retrieve_object_scheduled_task_request_type.from_dict(retrieve_object_scheduled_task_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


