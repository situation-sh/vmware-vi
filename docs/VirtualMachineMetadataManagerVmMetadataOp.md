# VirtualMachineMetadataManagerVmMetadataOp

A boxed *VirtualMachineMetadataManagerVmMetadataOp_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineMetadataManagerVmMetadataOpEnum**](VirtualMachineMetadataManagerVmMetadataOpEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_metadata_manager_vm_metadata_op import VirtualMachineMetadataManagerVmMetadataOp

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMetadataManagerVmMetadataOp from a JSON string
virtual_machine_metadata_manager_vm_metadata_op_instance = VirtualMachineMetadataManagerVmMetadataOp.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMetadataManagerVmMetadataOp.to_json()

# convert the object into a dict
virtual_machine_metadata_manager_vm_metadata_op_dict = virtual_machine_metadata_manager_vm_metadata_op_instance.to_dict()
# create an instance of VirtualMachineMetadataManagerVmMetadataOp from a dict
virtual_machine_metadata_manager_vm_metadata_op_form_dict = virtual_machine_metadata_manager_vm_metadata_op.from_dict(virtual_machine_metadata_manager_vm_metadata_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


