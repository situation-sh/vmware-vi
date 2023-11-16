# HostFirewallRule

This data object type describes a port (or range of ports), identified by port number(s), direction and protocol.  It is used as a convenient way for users to express what ports they want to permit through the firewall. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | The port number.  | 
**end_port** | **int** | For a port range, the ending port number.  | [optional] 
**direction** | [**HostFirewallRuleDirectionEnum**](HostFirewallRuleDirectionEnum.md) |  | 
**port_type** | [**HostFirewallRulePortTypeEnum**](HostFirewallRulePortTypeEnum.md) |  | [optional] 
**protocol** | **str** | The port protocol.  Valid values are defined by the *HostFirewallRuleProtocol_enum* enumeration.  | 

## Example

```python
from vmware_vi.models.host_firewall_rule import HostFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRule from a JSON string
host_firewall_rule_instance = HostFirewallRule.from_json(json)
# print the JSON string representation of the object
print HostFirewallRule.to_json()

# convert the object into a dict
host_firewall_rule_dict = host_firewall_rule_instance.to_dict()
# create an instance of HostFirewallRule from a dict
host_firewall_rule_form_dict = host_firewall_rule.from_dict(host_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


