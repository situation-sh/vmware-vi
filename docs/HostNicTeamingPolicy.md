# HostNicTeamingPolicy

Policy for a network adapter team. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | Network adapter teaming policy includes failover and load balancing, It can be one of the following: - **loadbalance\\_ip**: route based on ip hash. - **loadbalance\\_srcmac**: route based on source MAC hash. - **loadbalance\\_srcid**: route based on the source of the port ID. - **failover\\_explicit**: use explicit failover order.    See also *HostNetCapabilities.nicTeamingPolicy*.  | [optional] 
**reverse_policy** | **bool** | Deprecated as of VI API 5.1, the system default (true) will be used.  The flag to indicate whether or not the teaming policy is applied to inbound frames as well.  For example, if the policy is explicit failover, a broadcast request goes through uplink1 and comes back through uplink2. Then if the reverse policy is set, the frame is dropped when it is received from uplink2. This reverse policy is useful to prevent the virtual machine from getting reflections.  | [optional] 
**notify_switches** | **bool** | Flag to specify whether or not to notify the physical switch if a link fails.  If this property is true, ESX Server will respond to the failure by sending a RARP packet from a different physical adapter, causing the switch to update its cache.  | [optional] 
**rolling_order** | **bool** | The flag to indicate whether or not to use a rolling policy when restoring links.  For example, assume the explicit link order is (vmnic9, vmnic0), therefore vmnic9 goes down, vmnic0 comes up. However, when vmnic9 comes backup, if rollingOrder is set to be true, vmnic0 continues to be used, otherwise, vmnic9 is restored as specified in the explicitly order.  | [optional] 
**failure_criteria** | [**HostNicFailureCriteria**](HostNicFailureCriteria.md) |  | [optional] 
**nic_order** | [**HostNicOrderPolicy**](HostNicOrderPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_nic_teaming_policy import HostNicTeamingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostNicTeamingPolicy from a JSON string
host_nic_teaming_policy_instance = HostNicTeamingPolicy.from_json(json)
# print the JSON string representation of the object
print HostNicTeamingPolicy.to_json()

# convert the object into a dict
host_nic_teaming_policy_dict = host_nic_teaming_policy_instance.to_dict()
# create an instance of HostNicTeamingPolicy from a dict
host_nic_teaming_policy_form_dict = host_nic_teaming_policy.from_dict(host_nic_teaming_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


