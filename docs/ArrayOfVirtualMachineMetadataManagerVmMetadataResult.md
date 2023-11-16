# ArrayOfVirtualMachineMetadataManagerVmMetadataResult

A boxed array of *VirtualMachineMetadataManagerVmMetadataResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMetadataManagerVmMetadataResult]**](VirtualMachineMetadataManagerVmMetadataResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_metadata_manager_vm_metadata_result import ArrayOfVirtualMachineMetadataManagerVmMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataResult from a JSON string
array_of_virtual_machine_metadata_manager_vm_metadata_result_instance = ArrayOfVirtualMachineMetadataManagerVmMetadataResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMetadataManagerVmMetadataResult.to_json()

# convert the object into a dict
array_of_virtual_machine_metadata_manager_vm_metadata_result_dict = array_of_virtual_machine_metadata_manager_vm_metadata_result_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataResult from a dict
array_of_virtual_machine_metadata_manager_vm_metadata_result_form_dict = array_of_virtual_machine_metadata_manager_vm_metadata_result.from_dict(array_of_virtual_machine_metadata_manager_vm_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


