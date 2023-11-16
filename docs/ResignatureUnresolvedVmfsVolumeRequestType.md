# ResignatureUnresolvedVmfsVolumeRequestType

The parameters of *HostDatastoreSystem.ResignatureUnresolvedVmfsVolume_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_spec** | [**HostUnresolvedVmfsResignatureSpec**](HostUnresolvedVmfsResignatureSpec.md) |  | 

## Example

```python
from vmware_vi.models.resignature_unresolved_vmfs_volume_request_type import ResignatureUnresolvedVmfsVolumeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResignatureUnresolvedVmfsVolumeRequestType from a JSON string
resignature_unresolved_vmfs_volume_request_type_instance = ResignatureUnresolvedVmfsVolumeRequestType.from_json(json)
# print the JSON string representation of the object
print ResignatureUnresolvedVmfsVolumeRequestType.to_json()

# convert the object into a dict
resignature_unresolved_vmfs_volume_request_type_dict = resignature_unresolved_vmfs_volume_request_type_instance.to_dict()
# create an instance of ResignatureUnresolvedVmfsVolumeRequestType from a dict
resignature_unresolved_vmfs_volume_request_type_form_dict = resignature_unresolved_vmfs_volume_request_type.from_dict(resignature_unresolved_vmfs_volume_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


