# ReconfigureScheduledTaskRequestType

The parameters of *ScheduledTask.ReconfigureScheduledTask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**ScheduledTaskSpec**](ScheduledTaskSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_scheduled_task_request_type import ReconfigureScheduledTaskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureScheduledTaskRequestType from a JSON string
reconfigure_scheduled_task_request_type_instance = ReconfigureScheduledTaskRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureScheduledTaskRequestType.to_json()

# convert the object into a dict
reconfigure_scheduled_task_request_type_dict = reconfigure_scheduled_task_request_type_instance.to_dict()
# create an instance of ReconfigureScheduledTaskRequestType from a dict
reconfigure_scheduled_task_request_type_form_dict = reconfigure_scheduled_task_request_type.from_dict(reconfigure_scheduled_task_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


