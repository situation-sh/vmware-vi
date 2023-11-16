# ArrayOfNetDhcpConfigInfoDhcpOptions

A boxed array of *NetDhcpConfigInfoDhcpOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetDhcpConfigInfoDhcpOptions]**](NetDhcpConfigInfoDhcpOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_dhcp_config_info_dhcp_options import ArrayOfNetDhcpConfigInfoDhcpOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetDhcpConfigInfoDhcpOptions from a JSON string
array_of_net_dhcp_config_info_dhcp_options_instance = ArrayOfNetDhcpConfigInfoDhcpOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetDhcpConfigInfoDhcpOptions.to_json()

# convert the object into a dict
array_of_net_dhcp_config_info_dhcp_options_dict = array_of_net_dhcp_config_info_dhcp_options_instance.to_dict()
# create an instance of ArrayOfNetDhcpConfigInfoDhcpOptions from a dict
array_of_net_dhcp_config_info_dhcp_options_form_dict = array_of_net_dhcp_config_info_dhcp_options.from_dict(array_of_net_dhcp_config_info_dhcp_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


