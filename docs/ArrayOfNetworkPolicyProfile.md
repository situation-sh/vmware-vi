# ArrayOfNetworkPolicyProfile

A boxed array of *NetworkPolicyProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetworkPolicyProfile]**](NetworkPolicyProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_network_policy_profile import ArrayOfNetworkPolicyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetworkPolicyProfile from a JSON string
array_of_network_policy_profile_instance = ArrayOfNetworkPolicyProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetworkPolicyProfile.to_json()

# convert the object into a dict
array_of_network_policy_profile_dict = array_of_network_policy_profile_instance.to_dict()
# create an instance of ArrayOfNetworkPolicyProfile from a dict
array_of_network_policy_profile_form_dict = array_of_network_policy_profile.from_dict(array_of_network_policy_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


