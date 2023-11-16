# HostProfileManagerConfigTaskList

The *HostProfileManagerConfigTaskList* data object represents a set of tasks to be performed on a host during host profile application.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**HostConfigSpec**](HostConfigSpec.md) |  | [optional] 
**task_description** | [**List[LocalizableMessage]**](LocalizableMessage.md) | Description of tasks that will be performed on the host to carry out HostProfile application.  ***Since:*** vSphere API 4.0  | [optional] 
**task_list_requirement** | **List[str]** | A set of requirements whose actions must be fulfilled before and/or after the task list is applied on an ESXi host, e.g.  whether the ESXi host must be in maintenance mode prior to applying the &lt;code&gt;configSpec&lt;/code&gt;, or whether the host will need to be rebooted after applying the &lt;code&gt;configSpec&lt;/code&gt;. See *HostProfileManagerTaskListRequirement_enum* for details of supported values.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_manager_config_task_list import HostProfileManagerConfigTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerConfigTaskList from a JSON string
host_profile_manager_config_task_list_instance = HostProfileManagerConfigTaskList.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerConfigTaskList.to_json()

# convert the object into a dict
host_profile_manager_config_task_list_dict = host_profile_manager_config_task_list_instance.to_dict()
# create an instance of HostProfileManagerConfigTaskList from a dict
host_profile_manager_config_task_list_form_dict = host_profile_manager_config_task_list.from_dict(host_profile_manager_config_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


