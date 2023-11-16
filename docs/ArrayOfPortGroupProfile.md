# ArrayOfPortGroupProfile

A boxed array of *PortGroupProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PortGroupProfile]**](PortGroupProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_port_group_profile import ArrayOfPortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPortGroupProfile from a JSON string
array_of_port_group_profile_instance = ArrayOfPortGroupProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfPortGroupProfile.to_json()

# convert the object into a dict
array_of_port_group_profile_dict = array_of_port_group_profile_instance.to_dict()
# create an instance of ArrayOfPortGroupProfile from a dict
array_of_port_group_profile_form_dict = array_of_port_group_profile.from_dict(array_of_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


