# UpdateVirtualMachineFilesResult

UpdateVirtualMachineFilesResult is the result returned to the *Datastore.UpdateVirtualMachineFiles_Task* method.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_vm_file** | [**List[UpdateVirtualMachineFilesResultFailedVmFileInfo]**](UpdateVirtualMachineFilesResultFailedVmFileInfo.md) | The list of virtual machines files the server has attempted to update but failed to update.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.update_virtual_machine_files_result import UpdateVirtualMachineFilesResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVirtualMachineFilesResult from a JSON string
update_virtual_machine_files_result_instance = UpdateVirtualMachineFilesResult.from_json(json)
# print the JSON string representation of the object
print UpdateVirtualMachineFilesResult.to_json()

# convert the object into a dict
update_virtual_machine_files_result_dict = update_virtual_machine_files_result_instance.to_dict()
# create an instance of UpdateVirtualMachineFilesResult from a dict
update_virtual_machine_files_result_form_dict = update_virtual_machine_files_result.from_dict(update_virtual_machine_files_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


