# HostNetworkPolicy

This data object type describes network policies that can be configured for both virtual switches and port groups.  The policy settings on the port group can inherit policy settings from their containing virtual switch. These policy settings are inherited if the settings on the port group are not set. Since every policy setting on a port group is optional, every individual policy setting can be inherited.  By contrast, if a host is capable of implementing a policy setting, every virtual switch has some value assigned to the policy setting. In this case, although all of the policy settings are optional, they always have some value either by inheritance or by direct setting.  Policy settings are organized into policy groups such as SecurityPolicy. Policy groups are optional since it is possible that a host may not implement such policies. If a host does not support a policy group, the policy group is not set on both the virtual switches and the port groups.  See also *HostNetCapabilities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security** | [**HostNetworkSecurityPolicy**](HostNetworkSecurityPolicy.md) |  | [optional] 
**nic_teaming** | [**HostNicTeamingPolicy**](HostNicTeamingPolicy.md) |  | [optional] 
**offload_policy** | [**HostNetOffloadCapabilities**](HostNetOffloadCapabilities.md) |  | [optional] 
**shaping_policy** | [**HostNetworkTrafficShapingPolicy**](HostNetworkTrafficShapingPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_network_policy import HostNetworkPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkPolicy from a JSON string
host_network_policy_instance = HostNetworkPolicy.from_json(json)
# print the JSON string representation of the object
print HostNetworkPolicy.to_json()

# convert the object into a dict
host_network_policy_dict = host_network_policy_instance.to_dict()
# create an instance of HostNetworkPolicy from a dict
host_network_policy_form_dict = host_network_policy.from_dict(host_network_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


