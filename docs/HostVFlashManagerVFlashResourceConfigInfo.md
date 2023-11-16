# HostVFlashManagerVFlashResourceConfigInfo

vFlash resource configuration Information.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs** | [**HostVffsVolume**](HostVffsVolume.md) |  | [optional] 
**capacity** | **int** | Capacity of the vFlash resource.  It is the capacity of the contained VFFS volume.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_resource_config_info import HostVFlashManagerVFlashResourceConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashResourceConfigInfo from a JSON string
host_v_flash_manager_v_flash_resource_config_info_instance = HostVFlashManagerVFlashResourceConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashResourceConfigInfo.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_resource_config_info_dict = host_v_flash_manager_v_flash_resource_config_info_instance.to_dict()
# create an instance of HostVFlashManagerVFlashResourceConfigInfo from a dict
host_v_flash_manager_v_flash_resource_config_info_form_dict = host_v_flash_manager_v_flash_resource_config_info.from_dict(host_v_flash_manager_v_flash_resource_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


