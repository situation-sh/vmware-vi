# HostVffsVolume

vFlash File System Volume.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major_version** | **int** | Major version number of VFFS.  ***Since:*** vSphere API 5.5  | 
**version** | **str** | Version string.  Contains major and minor version numbers.  ***Since:*** vSphere API 5.5  | 
**uuid** | **str** | The universally unique identifier assigned to VFFS.  ***Since:*** vSphere API 5.5  | 
**extent** | [**List[HostScsiDiskPartition]**](HostScsiDiskPartition.md) | The list of partition names that comprise this disk&#39;s VFFS extents.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_vffs_volume import HostVffsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostVffsVolume from a JSON string
host_vffs_volume_instance = HostVffsVolume.from_json(json)
# print the JSON string representation of the object
print HostVffsVolume.to_json()

# convert the object into a dict
host_vffs_volume_dict = host_vffs_volume_instance.to_dict()
# create an instance of HostVffsVolume from a dict
host_vffs_volume_form_dict = host_vffs_volume.from_dict(host_vffs_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


