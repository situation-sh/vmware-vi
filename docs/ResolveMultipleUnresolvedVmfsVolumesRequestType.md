# ResolveMultipleUnresolvedVmfsVolumesRequestType

The parameters of *HostStorageSystem.ResolveMultipleUnresolvedVmfsVolumes*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_spec** | [**List[HostUnresolvedVmfsResolutionSpec]**](HostUnresolvedVmfsResolutionSpec.md) | List of data object that describes what the disk extents to be used for creating the new VMFS volume.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.resolve_multiple_unresolved_vmfs_volumes_request_type import ResolveMultipleUnresolvedVmfsVolumesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveMultipleUnresolvedVmfsVolumesRequestType from a JSON string
resolve_multiple_unresolved_vmfs_volumes_request_type_instance = ResolveMultipleUnresolvedVmfsVolumesRequestType.from_json(json)
# print the JSON string representation of the object
print ResolveMultipleUnresolvedVmfsVolumesRequestType.to_json()

# convert the object into a dict
resolve_multiple_unresolved_vmfs_volumes_request_type_dict = resolve_multiple_unresolved_vmfs_volumes_request_type_instance.to_dict()
# create an instance of ResolveMultipleUnresolvedVmfsVolumesRequestType from a dict
resolve_multiple_unresolved_vmfs_volumes_request_type_form_dict = resolve_multiple_unresolved_vmfs_volumes_request_type.from_dict(resolve_multiple_unresolved_vmfs_volumes_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


