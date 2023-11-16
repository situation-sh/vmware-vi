# OptionProfile

The *OptionProfile* data object encapsulates one advanced configuration.  Use the *ApplyProfile.policy* list for access to configuration data for the option profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.option_profile import OptionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OptionProfile from a JSON string
option_profile_instance = OptionProfile.from_json(json)
# print the JSON string representation of the object
print OptionProfile.to_json()

# convert the object into a dict
option_profile_dict = option_profile_instance.to_dict()
# create an instance of OptionProfile from a dict
option_profile_form_dict = option_profile.from_dict(option_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


