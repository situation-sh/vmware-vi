# GenerateHostProfileTaskListRequestType

The parameters of *HostProfileManager.GenerateHostProfileTaskList_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**HostConfigSpec**](HostConfigSpec.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.generate_host_profile_task_list_request_type import GenerateHostProfileTaskListRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateHostProfileTaskListRequestType from a JSON string
generate_host_profile_task_list_request_type_instance = GenerateHostProfileTaskListRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateHostProfileTaskListRequestType.to_json()

# convert the object into a dict
generate_host_profile_task_list_request_type_dict = generate_host_profile_task_list_request_type_instance.to_dict()
# create an instance of GenerateHostProfileTaskListRequestType from a dict
generate_host_profile_task_list_request_type_form_dict = generate_host_profile_task_list_request_type.from_dict(generate_host_profile_task_list_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


