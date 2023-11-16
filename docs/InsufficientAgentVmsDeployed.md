# InsufficientAgentVmsDeployed

This fault is returned when the required number of deployed agent virtual machines is not currently deployed on a host and hence the host cannot be used to run client virtual machines.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** |  | 
**required_num_agent_vms** | **int** | The number of agent virtual machines required to be deployed on the host.  ***Since:*** vSphere API 5.0  | 
**current_num_agent_vms** | **int** | The number of agent virtual machines currently deployed on the host.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.insufficient_agent_vms_deployed import InsufficientAgentVmsDeployed

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientAgentVmsDeployed from a JSON string
insufficient_agent_vms_deployed_instance = InsufficientAgentVmsDeployed.from_json(json)
# print the JSON string representation of the object
print InsufficientAgentVmsDeployed.to_json()

# convert the object into a dict
insufficient_agent_vms_deployed_dict = insufficient_agent_vms_deployed_instance.to_dict()
# create an instance of InsufficientAgentVmsDeployed from a dict
insufficient_agent_vms_deployed_form_dict = insufficient_agent_vms_deployed.from_dict(insufficient_agent_vms_deployed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


