# UnmountVmfsVolumeExRequestType

The parameters of *HostStorageSystem.UnmountVmfsVolumeEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **List[str]** | each element specifies the UUID of a VMFS volume to be unmounted.  | 

## Example

```python
from vmware_vi.models.unmount_vmfs_volume_ex_request_type import UnmountVmfsVolumeExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmountVmfsVolumeExRequestType from a JSON string
unmount_vmfs_volume_ex_request_type_instance = UnmountVmfsVolumeExRequestType.from_json(json)
# print the JSON string representation of the object
print UnmountVmfsVolumeExRequestType.to_json()

# convert the object into a dict
unmount_vmfs_volume_ex_request_type_dict = unmount_vmfs_volume_ex_request_type_instance.to_dict()
# create an instance of UnmountVmfsVolumeExRequestType from a dict
unmount_vmfs_volume_ex_request_type_form_dict = unmount_vmfs_volume_ex_request_type.from_dict(unmount_vmfs_volume_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


