# NetDhcpConfigSpecDhcpOptionsSpec

Provides for configuration of IPv6  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable or disable dhcp for IPv4.  ***Since:*** vSphere API 4.1  | [optional] 
**config** | [**List[KeyValue]**](KeyValue.md) | Platform specific settings for DHCP Client.  The key part is a unique number, the value part is the platform specific configuration command. See *NetDhcpConfigInfo* for value formatting.  ***Since:*** vSphere API 4.1  | 
**operation** | **str** | Requires one of the values from *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.net_dhcp_config_spec_dhcp_options_spec import NetDhcpConfigSpecDhcpOptionsSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetDhcpConfigSpecDhcpOptionsSpec from a JSON string
net_dhcp_config_spec_dhcp_options_spec_instance = NetDhcpConfigSpecDhcpOptionsSpec.from_json(json)
# print the JSON string representation of the object
print NetDhcpConfigSpecDhcpOptionsSpec.to_json()

# convert the object into a dict
net_dhcp_config_spec_dhcp_options_spec_dict = net_dhcp_config_spec_dhcp_options_spec_instance.to_dict()
# create an instance of NetDhcpConfigSpecDhcpOptionsSpec from a dict
net_dhcp_config_spec_dhcp_options_spec_form_dict = net_dhcp_config_spec_dhcp_options_spec.from_dict(net_dhcp_config_spec_dhcp_options_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


