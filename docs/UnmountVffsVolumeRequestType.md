# UnmountVffsVolumeRequestType

The parameters of *HostStorageSystem.UnmountVffsVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.unmount_vffs_volume_request_type import UnmountVffsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmountVffsVolumeRequestType from a JSON string
unmount_vffs_volume_request_type_instance = UnmountVffsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print UnmountVffsVolumeRequestType.to_json()

# convert the object into a dict
unmount_vffs_volume_request_type_dict = unmount_vffs_volume_request_type_instance.to_dict()
# create an instance of UnmountVffsVolumeRequestType from a dict
unmount_vffs_volume_request_type_form_dict = unmount_vffs_volume_request_type.from_dict(unmount_vffs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


