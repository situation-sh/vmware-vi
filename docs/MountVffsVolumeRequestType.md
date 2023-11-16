# MountVffsVolumeRequestType

The parameters of *HostStorageSystem.MountVffsVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.mount_vffs_volume_request_type import MountVffsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MountVffsVolumeRequestType from a JSON string
mount_vffs_volume_request_type_instance = MountVffsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print MountVffsVolumeRequestType.to_json()

# convert the object into a dict
mount_vffs_volume_request_type_dict = mount_vffs_volume_request_type_instance.to_dict()
# create an instance of MountVffsVolumeRequestType from a dict
mount_vffs_volume_request_type_form_dict = mount_vffs_volume_request_type.from_dict(mount_vffs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


