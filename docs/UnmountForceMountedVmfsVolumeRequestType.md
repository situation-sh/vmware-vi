# UnmountForceMountedVmfsVolumeRequestType

The parameters of *HostStorageSystem.UnmountForceMountedVmfsVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.unmount_force_mounted_vmfs_volume_request_type import UnmountForceMountedVmfsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmountForceMountedVmfsVolumeRequestType from a JSON string
unmount_force_mounted_vmfs_volume_request_type_instance = UnmountForceMountedVmfsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print UnmountForceMountedVmfsVolumeRequestType.to_json()

# convert the object into a dict
unmount_force_mounted_vmfs_volume_request_type_dict = unmount_force_mounted_vmfs_volume_request_type_instance.to_dict()
# create an instance of UnmountForceMountedVmfsVolumeRequestType from a dict
unmount_force_mounted_vmfs_volume_request_type_form_dict = unmount_force_mounted_vmfs_volume_request_type.from_dict(unmount_force_mounted_vmfs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


