# ArrayOfStorageResourceManagerStorageProfileStatistics

A boxed array of *StorageResourceManagerStorageProfileStatistics*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageResourceManagerStorageProfileStatistics]**](StorageResourceManagerStorageProfileStatistics.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_resource_manager_storage_profile_statistics import ArrayOfStorageResourceManagerStorageProfileStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageResourceManagerStorageProfileStatistics from a JSON string
array_of_storage_resource_manager_storage_profile_statistics_instance = ArrayOfStorageResourceManagerStorageProfileStatistics.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageResourceManagerStorageProfileStatistics.to_json()

# convert the object into a dict
array_of_storage_resource_manager_storage_profile_statistics_dict = array_of_storage_resource_manager_storage_profile_statistics_instance.to_dict()
# create an instance of ArrayOfStorageResourceManagerStorageProfileStatistics from a dict
array_of_storage_resource_manager_storage_profile_statistics_form_dict = array_of_storage_resource_manager_storage_profile_statistics.from_dict(array_of_storage_resource_manager_storage_profile_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


