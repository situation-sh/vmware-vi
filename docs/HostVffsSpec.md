# HostVffsSpec

This data object type describes the VFFS creation specification.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The device path of the SSD disk.  See also *HostScsiDisk.devicePath*.  ***Since:*** vSphere API 5.5  | 
**partition** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | [optional] 
**major_version** | **int** | Major version number of VFFS.  This can be changed if the VFFS is upgraded, but this is an irreversible change.  ***Since:*** vSphere API 5.5  | 
**volume_name** | **str** | Volume name of VFFS.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_vffs_spec import HostVffsSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVffsSpec from a JSON string
host_vffs_spec_instance = HostVffsSpec.from_json(json)
# print the JSON string representation of the object
print HostVffsSpec.to_json()

# convert the object into a dict
host_vffs_spec_dict = host_vffs_spec_instance.to_dict()
# create an instance of HostVffsSpec from a dict
host_vffs_spec_form_dict = host_vffs_spec.from_dict(host_vffs_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


