# ArrayOfHostFirewallDefaultPolicy

A boxed array of *HostFirewallDefaultPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallDefaultPolicy]**](HostFirewallDefaultPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_default_policy import ArrayOfHostFirewallDefaultPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallDefaultPolicy from a JSON string
array_of_host_firewall_default_policy_instance = ArrayOfHostFirewallDefaultPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallDefaultPolicy.to_json()

# convert the object into a dict
array_of_host_firewall_default_policy_dict = array_of_host_firewall_default_policy_instance.to_dict()
# create an instance of ArrayOfHostFirewallDefaultPolicy from a dict
array_of_host_firewall_default_policy_form_dict = array_of_host_firewall_default_policy.from_dict(array_of_host_firewall_default_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


