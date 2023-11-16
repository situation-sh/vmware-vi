# ArrayOfOptionProfile

A boxed array of *OptionProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OptionProfile]**](OptionProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_option_profile import ArrayOfOptionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOptionProfile from a JSON string
array_of_option_profile_instance = ArrayOfOptionProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfOptionProfile.to_json()

# convert the object into a dict
array_of_option_profile_dict = array_of_option_profile_instance.to_dict()
# create an instance of ArrayOfOptionProfile from a dict
array_of_option_profile_form_dict = array_of_option_profile.from_dict(array_of_option_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


