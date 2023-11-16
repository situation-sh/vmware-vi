# DeleteVmfsVolumeStateRequestType

The parameters of *HostStorageSystem.DeleteVmfsVolumeState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **str** | The VMFS UUID.  | 

## Example

```python
from vmware_vi.models.delete_vmfs_volume_state_request_type import DeleteVmfsVolumeStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVmfsVolumeStateRequestType from a JSON string
delete_vmfs_volume_state_request_type_instance = DeleteVmfsVolumeStateRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteVmfsVolumeStateRequestType.to_json()

# convert the object into a dict
delete_vmfs_volume_state_request_type_dict = delete_vmfs_volume_state_request_type_instance.to_dict()
# create an instance of DeleteVmfsVolumeStateRequestType from a dict
delete_vmfs_volume_state_request_type_form_dict = delete_vmfs_volume_state_request_type.from_dict(delete_vmfs_volume_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


