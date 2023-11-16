# HostEsxAgentHostManagerConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_vm_datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**agent_vm_network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_esx_agent_host_manager_config_info import HostEsxAgentHostManagerConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostEsxAgentHostManagerConfigInfo from a JSON string
host_esx_agent_host_manager_config_info_instance = HostEsxAgentHostManagerConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostEsxAgentHostManagerConfigInfo.to_json()

# convert the object into a dict
host_esx_agent_host_manager_config_info_dict = host_esx_agent_host_manager_config_info_instance.to_dict()
# create an instance of HostEsxAgentHostManagerConfigInfo from a dict
host_esx_agent_host_manager_config_info_form_dict = host_esx_agent_host_manager_config_info.from_dict(host_esx_agent_host_manager_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


