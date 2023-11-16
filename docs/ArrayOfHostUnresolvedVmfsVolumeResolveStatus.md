# ArrayOfHostUnresolvedVmfsVolumeResolveStatus

A boxed array of *HostUnresolvedVmfsVolumeResolveStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostUnresolvedVmfsVolumeResolveStatus]**](HostUnresolvedVmfsVolumeResolveStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_unresolved_vmfs_volume_resolve_status import ArrayOfHostUnresolvedVmfsVolumeResolveStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostUnresolvedVmfsVolumeResolveStatus from a JSON string
array_of_host_unresolved_vmfs_volume_resolve_status_instance = ArrayOfHostUnresolvedVmfsVolumeResolveStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostUnresolvedVmfsVolumeResolveStatus.to_json()

# convert the object into a dict
array_of_host_unresolved_vmfs_volume_resolve_status_dict = array_of_host_unresolved_vmfs_volume_resolve_status_instance.to_dict()
# create an instance of ArrayOfHostUnresolvedVmfsVolumeResolveStatus from a dict
array_of_host_unresolved_vmfs_volume_resolve_status_form_dict = array_of_host_unresolved_vmfs_volume_resolve_status.from_dict(array_of_host_unresolved_vmfs_volume_resolve_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


