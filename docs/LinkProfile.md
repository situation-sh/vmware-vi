# LinkProfile

The LinkProfile data object represents a subprofile for links connected to virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.link_profile import LinkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProfile from a JSON string
link_profile_instance = LinkProfile.from_json(json)
# print the JSON string representation of the object
print LinkProfile.to_json()

# convert the object into a dict
link_profile_dict = link_profile_instance.to_dict()
# create an instance of LinkProfile from a dict
link_profile_form_dict = link_profile.from_dict(link_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


