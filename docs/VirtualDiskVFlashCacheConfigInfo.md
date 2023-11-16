# VirtualDiskVFlashCacheConfigInfo

Data object describes the vFlash cache configuration on this virtual disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_module** | **str** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Name of vFlash module which manages the cache.  If not specified, default setting *HostVFlashManagerVFlashCacheConfigSpec.defaultVFlashModule* will be used.  ***Since:*** vSphere API 5.5  | [optional] 
**reservation_in_mb** | **int** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Amount of vFlash resource that is guaranteed available to the cache.  If not specified, default reservation will be used.  ***Since:*** vSphere API 5.5  | [optional] 
**cache_consistency_type** | **str** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Cache data consistency types after a crash.  See *VirtualDiskVFlashCacheConfigInfoCacheConsistencyType_enum* for supported types. If not specified, the default value used is *strong*  ***Since:*** vSphere API 5.5  | [optional] 
**cache_mode** | **str** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Cache modes.  See *VirtualDiskVFlashCacheConfigInfoCacheMode_enum* for supported modes. If not specified, the default value used is *write_thru*.  ***Since:*** vSphere API 5.5  | [optional] 
**block_size_in_kb** | **int** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Cache block size.  This parameter allows the user to control how much data gets cached on a single access to the VMDK. Max block size is 1MB. Default is 4KB.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_v_flash_cache_config_info import VirtualDiskVFlashCacheConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskVFlashCacheConfigInfo from a JSON string
virtual_disk_v_flash_cache_config_info_instance = VirtualDiskVFlashCacheConfigInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskVFlashCacheConfigInfo.to_json()

# convert the object into a dict
virtual_disk_v_flash_cache_config_info_dict = virtual_disk_v_flash_cache_config_info_instance.to_dict()
# create an instance of VirtualDiskVFlashCacheConfigInfo from a dict
virtual_disk_v_flash_cache_config_info_form_dict = virtual_disk_v_flash_cache_config_info.from_dict(virtual_disk_v_flash_cache_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


