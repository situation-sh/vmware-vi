# NetDhcpConfigSpec

Dynamic Host Configuration Protocol Configuration for IP version 4 and version 6.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6** | [**NetDhcpConfigSpecDhcpOptionsSpec**](NetDhcpConfigSpecDhcpOptionsSpec.md) |  | [optional] 
**ipv4** | [**NetDhcpConfigSpecDhcpOptionsSpec**](NetDhcpConfigSpecDhcpOptionsSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.net_dhcp_config_spec import NetDhcpConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetDhcpConfigSpec from a JSON string
net_dhcp_config_spec_instance = NetDhcpConfigSpec.from_json(json)
# print the JSON string representation of the object
print NetDhcpConfigSpec.to_json()

# convert the object into a dict
net_dhcp_config_spec_dict = net_dhcp_config_spec_instance.to_dict()
# create an instance of NetDhcpConfigSpec from a dict
net_dhcp_config_spec_form_dict = net_dhcp_config_spec.from_dict(net_dhcp_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


