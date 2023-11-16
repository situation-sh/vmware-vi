# ProfileApplyProfileProperty

The *ProfileApplyProfileProperty* data object defines one or more subprofiles.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | Name of the property.  ***Since:*** vSphere API 5.0  | 
**array** | **bool** | Flag indicating whether this property is an array of profiles.  ***Since:*** vSphere API 5.0  | 
**profile** | [**List[ApplyProfile]**](ApplyProfile.md) | Subprofiles that define policies and nested subprofiles.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_apply_profile_property import ProfileApplyProfileProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileApplyProfileProperty from a JSON string
profile_apply_profile_property_instance = ProfileApplyProfileProperty.from_json(json)
# print the JSON string representation of the object
print ProfileApplyProfileProperty.to_json()

# convert the object into a dict
profile_apply_profile_property_dict = profile_apply_profile_property_instance.to_dict()
# create an instance of ProfileApplyProfileProperty from a dict
profile_apply_profile_property_form_dict = profile_apply_profile_property.from_dict(profile_apply_profile_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


