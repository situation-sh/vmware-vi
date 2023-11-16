# HostNetworkSecurityPolicy

This data object type describes security policy governing ports. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_promiscuous** | **bool** | The flag to indicate whether or not all traffic is seen on the port.  | [optional] 
**mac_changes** | **bool** | The flag to indicate whether or not the Media Access Control (MAC) address can be changed.  | [optional] 
**forged_transmits** | **bool** | The flag to indicate whether or not the virtual network adapter should be allowed to send network traffic with a different MAC address than that of the virtual network adapter.  | [optional] 

## Example

```python
from vmware_vi.models.host_network_security_policy import HostNetworkSecurityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkSecurityPolicy from a JSON string
host_network_security_policy_instance = HostNetworkSecurityPolicy.from_json(json)
# print the JSON string representation of the object
print HostNetworkSecurityPolicy.to_json()

# convert the object into a dict
host_network_security_policy_dict = host_network_security_policy_instance.to_dict()
# create an instance of HostNetworkSecurityPolicy from a dict
host_network_security_policy_form_dict = host_network_security_policy.from_dict(host_network_security_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


