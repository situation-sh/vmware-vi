# HostNicOrderPolicy

This data object type describes network adapter ordering policy for a network adapter team.  A physical network adapter can be in the active list, the standby list, or neither. It cannot be in both lists. For a virtual switch, the NicOrderPolicy property is never null when retrieved from the server. When creating a new virtual switch or updating an existing virtual switch, the NicOrderPolicy can be null, in which case the default NicOrderPolicy from the server will be used. For a portgroup, a null NicOrderPolicy property means the portgroup inherits the policy from its parent. Otherwise, the NicOrderPolicy property defined in the portgroup takes precedence. In all cases where the NicOrderPolicy property is set, an empty activeNic array means there are no active Ethernet adapters in the team. An empty standbyNic array means there are no standby Ethernet adapters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_nic** | **List[str]** | List of active network adapters used for load balancing.  | [optional] 
**standby_nic** | **List[str]** | Standby network adapters used for failover.  | [optional] 

## Example

```python
from vmware_vi.models.host_nic_order_policy import HostNicOrderPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostNicOrderPolicy from a JSON string
host_nic_order_policy_instance = HostNicOrderPolicy.from_json(json)
# print the JSON string representation of the object
print HostNicOrderPolicy.to_json()

# convert the object into a dict
host_nic_order_policy_dict = host_nic_order_policy_instance.to_dict()
# create an instance of HostNicOrderPolicy from a dict
host_nic_order_policy_form_dict = host_nic_order_policy.from_dict(host_nic_order_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


