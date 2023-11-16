# StorageResourceManagerStorageProfileStatistics

A data object to report aggregate storage statistics by storage profile  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Profile identifier for the reported statistics  ***Since:*** vSphere API 6.0  | 
**total_space_mb** | **int** | The aggregate storage capacity available for a given storage capability profile.  The capacity is reported in Megabytes.  ***Since:*** vSphere API 6.0  | 
**used_space_mb** | **int** | The aggregate used storage capacity by a given storage capability profile The used space is reported in Megabytes  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.storage_resource_manager_storage_profile_statistics import StorageResourceManagerStorageProfileStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StorageResourceManagerStorageProfileStatistics from a JSON string
storage_resource_manager_storage_profile_statistics_instance = StorageResourceManagerStorageProfileStatistics.from_json(json)
# print the JSON string representation of the object
print StorageResourceManagerStorageProfileStatistics.to_json()

# convert the object into a dict
storage_resource_manager_storage_profile_statistics_dict = storage_resource_manager_storage_profile_statistics_instance.to_dict()
# create an instance of StorageResourceManagerStorageProfileStatistics from a dict
storage_resource_manager_storage_profile_statistics_form_dict = storage_resource_manager_storage_profile_statistics.from_dict(storage_resource_manager_storage_profile_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


