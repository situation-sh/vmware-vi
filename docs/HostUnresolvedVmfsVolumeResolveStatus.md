# HostUnresolvedVmfsVolumeResolveStatus

Data object that describes the resolvability of a volume.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolvable** | **bool** | Can this volume be resolved? There may be other reasons a volume cannot be resolved other than the fact that it is incomplete.  This boolean will authoritatively indicate if the server can resolve this volume.  ***Since:*** vSphere API 4.0  | 
**incomplete_extents** | **bool** | Is the list of extents for the volume a partial list? A volume can only be resignatured if all extents composing that volume are available.  Hence, a volume with a partial extent list cannot be resignatured.  In cases where this information is not known for a volume, this property will be unset.  ***Since:*** vSphere API 4.0  | [optional] 
**multiple_copies** | **bool** | Are there multiple copies of extents for this volume? If any extent of the volume has multiple copies then the extents to be resolved must be explicitly specified when resolving this volume.  In cases where this information is not known for a volume, this property will be unset.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_unresolved_vmfs_volume_resolve_status import HostUnresolvedVmfsVolumeResolveStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HostUnresolvedVmfsVolumeResolveStatus from a JSON string
host_unresolved_vmfs_volume_resolve_status_instance = HostUnresolvedVmfsVolumeResolveStatus.from_json(json)
# print the JSON string representation of the object
print HostUnresolvedVmfsVolumeResolveStatus.to_json()

# convert the object into a dict
host_unresolved_vmfs_volume_resolve_status_dict = host_unresolved_vmfs_volume_resolve_status_instance.to_dict()
# create an instance of HostUnresolvedVmfsVolumeResolveStatus from a dict
host_unresolved_vmfs_volume_resolve_status_form_dict = host_unresolved_vmfs_volume_resolve_status.from_dict(host_unresolved_vmfs_volume_resolve_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


