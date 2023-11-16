# ArrayOfVlanProfile

A boxed array of *VlanProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VlanProfile]**](VlanProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vlan_profile import ArrayOfVlanProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVlanProfile from a JSON string
array_of_vlan_profile_instance = ArrayOfVlanProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfVlanProfile.to_json()

# convert the object into a dict
array_of_vlan_profile_dict = array_of_vlan_profile_instance.to_dict()
# create an instance of ArrayOfVlanProfile from a dict
array_of_vlan_profile_form_dict = array_of_vlan_profile.from_dict(array_of_vlan_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


