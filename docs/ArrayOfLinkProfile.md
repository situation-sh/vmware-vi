# ArrayOfLinkProfile

A boxed array of *LinkProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LinkProfile]**](LinkProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_link_profile import ArrayOfLinkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLinkProfile from a JSON string
array_of_link_profile_instance = ArrayOfLinkProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfLinkProfile.to_json()

# convert the object into a dict
array_of_link_profile_dict = array_of_link_profile_instance.to_dict()
# create an instance of ArrayOfLinkProfile from a dict
array_of_link_profile_form_dict = array_of_link_profile.from_dict(array_of_link_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


