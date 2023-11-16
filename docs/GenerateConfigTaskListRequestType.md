# GenerateConfigTaskListRequestType

The parameters of *HostProfileManager.GenerateConfigTaskList*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**HostConfigSpec**](HostConfigSpec.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.generate_config_task_list_request_type import GenerateConfigTaskListRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateConfigTaskListRequestType from a JSON string
generate_config_task_list_request_type_instance = GenerateConfigTaskListRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateConfigTaskListRequestType.to_json()

# convert the object into a dict
generate_config_task_list_request_type_dict = generate_config_task_list_request_type_instance.to_dict()
# create an instance of GenerateConfigTaskListRequestType from a dict
generate_config_task_list_request_type_form_dict = generate_config_task_list_request_type.from_dict(generate_config_task_list_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


