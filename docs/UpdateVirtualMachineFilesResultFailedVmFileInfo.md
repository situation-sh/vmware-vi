# UpdateVirtualMachineFilesResultFailedVmFileInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_file** | **str** | The file path  ***Since:*** vSphere API 4.1  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.update_virtual_machine_files_result_failed_vm_file_info import UpdateVirtualMachineFilesResultFailedVmFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVirtualMachineFilesResultFailedVmFileInfo from a JSON string
update_virtual_machine_files_result_failed_vm_file_info_instance = UpdateVirtualMachineFilesResultFailedVmFileInfo.from_json(json)
# print the JSON string representation of the object
print UpdateVirtualMachineFilesResultFailedVmFileInfo.to_json()

# convert the object into a dict
update_virtual_machine_files_result_failed_vm_file_info_dict = update_virtual_machine_files_result_failed_vm_file_info_instance.to_dict()
# create an instance of UpdateVirtualMachineFilesResultFailedVmFileInfo from a dict
update_virtual_machine_files_result_failed_vm_file_info_form_dict = update_virtual_machine_files_result_failed_vm_file_info.from_dict(update_virtual_machine_files_result_failed_vm_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


