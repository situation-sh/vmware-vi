# ProfileDescriptionSection

The *ProfileDescriptionSection* data object contains a profile element description and any messages that may be associated with the profile section.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**ExtendedElementDescription**](ExtendedElementDescription.md) |  | 
**message** | [**List[LocalizableMessage]**](LocalizableMessage.md) | List of messages that make up the section.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_description_section import ProfileDescriptionSection

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileDescriptionSection from a JSON string
profile_description_section_instance = ProfileDescriptionSection.from_json(json)
# print the JSON string representation of the object
print ProfileDescriptionSection.to_json()

# convert the object into a dict
profile_description_section_dict = profile_description_section_instance.to_dict()
# create an instance of ProfileDescriptionSection from a dict
profile_description_section_form_dict = profile_description_section.from_dict(profile_description_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


