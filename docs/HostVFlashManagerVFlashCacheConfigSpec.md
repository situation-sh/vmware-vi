# HostVFlashManagerVFlashCacheConfigSpec

Specification to configure vFlash cache on the host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_v_flash_module** | **str** | Name of the default vFlash module for the read-write caches associated with the VMs of this host.  This setting can be overridden by *VirtualDiskVFlashCacheConfigInfo.vFlashModule* per VMDK.  ***Since:*** vSphere API 5.5  | 
**swap_cache_reservation_in_gb** | **int** | Amount of vFlash resource is allocated to the host swap cache.  As long as set, reservation will be permanent and retain regardless of host power state. The host swap cache will be disabled if the reservation is set to zero.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_cache_config_spec import HostVFlashManagerVFlashCacheConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashCacheConfigSpec from a JSON string
host_v_flash_manager_v_flash_cache_config_spec_instance = HostVFlashManagerVFlashCacheConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashCacheConfigSpec.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_cache_config_spec_dict = host_v_flash_manager_v_flash_cache_config_spec_instance.to_dict()
# create an instance of HostVFlashManagerVFlashCacheConfigSpec from a dict
host_v_flash_manager_v_flash_cache_config_spec_form_dict = host_v_flash_manager_v_flash_cache_config_spec.from_dict(host_v_flash_manager_v_flash_cache_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


