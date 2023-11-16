# RetrieveEntityScheduledTaskRequestType

The parameters of *ScheduledTaskManager.RetrieveEntityScheduledTask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_entity_scheduled_task_request_type import RetrieveEntityScheduledTaskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityScheduledTaskRequestType from a JSON string
retrieve_entity_scheduled_task_request_type_instance = RetrieveEntityScheduledTaskRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveEntityScheduledTaskRequestType.to_json()

# convert the object into a dict
retrieve_entity_scheduled_task_request_type_dict = retrieve_entity_scheduled_task_request_type_instance.to_dict()
# create an instance of RetrieveEntityScheduledTaskRequestType from a dict
retrieve_entity_scheduled_task_request_type_form_dict = retrieve_entity_scheduled_task_request_type.from_dict(retrieve_entity_scheduled_task_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


