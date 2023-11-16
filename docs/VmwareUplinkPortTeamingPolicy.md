# VmwareUplinkPortTeamingPolicy

Policy for a uplink port team.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**StringPolicy**](StringPolicy.md) |  | [optional] 
**reverse_policy** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**notify_switches** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**rolling_order** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**failure_criteria** | [**DVSFailureCriteria**](DVSFailureCriteria.md) |  | [optional] 
**uplink_port_order** | [**VMwareUplinkPortOrderPolicy**](VMwareUplinkPortOrderPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vmware_uplink_port_teaming_policy import VmwareUplinkPortTeamingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareUplinkPortTeamingPolicy from a JSON string
vmware_uplink_port_teaming_policy_instance = VmwareUplinkPortTeamingPolicy.from_json(json)
# print the JSON string representation of the object
print VmwareUplinkPortTeamingPolicy.to_json()

# convert the object into a dict
vmware_uplink_port_teaming_policy_dict = vmware_uplink_port_teaming_policy_instance.to_dict()
# create an instance of VmwareUplinkPortTeamingPolicy from a dict
vmware_uplink_port_teaming_policy_form_dict = vmware_uplink_port_teaming_policy.from_dict(vmware_uplink_port_teaming_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


