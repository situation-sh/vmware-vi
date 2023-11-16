# ArrayOfFirewallProfileRulesetProfile

A boxed array of *FirewallProfileRulesetProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FirewallProfileRulesetProfile]**](FirewallProfileRulesetProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_firewall_profile_ruleset_profile import ArrayOfFirewallProfileRulesetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFirewallProfileRulesetProfile from a JSON string
array_of_firewall_profile_ruleset_profile_instance = ArrayOfFirewallProfileRulesetProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfFirewallProfileRulesetProfile.to_json()

# convert the object into a dict
array_of_firewall_profile_ruleset_profile_dict = array_of_firewall_profile_ruleset_profile_instance.to_dict()
# create an instance of ArrayOfFirewallProfileRulesetProfile from a dict
array_of_firewall_profile_ruleset_profile_form_dict = array_of_firewall_profile_ruleset_profile.from_dict(array_of_firewall_profile_ruleset_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


