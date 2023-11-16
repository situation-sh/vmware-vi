# StorageProfile

The *StorageProfile* data object represents the host storage configuration.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_storage** | [**List[NasStorageProfile]**](NasStorageProfile.md) | List of NAS storage subprofiles.  Use the *NasStorageProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_profile import StorageProfile

# TODO update the JSON string below
json = "{}"
# create an instance of StorageProfile from a JSON string
storage_profile_instance = StorageProfile.from_json(json)
# print the JSON string representation of the object
print StorageProfile.to_json()

# convert the object into a dict
storage_profile_dict = storage_profile_instance.to_dict()
# create an instance of StorageProfile from a dict
storage_profile_form_dict = storage_profile.from_dict(storage_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


