# HostUnresolvedVmfsVolume

Information about detected unbound, unresolved VMFS volume.  An unresolved VMFS volume is reported when one or more device partitions of volume are detected to have copies of extents of the volume. Such copies can be created via replication or snapshots.  UnresolvedVmfsVolume are not mounted on the host where they are detected. User may choose to resignature the volume in which case a new Uuid is assigned to the volume and contents of the VMFS volume is kept intact.  User may choose to keep the original Uuid and mount the VMFS volume as it is on the given host. In this case, user has chosen to mount the copy of the VMFS volume on that host with no change to the original Uuid. This may fail with VmfsVolumeAlreadyMounted exception if there is an existing VMFS volume with the same Uuid mounted somewhere in the same datacenter.  Simple diagram representing the possible operations on UnresolvedVmfsVolume        ---------------------------------------------------------------------------       |                resignature                 forceMount                   |       |  VmfsVolume <---------------  Unresolved ------------>  VmfsVolume with |       | forceMountedInfo              Vmfs Volume              forceMountedInfo |       |  not set                                                  will be set   |       ---------------------------------------------------------------------------  See also *HostStorageSystem*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extent** | [**List[HostUnresolvedVmfsExtent]**](HostUnresolvedVmfsExtent.md) | List of detected copies of VMFS extents.  ***Since:*** vSphere API 4.0  | 
**vmfs_label** | **str** | The detected VMFS label name  ***Since:*** vSphere API 4.0  | 
**vmfs_uuid** | **str** | The detected VMFS UUID  ***Since:*** vSphere API 4.0  | 
**total_blocks** | **int** | Total number of blocks in this volume.  ***Since:*** vSphere API 4.0  | 
**resolve_status** | [**HostUnresolvedVmfsVolumeResolveStatus**](HostUnresolvedVmfsVolumeResolveStatus.md) |  | 

## Example

```python
from vmware_vi.models.host_unresolved_vmfs_volume import HostUnresolvedVmfsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostUnresolvedVmfsVolume from a JSON string
host_unresolved_vmfs_volume_instance = HostUnresolvedVmfsVolume.from_json(json)
# print the JSON string representation of the object
print HostUnresolvedVmfsVolume.to_json()

# convert the object into a dict
host_unresolved_vmfs_volume_dict = host_unresolved_vmfs_volume_instance.to_dict()
# create an instance of HostUnresolvedVmfsVolume from a dict
host_unresolved_vmfs_volume_form_dict = host_unresolved_vmfs_volume.from_dict(host_unresolved_vmfs_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


