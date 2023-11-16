# HostFirewallConfigRuleSetConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_id** | **str** | Id of the ruleset.  ***Since:*** vSphere API 4.0  | 
**enabled** | **bool** | Flag indicating if the specified ruleset should be enabled.  ***Since:*** vSphere API 4.0  | 
**allowed_hosts** | [**HostFirewallRulesetIpList**](HostFirewallRulesetIpList.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_firewall_config_rule_set_config import HostFirewallConfigRuleSetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallConfigRuleSetConfig from a JSON string
host_firewall_config_rule_set_config_instance = HostFirewallConfigRuleSetConfig.from_json(json)
# print the JSON string representation of the object
print HostFirewallConfigRuleSetConfig.to_json()

# convert the object into a dict
host_firewall_config_rule_set_config_dict = host_firewall_config_rule_set_config_instance.to_dict()
# create an instance of HostFirewallConfigRuleSetConfig from a dict
host_firewall_config_rule_set_config_form_dict = host_firewall_config_rule_set_config.from_dict(host_firewall_config_rule_set_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


