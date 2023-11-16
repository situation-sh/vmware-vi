# HostFirewallDefaultPolicy

Default settings for the firewall, used for ports that are not explicitly opened. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_blocked** | **bool** | Flag indicating whether incoming traffic should be blocked by default.  | [optional] 
**outgoing_blocked** | **bool** | Flag indicating whether outgoing traffic should be blocked by default.  | [optional] 

## Example

```python
from vmware_vi.models.host_firewall_default_policy import HostFirewallDefaultPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallDefaultPolicy from a JSON string
host_firewall_default_policy_instance = HostFirewallDefaultPolicy.from_json(json)
# print the JSON string representation of the object
print HostFirewallDefaultPolicy.to_json()

# convert the object into a dict
host_firewall_default_policy_dict = host_firewall_default_policy_instance.to_dict()
# create an instance of HostFirewallDefaultPolicy from a dict
host_firewall_default_policy_form_dict = host_firewall_default_policy.from_dict(host_firewall_default_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


