# HostVFlashManagerVFlashResourceRunTimeInfo

Data object provides vFlash resource runtime usage.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **int** | Overall usage of vFlash resource, in bytes.  ***Since:*** vSphere API 5.5  | 
**capacity** | **int** | Overall capacity of vFlash resource, in bytes.  ***Since:*** vSphere API 5.5  | 
**accessible** | **bool** | True if all the included the VFFS volumes are accessible.  False if one or multiple included VFFS volumes are inaccessible.  ***Since:*** vSphere API 5.5  | 
**capacity_for_vm_cache** | **int** | vFlash resource capacity can be allocated for VM caches  ***Since:*** vSphere API 5.5  | 
**free_for_vm_cache** | **int** | Free vFlash resource can be allocated for VM caches  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_resource_run_time_info import HostVFlashManagerVFlashResourceRunTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashResourceRunTimeInfo from a JSON string
host_v_flash_manager_v_flash_resource_run_time_info_instance = HostVFlashManagerVFlashResourceRunTimeInfo.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashResourceRunTimeInfo.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_resource_run_time_info_dict = host_v_flash_manager_v_flash_resource_run_time_info_instance.to_dict()
# create an instance of HostVFlashManagerVFlashResourceRunTimeInfo from a dict
host_v_flash_manager_v_flash_resource_run_time_info_form_dict = host_v_flash_manager_v_flash_resource_run_time_info.from_dict(host_v_flash_manager_v_flash_resource_run_time_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


