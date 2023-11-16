# ArrayOfVirtualMachineMetadataManagerVmMetadata

A boxed array of *VirtualMachineMetadataManagerVmMetadata*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineMetadataManagerVmMetadata]**](VirtualMachineMetadataManagerVmMetadata.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_metadata_manager_vm_metadata import ArrayOfVirtualMachineMetadataManagerVmMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadata from a JSON string
array_of_virtual_machine_metadata_manager_vm_metadata_instance = ArrayOfVirtualMachineMetadataManagerVmMetadata.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineMetadataManagerVmMetadata.to_json()

# convert the object into a dict
array_of_virtual_machine_metadata_manager_vm_metadata_dict = array_of_virtual_machine_metadata_manager_vm_metadata_instance.to_dict()
# create an instance of ArrayOfVirtualMachineMetadataManagerVmMetadata from a dict
array_of_virtual_machine_metadata_manager_vm_metadata_form_dict = array_of_virtual_machine_metadata_manager_vm_metadata.from_dict(array_of_virtual_machine_metadata_manager_vm_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


