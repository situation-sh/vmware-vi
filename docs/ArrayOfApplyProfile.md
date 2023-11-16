# ArrayOfApplyProfile

A boxed array of *ApplyProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ApplyProfile]**](ApplyProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_apply_profile import ArrayOfApplyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfApplyProfile from a JSON string
array_of_apply_profile_instance = ArrayOfApplyProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfApplyProfile.to_json()

# convert the object into a dict
array_of_apply_profile_dict = array_of_apply_profile_instance.to_dict()
# create an instance of ArrayOfApplyProfile from a dict
array_of_apply_profile_form_dict = array_of_apply_profile.from_dict(array_of_apply_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


