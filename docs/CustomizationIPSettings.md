# CustomizationIPSettings

IP settings for a virtual network adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**CustomizationIpGenerator**](CustomizationIpGenerator.md) |  | 
**subnet_mask** | **str** | Subnet mask for this virtual network adapter.  | [optional] 
**gateway** | **List[str]** | For a virtual network adapter with a static IP address, this data object type contains a list of gateways, in order of preference.  | [optional] 
**ip_v6_spec** | [**CustomizationIPSettingsIpV6AddressSpec**](CustomizationIPSettingsIpV6AddressSpec.md) |  | [optional] 
**dns_server_list** | **List[str]** | A list of server IP addresses to use for DNS lookup in a Windows guest operating system.  In Windows, these settings are adapter-specific, whereas in Linux, they are global. As a result, the Linux guest customization process ignores this setting and looks for its DNS servers in the globalIPSettings object.  Specify these servers in order of preference. If this list is not empty, and if a DHCP IpGenerator is used, then these settings override the DHCP settings.  | [optional] 
**dns_domain** | **str** | A DNS domain suffix such as vmware.com.  | [optional] 
**primary_wins** | **str** | The IP address of the primary WINS server.  This property is ignored for Linux guest operating systems.  | [optional] 
**secondary_wins** | **str** | The IP address of the secondary WINS server.  This property is ignored for Linux guest operating systems.  | [optional] 
**net_bios** | [**CustomizationNetBIOSModeEnum**](CustomizationNetBIOSModeEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.customization_ip_settings import CustomizationIPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationIPSettings from a JSON string
customization_ip_settings_instance = CustomizationIPSettings.from_json(json)
# print the JSON string representation of the object
print CustomizationIPSettings.to_json()

# convert the object into a dict
customization_ip_settings_dict = customization_ip_settings_instance.to_dict()
# create an instance of CustomizationIPSettings from a dict
customization_ip_settings_form_dict = customization_ip_settings.from_dict(customization_ip_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


