# HostFirewallRuleset

Data object that describes a single network ruleset that can be allowed or blocked by the firewall using the *HostFirewallSystem* object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Brief identifier for the ruleset.  | 
**label** | **str** | Display label for the ruleset.  | 
**required** | **bool** | Flag indicating whether the ruleset is required and cannot be disabled.  | 
**rule** | [**List[HostFirewallRule]**](HostFirewallRule.md) | List of rules within the ruleset.  | 
**service** | **str** | Managed service (if any) that uses this ruleset.  Must be one of the services listed in *HostServiceInfo.service*.  | [optional] 
**enabled** | **bool** | Flag indicating whether the ruleset is enabled.  If the ruleset is enabled, all ports specified in the ruleset are opened by the firewall.  | 
**allowed_hosts** | [**HostFirewallRulesetIpList**](HostFirewallRulesetIpList.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_firewall_ruleset import HostFirewallRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRuleset from a JSON string
host_firewall_ruleset_instance = HostFirewallRuleset.from_json(json)
# print the JSON string representation of the object
print HostFirewallRuleset.to_json()

# convert the object into a dict
host_firewall_ruleset_dict = host_firewall_ruleset_instance.to_dict()
# create an instance of HostFirewallRuleset from a dict
host_firewall_ruleset_form_dict = host_firewall_ruleset.from_dict(host_firewall_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


