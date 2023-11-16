# ArrayOfHostNetworkSecurityPolicy

A boxed array of *HostNetworkSecurityPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkSecurityPolicy]**](HostNetworkSecurityPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_security_policy import ArrayOfHostNetworkSecurityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkSecurityPolicy from a JSON string
array_of_host_network_security_policy_instance = ArrayOfHostNetworkSecurityPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkSecurityPolicy.to_json()

# convert the object into a dict
array_of_host_network_security_policy_dict = array_of_host_network_security_policy_instance.to_dict()
# create an instance of ArrayOfHostNetworkSecurityPolicy from a dict
array_of_host_network_security_policy_form_dict = array_of_host_network_security_policy.from_dict(array_of_host_network_security_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


