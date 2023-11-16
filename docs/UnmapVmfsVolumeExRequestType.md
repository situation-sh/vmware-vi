# UnmapVmfsVolumeExRequestType

The parameters of *HostStorageSystem.UnmapVmfsVolumeEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **List[str]** | each element specifies the UUID of a VMFS volume to be unmapped.  | 

## Example

```python
from vmware_vi.models.unmap_vmfs_volume_ex_request_type import UnmapVmfsVolumeExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmapVmfsVolumeExRequestType from a JSON string
unmap_vmfs_volume_ex_request_type_instance = UnmapVmfsVolumeExRequestType.from_json(json)
# print the JSON string representation of the object
print UnmapVmfsVolumeExRequestType.to_json()

# convert the object into a dict
unmap_vmfs_volume_ex_request_type_dict = unmap_vmfs_volume_ex_request_type_instance.to_dict()
# create an instance of UnmapVmfsVolumeExRequestType from a dict
unmap_vmfs_volume_ex_request_type_form_dict = unmap_vmfs_volume_ex_request_type.from_dict(unmap_vmfs_volume_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


