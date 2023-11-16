# ArrayOfHostFirewallRulePortType

A boxed array of *HostFirewallRulePortType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallRulePortTypeEnum]**](HostFirewallRulePortTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_rule_port_type import ArrayOfHostFirewallRulePortType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallRulePortType from a JSON string
array_of_host_firewall_rule_port_type_instance = ArrayOfHostFirewallRulePortType.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallRulePortType.to_json()

# convert the object into a dict
array_of_host_firewall_rule_port_type_dict = array_of_host_firewall_rule_port_type_instance.to_dict()
# create an instance of ArrayOfHostFirewallRulePortType from a dict
array_of_host_firewall_rule_port_type_form_dict = array_of_host_firewall_rule_port_type.from_dict(array_of_host_firewall_rule_port_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


