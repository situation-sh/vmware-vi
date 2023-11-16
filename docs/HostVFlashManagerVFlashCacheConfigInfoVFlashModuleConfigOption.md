# HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_module** | **str** | Name of the vFlash module  ***Since:*** vSphere API 5.5  | 
**v_flash_module_version** | **str** | Version of the vFlash module  ***Since:*** vSphere API 5.5  | 
**min_supported_module_version** | **str** | Minimum supported version  ***Since:*** vSphere API 5.5  | 
**cache_consistency_type** | [**ChoiceOption**](ChoiceOption.md) |  | 
**cache_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**block_size_in_kb_option** | [**LongOption**](LongOption.md) |  | 
**reservation_in_mb_option** | [**LongOption**](LongOption.md) |  | 
**max_disk_size_in_kb** | **int** | Maximal size of virtual disk supported in kilobytes.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option import HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption from a JSON string
host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option_instance = HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option_dict = host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option_instance.to_dict()
# create an instance of HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption from a dict
host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option_form_dict = host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option.from_dict(host_v_flash_manager_v_flash_cache_config_info_v_flash_module_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


