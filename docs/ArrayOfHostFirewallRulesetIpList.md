# ArrayOfHostFirewallRulesetIpList

A boxed array of *HostFirewallRulesetIpList*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallRulesetIpList]**](HostFirewallRulesetIpList.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_ruleset_ip_list import ArrayOfHostFirewallRulesetIpList

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallRulesetIpList from a JSON string
array_of_host_firewall_ruleset_ip_list_instance = ArrayOfHostFirewallRulesetIpList.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallRulesetIpList.to_json()

# convert the object into a dict
array_of_host_firewall_ruleset_ip_list_dict = array_of_host_firewall_ruleset_ip_list_instance.to_dict()
# create an instance of ArrayOfHostFirewallRulesetIpList from a dict
array_of_host_firewall_ruleset_ip_list_form_dict = array_of_host_firewall_ruleset_ip_list.from_dict(array_of_host_firewall_ruleset_ip_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


