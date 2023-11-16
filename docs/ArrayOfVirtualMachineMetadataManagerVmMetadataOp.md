# ArrayOfVirtualMachineMetadataManagerVmMetadataOp

A boxed array of *VirtualMachineMetadataManagerVmMetadataOp_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMetadataManagerVmMetadataOpEnum]**](VirtualMachineMetadataManagerVmMetadataOpEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_metadata_manager_vm_metadata_op import ArrayOfVirtualMachineMetadataManagerVmMetadataOp

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataOp from a JSON string
array_of_virtual_machine_metadata_manager_vm_metadata_op_instance = ArrayOfVirtualMachineMetadataManagerVmMetadataOp.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMetadataManagerVmMetadataOp.to_json()

# convert the object into a dict
array_of_virtual_machine_metadata_manager_vm_metadata_op_dict = array_of_virtual_machine_metadata_manager_vm_metadata_op_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataOp from a dict
array_of_virtual_machine_metadata_manager_vm_metadata_op_form_dict = array_of_virtual_machine_metadata_manager_vm_metadata_op.from_dict(array_of_virtual_machine_metadata_manager_vm_metadata_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


