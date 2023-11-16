# ArrayOfVmwareUplinkPortTeamingPolicy

A boxed array of *VmwareUplinkPortTeamingPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmwareUplinkPortTeamingPolicy]**](VmwareUplinkPortTeamingPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmware_uplink_port_teaming_policy import ArrayOfVmwareUplinkPortTeamingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmwareUplinkPortTeamingPolicy from a JSON string
array_of_vmware_uplink_port_teaming_policy_instance = ArrayOfVmwareUplinkPortTeamingPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmwareUplinkPortTeamingPolicy.to_json()

# convert the object into a dict
array_of_vmware_uplink_port_teaming_policy_dict = array_of_vmware_uplink_port_teaming_policy_instance.to_dict()
# create an instance of ArrayOfVmwareUplinkPortTeamingPolicy from a dict
array_of_vmware_uplink_port_teaming_policy_form_dict = array_of_vmware_uplink_port_teaming_policy.from_dict(array_of_vmware_uplink_port_teaming_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


