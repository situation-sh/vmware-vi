# CustomizationGlobalIPSettings

A collection of global IP settings for a virtual network adapter.  In Linux, DNS server settings are global. The settings can either be statically set or supplied by a DHCP server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_suffix_list** | **List[str]** | List of name resolution suffixes for the virtual network adapter.  This list applies to both Windows and Linux guest customization. For Linux, this setting is global, whereas in Windows, this setting is listed on a per-adapter basis, even though the setting is global in Windows.  | [optional] 
**dns_server_list** | **List[str]** | List of DNS servers, for a virtual network adapter with a static IP address.  If this list is empty, then the guest operating system is expected to use a DHCP server to get its DNS server settings. These settings configure the virtual machine to use the specified DNS servers. These DNS server settings are listed in order of preference.  | [optional] 

## Example

```python
from vmware_vi.models.customization_global_ip_settings import CustomizationGlobalIPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationGlobalIPSettings from a JSON string
customization_global_ip_settings_instance = CustomizationGlobalIPSettings.from_json(json)
# print the JSON string representation of the object
print CustomizationGlobalIPSettings.to_json()

# convert the object into a dict
customization_global_ip_settings_dict = customization_global_ip_settings_instance.to_dict()
# create an instance of CustomizationGlobalIPSettings from a dict
customization_global_ip_settings_form_dict = customization_global_ip_settings.from_dict(customization_global_ip_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


