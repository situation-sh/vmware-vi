# ArrayOfFirewallProfile

A boxed array of *FirewallProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FirewallProfile]**](FirewallProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_firewall_profile import ArrayOfFirewallProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFirewallProfile from a JSON string
array_of_firewall_profile_instance = ArrayOfFirewallProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfFirewallProfile.to_json()

# convert the object into a dict
array_of_firewall_profile_dict = array_of_firewall_profile_instance.to_dict()
# create an instance of ArrayOfFirewallProfile from a dict
array_of_firewall_profile_form_dict = array_of_firewall_profile.from_dict(array_of_firewall_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


