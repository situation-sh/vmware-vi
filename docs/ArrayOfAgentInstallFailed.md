# ArrayOfAgentInstallFailed

A boxed array of *AgentInstallFailed*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AgentInstallFailed]**](AgentInstallFailed.md) |  | 

## Example

```python
from vmware_vi.models.array_of_agent_install_failed import ArrayOfAgentInstallFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAgentInstallFailed from a JSON string
array_of_agent_install_failed_instance = ArrayOfAgentInstallFailed.from_json(json)
# print the JSON string representation of the object
print ArrayOfAgentInstallFailed.to_json()

# convert the object into a dict
array_of_agent_install_failed_dict = array_of_agent_install_failed_instance.to_dict()
# create an instance of ArrayOfAgentInstallFailed from a dict
array_of_agent_install_failed_form_dict = array_of_agent_install_failed.from_dict(array_of_agent_install_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


