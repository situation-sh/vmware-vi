# ArrayOfHostPortGroupProfile

A boxed array of *HostPortGroupProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPortGroupProfile]**](HostPortGroupProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_port_group_profile import ArrayOfHostPortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPortGroupProfile from a JSON string
array_of_host_port_group_profile_instance = ArrayOfHostPortGroupProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPortGroupProfile.to_json()

# convert the object into a dict
array_of_host_port_group_profile_dict = array_of_host_port_group_profile_instance.to_dict()
# create an instance of ArrayOfHostPortGroupProfile from a dict
array_of_host_port_group_profile_form_dict = array_of_host_port_group_profile.from_dict(array_of_host_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


