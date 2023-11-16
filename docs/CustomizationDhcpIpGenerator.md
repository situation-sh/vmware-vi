# CustomizationDhcpIpGenerator

Use a DHCP server to configure the virtual network adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_dhcp_ip_generator import CustomizationDhcpIpGenerator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationDhcpIpGenerator from a JSON string
customization_dhcp_ip_generator_instance = CustomizationDhcpIpGenerator.from_json(json)
# print the JSON string representation of the object
print CustomizationDhcpIpGenerator.to_json()

# convert the object into a dict
customization_dhcp_ip_generator_dict = customization_dhcp_ip_generator_instance.to_dict()
# create an instance of CustomizationDhcpIpGenerator from a dict
customization_dhcp_ip_generator_form_dict = customization_dhcp_ip_generator.from_dict(customization_dhcp_ip_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


