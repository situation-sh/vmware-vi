# ArrayOfStorageProfile

A boxed array of *StorageProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageProfile]**](StorageProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_profile import ArrayOfStorageProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageProfile from a JSON string
array_of_storage_profile_instance = ArrayOfStorageProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageProfile.to_json()

# convert the object into a dict
array_of_storage_profile_dict = array_of_storage_profile_instance.to_dict()
# create an instance of ArrayOfStorageProfile from a dict
array_of_storage_profile_form_dict = array_of_storage_profile.from_dict(array_of_storage_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


