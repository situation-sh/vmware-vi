# ProfileDescription

The *ProfileDescription* data object describes a profile.  The description contains multiple sections. Each section describes a part of the profile.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | [**List[ProfileDescriptionSection]**](ProfileDescriptionSection.md) | Sections which make up the profile description.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_description import ProfileDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileDescription from a JSON string
profile_description_instance = ProfileDescription.from_json(json)
# print the JSON string representation of the object
print ProfileDescription.to_json()

# convert the object into a dict
profile_description_dict = profile_description_instance.to_dict()
# create an instance of ProfileDescription from a dict
profile_description_form_dict = profile_description.from_dict(profile_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


