# SecurityProfile

The *SecurityProfile* data object represents host security configuration.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**List[PermissionProfile]**](PermissionProfile.md) | Permission configuration.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.security_profile import SecurityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityProfile from a JSON string
security_profile_instance = SecurityProfile.from_json(json)
# print the JSON string representation of the object
print SecurityProfile.to_json()

# convert the object into a dict
security_profile_dict = security_profile_instance.to_dict()
# create an instance of SecurityProfile from a dict
security_profile_form_dict = security_profile.from_dict(security_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


