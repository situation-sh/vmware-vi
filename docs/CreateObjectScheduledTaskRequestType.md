# CreateObjectScheduledTaskRequestType

The parameters of *ScheduledTaskManager.CreateObjectScheduledTask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**ScheduledTaskSpec**](ScheduledTaskSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_object_scheduled_task_request_type import CreateObjectScheduledTaskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectScheduledTaskRequestType from a JSON string
create_object_scheduled_task_request_type_instance = CreateObjectScheduledTaskRequestType.from_json(json)
# print the JSON string representation of the object
print CreateObjectScheduledTaskRequestType.to_json()

# convert the object into a dict
create_object_scheduled_task_request_type_dict = create_object_scheduled_task_request_type_instance.to_dict()
# create an instance of CreateObjectScheduledTaskRequestType from a dict
create_object_scheduled_task_request_type_form_dict = create_object_scheduled_task_request_type.from_dict(create_object_scheduled_task_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


