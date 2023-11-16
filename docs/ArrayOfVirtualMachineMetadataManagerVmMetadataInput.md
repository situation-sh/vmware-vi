# ArrayOfVirtualMachineMetadataManagerVmMetadataInput

A boxed array of *VirtualMachineMetadataManagerVmMetadataInput*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMetadataManagerVmMetadataInput]**](VirtualMachineMetadataManagerVmMetadataInput.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_metadata_manager_vm_metadata_input import ArrayOfVirtualMachineMetadataManagerVmMetadataInput

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataInput from a JSON string
array_of_virtual_machine_metadata_manager_vm_metadata_input_instance = ArrayOfVirtualMachineMetadataManagerVmMetadataInput.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMetadataManagerVmMetadataInput.to_json()

# convert the object into a dict
array_of_virtual_machine_metadata_manager_vm_metadata_input_dict = array_of_virtual_machine_metadata_manager_vm_metadata_input_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadataInput from a dict
array_of_virtual_machine_metadata_manager_vm_metadata_input_form_dict = array_of_virtual_machine_metadata_manager_vm_metadata_input.from_dict(array_of_virtual_machine_metadata_manager_vm_metadata_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


