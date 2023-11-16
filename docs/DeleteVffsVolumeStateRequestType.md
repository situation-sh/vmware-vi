# DeleteVffsVolumeStateRequestType

The parameters of *HostStorageSystem.DeleteVffsVolumeState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_uuid** | **str** | The VFFS UUID.  | 

## Example

```python
from vmware_vi.models.delete_vffs_volume_state_request_type import DeleteVffsVolumeStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVffsVolumeStateRequestType from a JSON string
delete_vffs_volume_state_request_type_instance = DeleteVffsVolumeStateRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteVffsVolumeStateRequestType.to_json()

# convert the object into a dict
delete_vffs_volume_state_request_type_dict = delete_vffs_volume_state_request_type_instance.to_dict()
# create an instance of DeleteVffsVolumeStateRequestType from a dict
delete_vffs_volume_state_request_type_form_dict = delete_vffs_volume_state_request_type.from_dict(delete_vffs_volume_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


