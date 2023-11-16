# NetworkProfileDnsConfigProfile

The *NetworkProfileDnsConfigProfile* data object represents DNS configuration for the host.  Use the *ApplyProfile.policy* list for access to configuration data for the DNS profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.network_profile_dns_config_profile import NetworkProfileDnsConfigProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProfileDnsConfigProfile from a JSON string
network_profile_dns_config_profile_instance = NetworkProfileDnsConfigProfile.from_json(json)
# print the JSON string representation of the object
print NetworkProfileDnsConfigProfile.to_json()

# convert the object into a dict
network_profile_dns_config_profile_dict = network_profile_dns_config_profile_instance.to_dict()
# create an instance of NetworkProfileDnsConfigProfile from a dict
network_profile_dns_config_profile_form_dict = network_profile_dns_config_profile.from_dict(network_profile_dns_config_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


