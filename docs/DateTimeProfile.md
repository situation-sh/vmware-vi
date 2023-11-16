# DateTimeProfile

The *DateTimeProfile* data object represents host date and time configuration.  Use the *ApplyProfile.policy* list for access to configuration data for the date and time profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.date_time_profile import DateTimeProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeProfile from a JSON string
date_time_profile_instance = DateTimeProfile.from_json(json)
# print the JSON string representation of the object
print DateTimeProfile.to_json()

# convert the object into a dict
date_time_profile_dict = date_time_profile_instance.to_dict()
# create an instance of DateTimeProfile from a dict
date_time_profile_form_dict = date_time_profile.from_dict(date_time_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


