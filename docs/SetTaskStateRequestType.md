# SetTaskStateRequestType

The parameters of *Task.SetTaskState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**TaskInfoStateEnum**](TaskInfoStateEnum.md) |  | 
**result** | [**Any**](Any.md) |  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.set_task_state_request_type import SetTaskStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetTaskStateRequestType from a JSON string
set_task_state_request_type_instance = SetTaskStateRequestType.from_json(json)
# print the JSON string representation of the object
print SetTaskStateRequestType.to_json()

# convert the object into a dict
set_task_state_request_type_dict = set_task_state_request_type_instance.to_dict()
# create an instance of SetTaskStateRequestType from a dict
set_task_state_request_type_form_dict = set_task_state_request_type.from_dict(set_task_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


