# ArrayOfHostFirewallConfig

A boxed array of *HostFirewallConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallConfig]**](HostFirewallConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_config import ArrayOfHostFirewallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallConfig from a JSON string
array_of_host_firewall_config_instance = ArrayOfHostFirewallConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallConfig.to_json()

# convert the object into a dict
array_of_host_firewall_config_dict = array_of_host_firewall_config_instance.to_dict()
# create an instance of ArrayOfHostFirewallConfig from a dict
array_of_host_firewall_config_form_dict = array_of_host_firewall_config.from_dict(array_of_host_firewall_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


