# NetworkPolicyProfile

The *NetworkPolicyProfile* data object represents a network policy.  The *ApplyProfile.policy* property contains network configuration data values.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.network_policy_profile import NetworkPolicyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPolicyProfile from a JSON string
network_policy_profile_instance = NetworkPolicyProfile.from_json(json)
# print the JSON string representation of the object
print NetworkPolicyProfile.to_json()

# convert the object into a dict
network_policy_profile_dict = network_policy_profile_instance.to_dict()
# create an instance of NetworkPolicyProfile from a dict
network_policy_profile_form_dict = network_policy_profile.from_dict(network_policy_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


