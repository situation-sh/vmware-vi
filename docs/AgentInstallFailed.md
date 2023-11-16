# AgentInstallFailed

An AgentInstallFailed fault is thrown when VirtualCenter fails to install the VirtualCenter agent on a host.  For example, a fault is thrown if the agent software cannot be uploaded to the host or an error occurred during the agent installation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the agent install failed, if known.  Values should come from *AgentInstallFailedReason_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**status_code** | **int** | The status code returned by the agent installer, if it was run.  ***Since:*** vSphere API 4.0  | [optional] 
**installer_output** | **str** | The output (stdout/stderr) from executing the agent installer.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.agent_install_failed import AgentInstallFailed

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInstallFailed from a JSON string
agent_install_failed_instance = AgentInstallFailed.from_json(json)
# print the JSON string representation of the object
print AgentInstallFailed.to_json()

# convert the object into a dict
agent_install_failed_dict = agent_install_failed_instance.to_dict()
# create an instance of AgentInstallFailed from a dict
agent_install_failed_form_dict = agent_install_failed.from_dict(agent_install_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


