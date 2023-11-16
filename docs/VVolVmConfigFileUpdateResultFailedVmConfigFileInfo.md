# VVolVmConfigFileUpdateResultFailedVmConfigFileInfo

Information of the failed update on the virtual machine config file.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_config_v_vol_id** | **str** | The target virtual machine config VVol ID  ***Since:*** vSphere API 6.5  | 
**ds_path** | **str** | Datastore path for the virtual machine that failed to recover  ***Since:*** vSphere API 7.0  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.v_vol_vm_config_file_update_result_failed_vm_config_file_info import VVolVmConfigFileUpdateResultFailedVmConfigFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VVolVmConfigFileUpdateResultFailedVmConfigFileInfo from a JSON string
v_vol_vm_config_file_update_result_failed_vm_config_file_info_instance = VVolVmConfigFileUpdateResultFailedVmConfigFileInfo.from_json(json)
# print the JSON string representation of the object
print VVolVmConfigFileUpdateResultFailedVmConfigFileInfo.to_json()

# convert the object into a dict
v_vol_vm_config_file_update_result_failed_vm_config_file_info_dict = v_vol_vm_config_file_update_result_failed_vm_config_file_info_instance.to_dict()
# create an instance of VVolVmConfigFileUpdateResultFailedVmConfigFileInfo from a dict
v_vol_vm_config_file_update_result_failed_vm_config_file_info_form_dict = v_vol_vm_config_file_update_result_failed_vm_config_file_info.from_dict(v_vol_vm_config_file_update_result_failed_vm_config_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


