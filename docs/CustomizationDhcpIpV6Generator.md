# CustomizationDhcpIpV6Generator

Use a DHCP server to configure ipv6 address  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_dhcp_ip_v6_generator import CustomizationDhcpIpV6Generator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationDhcpIpV6Generator from a JSON string
customization_dhcp_ip_v6_generator_instance = CustomizationDhcpIpV6Generator.from_json(json)
# print the JSON string representation of the object
print CustomizationDhcpIpV6Generator.to_json()

# convert the object into a dict
customization_dhcp_ip_v6_generator_dict = customization_dhcp_ip_v6_generator_instance.to_dict()
# create an instance of CustomizationDhcpIpV6Generator from a dict
customization_dhcp_ip_v6_generator_form_dict = customization_dhcp_ip_v6_generator.from_dict(customization_dhcp_ip_v6_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


