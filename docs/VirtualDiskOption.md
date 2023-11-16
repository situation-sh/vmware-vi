# VirtualDiskOption

The VirtualDiskOption data class contains the options for the virtual disk data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_kb** | [**LongOption**](LongOption.md) |  | 
**io_allocation_option** | [**StorageIOAllocationOption**](StorageIOAllocationOption.md) |  | 
**v_flash_cache_config_option** | [**VirtualDiskOptionVFlashCacheConfigOption**](VirtualDiskOptionVFlashCacheConfigOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_option import VirtualDiskOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskOption from a JSON string
virtual_disk_option_instance = VirtualDiskOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskOption.to_json()

# convert the object into a dict
virtual_disk_option_dict = virtual_disk_option_instance.to_dict()
# create an instance of VirtualDiskOption from a dict
virtual_disk_option_form_dict = virtual_disk_option.from_dict(virtual_disk_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


