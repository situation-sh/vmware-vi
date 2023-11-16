# VirtualMachineMetadataManagerVmMetadataResult

A list of VmMetadataResults are returned for successful and non-successful results of an update or retrieve operation.  See also *VirtualMachineMetadataManager.UpdateMetadata*, *VirtualMachineMetadataManager.RetrieveMetadata*, *VirtualMachineMetadataManager.RetrieveAllMetadata*, *VirtualMachineMetadataManager.ClearMetadata*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_metadata** | [**VirtualMachineMetadataManagerVmMetadata**](VirtualMachineMetadataManagerVmMetadata.md) |  | 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_metadata_manager_vm_metadata_result import VirtualMachineMetadataManagerVmMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMetadataManagerVmMetadataResult from a JSON string
virtual_machine_metadata_manager_vm_metadata_result_instance = VirtualMachineMetadataManagerVmMetadataResult.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMetadataManagerVmMetadataResult.to_json()

# convert the object into a dict
virtual_machine_metadata_manager_vm_metadata_result_dict = virtual_machine_metadata_manager_vm_metadata_result_instance.to_dict()
# create an instance of VirtualMachineMetadataManagerVmMetadataResult from a dict
virtual_machine_metadata_manager_vm_metadata_result_form_dict = virtual_machine_metadata_manager_vm_metadata_result.from_dict(virtual_machine_metadata_manager_vm_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


