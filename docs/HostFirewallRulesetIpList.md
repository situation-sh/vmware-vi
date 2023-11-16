# HostFirewallRulesetIpList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **List[str]** | The list of ipAddresses.  All IPv4 addresses are specified as strings using dotted decimal format. For example, \&quot;192.0.20.10\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 5.0  | [optional] 
**ip_network** | [**List[HostFirewallRulesetIpNetwork]**](HostFirewallRulesetIpNetwork.md) | The list of networks  ***Since:*** vSphere API 5.0  | [optional] 
**all_ip** | **bool** | Flag indicating whether the ruleset works for all ip addresses.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_firewall_ruleset_ip_list import HostFirewallRulesetIpList

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRulesetIpList from a JSON string
host_firewall_ruleset_ip_list_instance = HostFirewallRulesetIpList.from_json(json)
# print the JSON string representation of the object
print HostFirewallRulesetIpList.to_json()

# convert the object into a dict
host_firewall_ruleset_ip_list_dict = host_firewall_ruleset_ip_list_instance.to_dict()
# create an instance of HostFirewallRulesetIpList from a dict
host_firewall_ruleset_ip_list_form_dict = host_firewall_ruleset_ip_list.from_dict(host_firewall_ruleset_ip_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


