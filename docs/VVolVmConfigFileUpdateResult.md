# VVolVmConfigFileUpdateResult

VVolVmConfigFileUpdateResult is the result returned by the *Datastore.UpdateVVolVirtualMachineFiles_Task* method.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded_vm_config_file** | [**List[KeyValue]**](KeyValue.md) | Mapping of target config VVol IDs to the target virtual machine config file paths which are successfully updated.  ***Since:*** vSphere API 6.5  | [optional] 
**failed_vm_config_file** | [**List[VVolVmConfigFileUpdateResultFailedVmConfigFileInfo]**](VVolVmConfigFileUpdateResultFailedVmConfigFileInfo.md) | The list of virtual machines config files the server has attempted, but failed to update.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.v_vol_vm_config_file_update_result import VVolVmConfigFileUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of VVolVmConfigFileUpdateResult from a JSON string
v_vol_vm_config_file_update_result_instance = VVolVmConfigFileUpdateResult.from_json(json)
# print the JSON string representation of the object
print VVolVmConfigFileUpdateResult.to_json()

# convert the object into a dict
v_vol_vm_config_file_update_result_dict = v_vol_vm_config_file_update_result_instance.to_dict()
# create an instance of VVolVmConfigFileUpdateResult from a dict
v_vol_vm_config_file_update_result_form_dict = v_vol_vm_config_file_update_result.from_dict(v_vol_vm_config_file_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


