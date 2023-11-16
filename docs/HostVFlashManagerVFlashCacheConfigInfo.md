# HostVFlashManagerVFlashCacheConfigInfo

Data object describes host vFlash cache configuration information.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_module_config_option** | [**List[HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption]**](HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption.md) | Cache configuration options for the supported vFlash modules.  ***Since:*** vSphere API 5.5  | [optional] 
**default_v_flash_module** | **str** | Name of the default vFlash module for the read-write cache associated with the VMs of this host.  This setting can be overridden by *VirtualDiskVFlashCacheConfigInfo.vFlashModule* per VMDK.  ***Since:*** vSphere API 5.5  | [optional] 
**swap_cache_reservation_in_gb** | **int** | Amount of vFlash resource is allocated to the host swap cache.  As long as set, reservation will be permanent and retain regardless of host power state. The host swap cache will be disabled if reservation is set to zero.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_cache_config_info import HostVFlashManagerVFlashCacheConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashCacheConfigInfo from a JSON string
host_v_flash_manager_v_flash_cache_config_info_instance = HostVFlashManagerVFlashCacheConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashCacheConfigInfo.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_cache_config_info_dict = host_v_flash_manager_v_flash_cache_config_info_instance.to_dict()
# create an instance of HostVFlashManagerVFlashCacheConfigInfo from a dict
host_v_flash_manager_v_flash_cache_config_info_form_dict = host_v_flash_manager_v_flash_cache_config_info.from_dict(host_v_flash_manager_v_flash_cache_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


