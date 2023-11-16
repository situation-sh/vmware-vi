# NasStorageProfile

The *NasStorageProfile* data object represents one NAS datastore configuration.  Use the *ApplyProfile.policy* list for access to configuration data for the NAS storage profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.nas_storage_profile import NasStorageProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NasStorageProfile from a JSON string
nas_storage_profile_instance = NasStorageProfile.from_json(json)
# print the JSON string representation of the object
print NasStorageProfile.to_json()

# convert the object into a dict
nas_storage_profile_dict = nas_storage_profile_instance.to_dict()
# create an instance of NasStorageProfile from a dict
nas_storage_profile_form_dict = nas_storage_profile.from_dict(nas_storage_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


