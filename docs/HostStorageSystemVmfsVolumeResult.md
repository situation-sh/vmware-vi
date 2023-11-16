# HostStorageSystemVmfsVolumeResult

Contains the result of the operation performed on a VMFS volume.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | UUID of VMFS volume  ***Since:*** vSphere API 6.0  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_storage_system_vmfs_volume_result import HostStorageSystemVmfsVolumeResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageSystemVmfsVolumeResult from a JSON string
host_storage_system_vmfs_volume_result_instance = HostStorageSystemVmfsVolumeResult.from_json(json)
# print the JSON string representation of the object
print HostStorageSystemVmfsVolumeResult.to_json()

# convert the object into a dict
host_storage_system_vmfs_volume_result_dict = host_storage_system_vmfs_volume_result_instance.to_dict()
# create an instance of HostStorageSystemVmfsVolumeResult from a dict
host_storage_system_vmfs_volume_result_form_dict = host_storage_system_vmfs_volume_result.from_dict(host_storage_system_vmfs_volume_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


