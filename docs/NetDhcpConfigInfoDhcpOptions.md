# NetDhcpConfigInfoDhcpOptions

Provides for reporting of DHCP client.  This data object may be used at a per interface or per system scope.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Report state of dhcp client services.  ***Since:*** vSphere API 4.1  | 
**config** | [**List[KeyValue]**](KeyValue.md) | Platform specific settings for DHCP Client.  The key part is a unique number, the value part is the platform specific configuration command. For example on Linux, BSD systems using the file dhclient.conf output would be reported at system scope: key&#x3D;&#39;1&#39;, value&#x3D;&#39;timeout 60;&#39; key&#x3D;&#39;2&#39;, value&#x3D;&#39;reboot 10;&#39; output reported at per interface scope: key&#x3D;&#39;1&#39;, value&#x3D;&#39;prepend domain-name-servers 192.0.2.1;&#39; key&#x3D;&#39;2&#39;, value&#x3D;&#39;equire subnet-mask, domain-name-servers;&#39;  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_dhcp_config_info_dhcp_options import NetDhcpConfigInfoDhcpOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NetDhcpConfigInfoDhcpOptions from a JSON string
net_dhcp_config_info_dhcp_options_instance = NetDhcpConfigInfoDhcpOptions.from_json(json)
# print the JSON string representation of the object
print NetDhcpConfigInfoDhcpOptions.to_json()

# convert the object into a dict
net_dhcp_config_info_dhcp_options_dict = net_dhcp_config_info_dhcp_options_instance.to_dict()
# create an instance of NetDhcpConfigInfoDhcpOptions from a dict
net_dhcp_config_info_dhcp_options_form_dict = net_dhcp_config_info_dhcp_options.from_dict(net_dhcp_config_info_dhcp_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


