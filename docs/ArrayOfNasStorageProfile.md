# ArrayOfNasStorageProfile

A boxed array of *NasStorageProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NasStorageProfile]**](NasStorageProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nas_storage_profile import ArrayOfNasStorageProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNasStorageProfile from a JSON string
array_of_nas_storage_profile_instance = ArrayOfNasStorageProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfNasStorageProfile.to_json()

# convert the object into a dict
array_of_nas_storage_profile_dict = array_of_nas_storage_profile_instance.to_dict()
# create an instance of ArrayOfNasStorageProfile from a dict
array_of_nas_storage_profile_form_dict = array_of_nas_storage_profile.from_dict(array_of_nas_storage_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


