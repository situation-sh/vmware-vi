# VsanHostConfigInfoStorageInfo

Host-local VSAN storage configuration.  This data object is used both for specifying and retrieving storage configuration for a host participating in the VSAN service.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_claim_storage** | **bool** | Deprecated as this configuration will be deprecated, autoclaim will be no longer supported.  Whether the VSAN service is configured to automatically claim local unused storage on this host.  When set, the VSAN service will automatically format and use local disks. Side effects from any disk consumption will be reflected in *VsanHostConfigInfoStorageInfo.diskMapping*. If this argument is specified as a host-level configuration input at the VC-level (see *ClusterConfigInfoEx.vsanHostConfig*), it will override that of any cluster-level default value.  See also *VsanHostConfigInfoStorageInfo.diskMapping*, *ClusterConfigInfoEx.vsanHostConfig*, *VsanClusterConfigInfo.defaultConfig*.  ***Since:*** vSphere API 5.5  | [optional] 
**disk_mapping** | [**List[VsanHostDiskMapping]**](VsanHostDiskMapping.md) | Deprecated use *VsanHostConfigInfoStorageInfo.diskMapInfo* instead.  List of *VsanHostDiskMapping* entries in use by the VSAN service.  DiskMappings to be used by the VSAN service may be manually specified using *HostVsanSystem.InitializeDisks_Task*.  See also *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 5.5  | [optional] 
**disk_map_info** | [**List[VsanHostDiskMapInfo]**](VsanHostDiskMapInfo.md) | List of *VsanHostDiskMapping* entries with runtime information from the perspective of this host.  ***Since:*** vSphere API 6.0  | [optional] 
**checksum_enabled** | **bool** | Deprecated this attribute was originally used for indicating whether hardware checksums is supported on the disks. But in vSphere 2016 hardware checksums are replaced with software implementation, supported by all disks. This makes current field redundant, and its value as an input/output is ignored.  Whether checksum is enabled on all the disks in this host.  If any disk is not checksum capable or 520 bps formatted, we will skip it.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_config_info_storage_info import VsanHostConfigInfoStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostConfigInfoStorageInfo from a JSON string
vsan_host_config_info_storage_info_instance = VsanHostConfigInfoStorageInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostConfigInfoStorageInfo.to_json()

# convert the object into a dict
vsan_host_config_info_storage_info_dict = vsan_host_config_info_storage_info_instance.to_dict()
# create an instance of VsanHostConfigInfoStorageInfo from a dict
vsan_host_config_info_storage_info_form_dict = vsan_host_config_info_storage_info.from_dict(vsan_host_config_info_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


