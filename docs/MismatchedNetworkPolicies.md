# MismatchedNetworkPolicies

Deprecated as of vSphere API 5.5, use *CannotUseNetwork* with a correct reason for the fault.  The virtual machine network uses different offload or security policies on the destination host than on the source host.  This is an error if the virtual machine is currently connected to the network, and a warning otherwise. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the interface device.  | 
**backing** | **str** | The name of the network.  | 
**connected** | **bool** | The connected/disconnected state of the device.  | 

## Example

```python
from vmware_vi.models.mismatched_network_policies import MismatchedNetworkPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of MismatchedNetworkPolicies from a JSON string
mismatched_network_policies_instance = MismatchedNetworkPolicies.from_json(json)
# print the JSON string representation of the object
print MismatchedNetworkPolicies.to_json()

# convert the object into a dict
mismatched_network_policies_dict = mismatched_network_policies_instance.to_dict()
# create an instance of MismatchedNetworkPolicies from a dict
mismatched_network_policies_form_dict = mismatched_network_policies.from_dict(mismatched_network_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


