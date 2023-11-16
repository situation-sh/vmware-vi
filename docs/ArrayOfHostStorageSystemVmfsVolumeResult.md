# ArrayOfHostStorageSystemVmfsVolumeResult

A boxed array of *HostStorageSystemVmfsVolumeResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostStorageSystemVmfsVolumeResult]**](HostStorageSystemVmfsVolumeResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_storage_system_vmfs_volume_result import ArrayOfHostStorageSystemVmfsVolumeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostStorageSystemVmfsVolumeResult from a JSON string
array_of_host_storage_system_vmfs_volume_result_instance = ArrayOfHostStorageSystemVmfsVolumeResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostStorageSystemVmfsVolumeResult.to_json()

# convert the object into a dict
array_of_host_storage_system_vmfs_volume_result_dict = array_of_host_storage_system_vmfs_volume_result_instance.to_dict()
# create an instance of ArrayOfHostStorageSystemVmfsVolumeResult from a dict
array_of_host_storage_system_vmfs_volume_result_form_dict = array_of_host_storage_system_vmfs_volume_result.from_dict(array_of_host_storage_system_vmfs_volume_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


