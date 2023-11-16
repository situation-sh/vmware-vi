# MountVmfsVolumeRequestType

The parameters of *HostStorageSystem.MountVmfsVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.mount_vmfs_volume_request_type import MountVmfsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MountVmfsVolumeRequestType from a JSON string
mount_vmfs_volume_request_type_instance = MountVmfsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print MountVmfsVolumeRequestType.to_json()

# convert the object into a dict
mount_vmfs_volume_request_type_dict = mount_vmfs_volume_request_type_instance.to_dict()
# create an instance of MountVmfsVolumeRequestType from a dict
mount_vmfs_volume_request_type_form_dict = mount_vmfs_volume_request_type.from_dict(mount_vmfs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


