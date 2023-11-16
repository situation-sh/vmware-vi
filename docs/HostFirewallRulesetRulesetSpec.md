# HostFirewallRulesetRulesetSpec

The ruleset update specification.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_hosts** | [**HostFirewallRulesetIpList**](HostFirewallRulesetIpList.md) |  | 

## Example

```python
from vmware_vi.models.host_firewall_ruleset_ruleset_spec import HostFirewallRulesetRulesetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRulesetRulesetSpec from a JSON string
host_firewall_ruleset_ruleset_spec_instance = HostFirewallRulesetRulesetSpec.from_json(json)
# print the JSON string representation of the object
print HostFirewallRulesetRulesetSpec.to_json()

# convert the object into a dict
host_firewall_ruleset_ruleset_spec_dict = host_firewall_ruleset_ruleset_spec_instance.to_dict()
# create an instance of HostFirewallRulesetRulesetSpec from a dict
host_firewall_ruleset_ruleset_spec_form_dict = host_firewall_ruleset_ruleset_spec.from_dict(host_firewall_ruleset_ruleset_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


