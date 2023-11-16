# MountVmfsVolumeExRequestType

The parameters of *HostStorageSystem.MountVmfsVolumeEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **List[str]** | each element specifies the UUID of a VMFS volume to be unmounted.  | 

## Example

```python
from vmware_vi.models.mount_vmfs_volume_ex_request_type import MountVmfsVolumeExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MountVmfsVolumeExRequestType from a JSON string
mount_vmfs_volume_ex_request_type_instance = MountVmfsVolumeExRequestType.from_json(json)
# print the JSON string representation of the object
print MountVmfsVolumeExRequestType.to_json()

# convert the object into a dict
mount_vmfs_volume_ex_request_type_dict = mount_vmfs_volume_ex_request_type_instance.to_dict()
# create an instance of MountVmfsVolumeExRequestType from a dict
mount_vmfs_volume_ex_request_type_form_dict = mount_vmfs_volume_ex_request_type.from_dict(mount_vmfs_volume_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


