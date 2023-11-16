# SetTaskDescriptionRequestType

The parameters of *Task.SetTaskDescription*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.set_task_description_request_type import SetTaskDescriptionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetTaskDescriptionRequestType from a JSON string
set_task_description_request_type_instance = SetTaskDescriptionRequestType.from_json(json)
# print the JSON string representation of the object
print SetTaskDescriptionRequestType.to_json()

# convert the object into a dict
set_task_description_request_type_dict = set_task_description_request_type_instance.to_dict()
# create an instance of SetTaskDescriptionRequestType from a dict
set_task_description_request_type_form_dict = set_task_description_request_type.from_dict(set_task_description_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


