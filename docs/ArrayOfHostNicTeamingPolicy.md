# ArrayOfHostNicTeamingPolicy

A boxed array of *HostNicTeamingPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNicTeamingPolicy]**](HostNicTeamingPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nic_teaming_policy import ArrayOfHostNicTeamingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNicTeamingPolicy from a JSON string
array_of_host_nic_teaming_policy_instance = ArrayOfHostNicTeamingPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNicTeamingPolicy.to_json()

# convert the object into a dict
array_of_host_nic_teaming_policy_dict = array_of_host_nic_teaming_policy_instance.to_dict()
# create an instance of ArrayOfHostNicTeamingPolicy from a dict
array_of_host_nic_teaming_policy_form_dict = array_of_host_nic_teaming_policy.from_dict(array_of_host_nic_teaming_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


