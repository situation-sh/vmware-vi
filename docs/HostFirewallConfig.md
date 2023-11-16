# HostFirewallConfig

DataObject used for firewall configuration  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**List[HostFirewallConfigRuleSetConfig]**](HostFirewallConfigRuleSetConfig.md) | Rules determining firewall settings.  ***Since:*** vSphere API 4.0  | [optional] 
**default_blocking_policy** | [**HostFirewallDefaultPolicy**](HostFirewallDefaultPolicy.md) |  | 

## Example

```python
from vmware_vi.models.host_firewall_config import HostFirewallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostFirewallConfig from a JSON string
host_firewall_config_instance = HostFirewallConfig.from_json(json)
# print the JSON string representation of the object
print HostFirewallConfig.to_json()

# convert the object into a dict
host_firewall_config_dict = host_firewall_config_instance.to_dict()
# create an instance of HostFirewallConfig from a dict
host_firewall_config_form_dict = host_firewall_config.from_dict(host_firewall_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


