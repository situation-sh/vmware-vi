# EsxAgentHostManagerUpdateConfigRequestType

The parameters of *HostEsxAgentHostManager.EsxAgentHostManagerUpdateConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_info** | [**HostEsxAgentHostManagerConfigInfo**](HostEsxAgentHostManagerConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.esx_agent_host_manager_update_config_request_type import EsxAgentHostManagerUpdateConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EsxAgentHostManagerUpdateConfigRequestType from a JSON string
esx_agent_host_manager_update_config_request_type_instance = EsxAgentHostManagerUpdateConfigRequestType.from_json(json)
# print the JSON string representation of the object
print EsxAgentHostManagerUpdateConfigRequestType.to_json()

# convert the object into a dict
esx_agent_host_manager_update_config_request_type_dict = esx_agent_host_manager_update_config_request_type_instance.to_dict()
# create an instance of EsxAgentHostManagerUpdateConfigRequestType from a dict
esx_agent_host_manager_update_config_request_type_form_dict = esx_agent_host_manager_update_config_request_type.from_dict(esx_agent_host_manager_update_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


