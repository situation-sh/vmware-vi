# HostFirewallRulesetIpNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The IPv4 or IPv6 network.  All IPv4 subnet addresses are specified as strings using dotted decimal format. For example, \&quot;192.0.20.0\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 5.0  | 
**prefix_length** | **int** | The prefix length for the network.  For example the prefix length for a network 10.20.120/22 is 22  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_firewall_ruleset_ip_network import HostFirewallRulesetIpNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallRulesetIpNetwork from a JSON string
host_firewall_ruleset_ip_network_instance = HostFirewallRulesetIpNetwork.from_json(json)
# print the JSON string representation of the object
print HostFirewallRulesetIpNetwork.to_json()

# convert the object into a dict
host_firewall_ruleset_ip_network_dict = host_firewall_ruleset_ip_network_instance.to_dict()
# create an instance of HostFirewallRulesetIpNetwork from a dict
host_firewall_ruleset_ip_network_form_dict = host_firewall_ruleset_ip_network.from_dict(host_firewall_ruleset_ip_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


