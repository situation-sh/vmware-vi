# HostFirewallRuleDirection

A boxed *HostFirewallRuleDirection_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostFirewallRuleDirectionEnum**](HostFirewallRuleDirectionEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_firewall_rule_direction import HostFirewallRuleDirection

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRuleDirection from a JSON string
host_firewall_rule_direction_instance = HostFirewallRuleDirection.from_json(json)
# print the JSON string representation of the object
print HostFirewallRuleDirection.to_json()

# convert the object into a dict
host_firewall_rule_direction_dict = host_firewall_rule_direction_instance.to_dict()
# create an instance of HostFirewallRuleDirection from a dict
host_firewall_rule_direction_form_dict = host_firewall_rule_direction.from_dict(host_firewall_rule_direction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


