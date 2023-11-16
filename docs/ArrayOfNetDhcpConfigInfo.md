# ArrayOfNetDhcpConfigInfo

A boxed array of *NetDhcpConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetDhcpConfigInfo]**](NetDhcpConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_dhcp_config_info import ArrayOfNetDhcpConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetDhcpConfigInfo from a JSON string
array_of_net_dhcp_config_info_instance = ArrayOfNetDhcpConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetDhcpConfigInfo.to_json()

# convert the object into a dict
array_of_net_dhcp_config_info_dict = array_of_net_dhcp_config_info_instance.to_dict()
# create an instance of ArrayOfNetDhcpConfigInfo from a dict
array_of_net_dhcp_config_info_form_dict = array_of_net_dhcp_config_info.from_dict(array_of_net_dhcp_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


