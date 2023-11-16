# FirewallProfileRulesetProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.firewall_profile_ruleset_profile import FirewallProfileRulesetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfileRulesetProfile from a JSON string
firewall_profile_ruleset_profile_instance = FirewallProfileRulesetProfile.from_json(json)
# print the JSON string representation of the object
print FirewallProfileRulesetProfile.to_json()

# convert the object into a dict
firewall_profile_ruleset_profile_dict = firewall_profile_ruleset_profile_instance.to_dict()
# create an instance of FirewallProfileRulesetProfile from a dict
firewall_profile_ruleset_profile_form_dict = firewall_profile_ruleset_profile.from_dict(firewall_profile_ruleset_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


