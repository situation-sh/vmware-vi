# ArrayOfHostProfileManagerConfigTaskList

A boxed array of *HostProfileManagerConfigTaskList*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProfileManagerConfigTaskList]**](HostProfileManagerConfigTaskList.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_profile_manager_config_task_list import ArrayOfHostProfileManagerConfigTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProfileManagerConfigTaskList from a JSON string
array_of_host_profile_manager_config_task_list_instance = ArrayOfHostProfileManagerConfigTaskList.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProfileManagerConfigTaskList.to_json()

# convert the object into a dict
array_of_host_profile_manager_config_task_list_dict = array_of_host_profile_manager_config_task_list_instance.to_dict()
# create an instance of ArrayOfHostProfileManagerConfigTaskList from a dict
array_of_host_profile_manager_config_task_list_form_dict = array_of_host_profile_manager_config_task_list.from_dict(array_of_host_profile_manager_config_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


