# UnmountVmfsVolumeRequestType

The parameters of *HostStorageSystem.UnmountVmfsVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.unmount_vmfs_volume_request_type import UnmountVmfsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmountVmfsVolumeRequestType from a JSON string
unmount_vmfs_volume_request_type_instance = UnmountVmfsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print UnmountVmfsVolumeRequestType.to_json()

# convert the object into a dict
unmount_vmfs_volume_request_type_dict = unmount_vmfs_volume_request_type_instance.to_dict()
# create an instance of UnmountVmfsVolumeRequestType from a dict
unmount_vmfs_volume_request_type_form_dict = unmount_vmfs_volume_request_type.from_dict(unmount_vmfs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


