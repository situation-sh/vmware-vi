# ArrayOfProfileDescriptionSection

A boxed array of *ProfileDescriptionSection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileDescriptionSection]**](ProfileDescriptionSection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_description_section import ArrayOfProfileDescriptionSection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileDescriptionSection from a JSON string
array_of_profile_description_section_instance = ArrayOfProfileDescriptionSection.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileDescriptionSection.to_json()

# convert the object into a dict
array_of_profile_description_section_dict = array_of_profile_description_section_instance.to_dict()
# create an instance of ArrayOfProfileDescriptionSection from a dict
array_of_profile_description_section_form_dict = array_of_profile_description_section.from_dict(array_of_profile_description_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


