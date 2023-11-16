# ArrayOfHostFirewallRuleset

A boxed array of *HostFirewallRuleset*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallRuleset]**](HostFirewallRuleset.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_ruleset import ArrayOfHostFirewallRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallRuleset from a JSON string
array_of_host_firewall_ruleset_instance = ArrayOfHostFirewallRuleset.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallRuleset.to_json()

# convert the object into a dict
array_of_host_firewall_ruleset_dict = array_of_host_firewall_ruleset_instance.to_dict()
# create an instance of ArrayOfHostFirewallRuleset from a dict
array_of_host_firewall_ruleset_form_dict = array_of_host_firewall_ruleset.from_dict(array_of_host_firewall_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


