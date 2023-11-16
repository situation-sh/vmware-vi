# HostFirewallInfo

Data object describing the firewall configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_policy** | [**HostFirewallDefaultPolicy**](HostFirewallDefaultPolicy.md) |  | 
**ruleset** | [**List[HostFirewallRuleset]**](HostFirewallRuleset.md) | List of configured rulesets.  | [optional] 

## Example

```python
from vmware_vi.models.host_firewall_info import HostFirewallInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallInfo from a JSON string
host_firewall_info_instance = HostFirewallInfo.from_json(json)
# print the JSON string representation of the object
print HostFirewallInfo.to_json()

# convert the object into a dict
host_firewall_info_dict = host_firewall_info_instance.to_dict()
# create an instance of HostFirewallInfo from a dict
host_firewall_info_form_dict = host_firewall_info.from_dict(host_firewall_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


