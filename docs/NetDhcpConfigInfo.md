# NetDhcpConfigInfo

Dynamic Host Configuration Protocol reporting for IP version 4 and version 6.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6** | [**NetDhcpConfigInfoDhcpOptions**](NetDhcpConfigInfoDhcpOptions.md) |  | [optional] 
**ipv4** | [**NetDhcpConfigInfoDhcpOptions**](NetDhcpConfigInfoDhcpOptions.md) |  | [optional] 

## Example

```python
from vmware_vi.models.net_dhcp_config_info import NetDhcpConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetDhcpConfigInfo from a JSON string
net_dhcp_config_info_instance = NetDhcpConfigInfo.from_json(json)
# print the JSON string representation of the object
print NetDhcpConfigInfo.to_json()

# convert the object into a dict
net_dhcp_config_info_dict = net_dhcp_config_info_instance.to_dict()
# create an instance of NetDhcpConfigInfo from a dict
net_dhcp_config_info_form_dict = net_dhcp_config_info.from_dict(net_dhcp_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


