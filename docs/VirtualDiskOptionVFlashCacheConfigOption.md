# VirtualDiskOptionVFlashCacheConfigOption

Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Options for vFlash cache configuration.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_consistency_type** | [**ChoiceOption**](ChoiceOption.md) |  | 
**cache_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**reservation_in_mb** | [**LongOption**](LongOption.md) |  | 
**block_size_in_kb** | [**LongOption**](LongOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_disk_option_v_flash_cache_config_option import VirtualDiskOptionVFlashCacheConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskOptionVFlashCacheConfigOption from a JSON string
virtual_disk_option_v_flash_cache_config_option_instance = VirtualDiskOptionVFlashCacheConfigOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskOptionVFlashCacheConfigOption.to_json()

# convert the object into a dict
virtual_disk_option_v_flash_cache_config_option_dict = virtual_disk_option_v_flash_cache_config_option_instance.to_dict()
# create an instance of VirtualDiskOptionVFlashCacheConfigOption from a dict
virtual_disk_option_v_flash_cache_config_option_form_dict = virtual_disk_option_v_flash_cache_config_option.from_dict(virtual_disk_option_v_flash_cache_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


