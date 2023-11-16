# ArrayOfHostApplyProfile

A boxed array of *HostApplyProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostApplyProfile]**](HostApplyProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_apply_profile import ArrayOfHostApplyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostApplyProfile from a JSON string
array_of_host_apply_profile_instance = ArrayOfHostApplyProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostApplyProfile.to_json()

# convert the object into a dict
array_of_host_apply_profile_dict = array_of_host_apply_profile_instance.to_dict()
# create an instance of ArrayOfHostApplyProfile from a dict
array_of_host_apply_profile_form_dict = array_of_host_apply_profile.from_dict(array_of_host_apply_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


