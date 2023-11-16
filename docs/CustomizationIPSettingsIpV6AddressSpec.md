# CustomizationIPSettingsIpV6AddressSpec

IPv6 settings  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**List[CustomizationIpV6Generator]**](CustomizationIpV6Generator.md) | ipv6 address generators  ***Since:*** vSphere API 4.0  | 
**gateway** | **List[str]** | gateways  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.customization_ip_settings_ip_v6_address_spec import CustomizationIPSettingsIpV6AddressSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationIPSettingsIpV6AddressSpec from a JSON string
customization_ip_settings_ip_v6_address_spec_instance = CustomizationIPSettingsIpV6AddressSpec.from_json(json)
# print the JSON string representation of the object
print CustomizationIPSettingsIpV6AddressSpec.to_json()

# convert the object into a dict
customization_ip_settings_ip_v6_address_spec_dict = customization_ip_settings_ip_v6_address_spec_instance.to_dict()
# create an instance of CustomizationIPSettingsIpV6AddressSpec from a dict
customization_ip_settings_ip_v6_address_spec_form_dict = customization_ip_settings_ip_v6_address_spec.from_dict(customization_ip_settings_ip_v6_address_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


