# HostVFlashManagerVFlashConfigInfo

vFlash configuration Information.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_resource_config_info** | [**HostVFlashManagerVFlashResourceConfigInfo**](HostVFlashManagerVFlashResourceConfigInfo.md) |  | [optional] 
**v_flash_cache_config_info** | [**HostVFlashManagerVFlashCacheConfigInfo**](HostVFlashManagerVFlashCacheConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_config_info import HostVFlashManagerVFlashConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashConfigInfo from a JSON string
host_v_flash_manager_v_flash_config_info_instance = HostVFlashManagerVFlashConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashConfigInfo.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_config_info_dict = host_v_flash_manager_v_flash_config_info_instance.to_dict()
# create an instance of HostVFlashManagerVFlashConfigInfo from a dict
host_v_flash_manager_v_flash_config_info_form_dict = host_v_flash_manager_v_flash_config_info.from_dict(host_v_flash_manager_v_flash_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


