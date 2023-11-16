# VsanHostDiskMapping

A *VsanHostDiskMapping* is a set of one SSD *HostScsiDisk* backed by a set of one or more non-SSD *HostScsiDisk*.  The maximum allowed *VsanHostDiskMapping* for a host is 5. A maximum set of 7 non-SSDs *HostScsiDisk* can be added to the one SSD *HostScsiDisk*.  See also *VsanHostConfigInfoStorageInfo*, *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssd** | [**HostScsiDisk**](HostScsiDisk.md) |  | 
**non_ssd** | [**List[HostScsiDisk]**](HostScsiDisk.md) | Set of non-SSD backing *HostScsiDisk*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_disk_mapping import VsanHostDiskMapping

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDiskMapping from a JSON string
vsan_host_disk_mapping_instance = VsanHostDiskMapping.from_json(json)
# print the JSON string representation of the object
print VsanHostDiskMapping.to_json()

# convert the object into a dict
vsan_host_disk_mapping_dict = vsan_host_disk_mapping_instance.to_dict()
# create an instance of VsanHostDiskMapping from a dict
vsan_host_disk_mapping_form_dict = vsan_host_disk_mapping.from_dict(vsan_host_disk_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


