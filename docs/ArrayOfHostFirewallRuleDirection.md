# ArrayOfHostFirewallRuleDirection

A boxed array of *HostFirewallRuleDirection_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallRuleDirectionEnum]**](HostFirewallRuleDirectionEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_rule_direction import ArrayOfHostFirewallRuleDirection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallRuleDirection from a JSON string
array_of_host_firewall_rule_direction_instance = ArrayOfHostFirewallRuleDirection.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallRuleDirection.to_json()

# convert the object into a dict
array_of_host_firewall_rule_direction_dict = array_of_host_firewall_rule_direction_instance.to_dict()
# create an instance of ArrayOfHostFirewallRuleDirection from a dict
array_of_host_firewall_rule_direction_form_dict = array_of_host_firewall_rule_direction.from_dict(array_of_host_firewall_rule_direction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


