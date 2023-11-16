# HostFirewallRulePortType

A boxed *HostFirewallRulePortType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostFirewallRulePortTypeEnum**](HostFirewallRulePortTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_firewall_rule_port_type import HostFirewallRulePortType

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRulePortType from a JSON string
host_firewall_rule_port_type_instance = HostFirewallRulePortType.from_json(json)
# print the JSON string representation of the object
print HostFirewallRulePortType.to_json()

# convert the object into a dict
host_firewall_rule_port_type_dict = host_firewall_rule_port_type_instance.to_dict()
# create an instance of HostFirewallRulePortType from a dict
host_firewall_rule_port_type_form_dict = host_firewall_rule_port_type.from_dict(host_firewall_rule_port_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


