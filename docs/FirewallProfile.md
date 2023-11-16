# FirewallProfile

The *FirewallProfile* data object represents a host firewall configuration.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset** | [**List[FirewallProfileRulesetProfile]**](FirewallProfileRulesetProfile.md) | List of Rulesets that will be configured for the firewall subprofile.  The rulesets can be enabled or disabled from the profile.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.firewall_profile import FirewallProfile

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfile from a JSON string
firewall_profile_instance = FirewallProfile.from_json(json)
# print the JSON string representation of the object
print FirewallProfile.to_json()

# convert the object into a dict
firewall_profile_dict = firewall_profile_instance.to_dict()
# create an instance of FirewallProfile from a dict
firewall_profile_form_dict = firewall_profile.from_dict(firewall_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


