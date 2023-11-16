# ArrayOfNetworkProfile

A boxed array of *NetworkProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetworkProfile]**](NetworkProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_network_profile import ArrayOfNetworkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetworkProfile from a JSON string
array_of_network_profile_instance = ArrayOfNetworkProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetworkProfile.to_json()

# convert the object into a dict
array_of_network_profile_dict = array_of_network_profile_instance.to_dict()
# create an instance of ArrayOfNetworkProfile from a dict
array_of_network_profile_form_dict = array_of_network_profile.from_dict(array_of_network_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


