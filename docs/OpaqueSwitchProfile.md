# OpaqueSwitchProfile

The *OpaqueSwitchProfile* data object represents opaque switch configuration for the host.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.opaque_switch_profile import OpaqueSwitchProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueSwitchProfile from a JSON string
opaque_switch_profile_instance = OpaqueSwitchProfile.from_json(json)
# print the JSON string representation of the object
print OpaqueSwitchProfile.to_json()

# convert the object into a dict
opaque_switch_profile_dict = opaque_switch_profile_instance.to_dict()
# create an instance of OpaqueSwitchProfile from a dict
opaque_switch_profile_form_dict = opaque_switch_profile.from_dict(opaque_switch_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


