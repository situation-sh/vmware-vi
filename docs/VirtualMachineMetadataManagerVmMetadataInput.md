# VirtualMachineMetadataManagerVmMetadataInput

VmMetadataInput specifies the operation and metadata for a specific VM.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The input operation type.  The values come from *VirtualMachineMetadataManagerVmMetadataOp_enum*  ***Since:*** vSphere API 5.5  | 
**vm_metadata** | [**VirtualMachineMetadataManagerVmMetadata**](VirtualMachineMetadataManagerVmMetadata.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_metadata_manager_vm_metadata_input import VirtualMachineMetadataManagerVmMetadataInput

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMetadataManagerVmMetadataInput from a JSON string
virtual_machine_metadata_manager_vm_metadata_input_instance = VirtualMachineMetadataManagerVmMetadataInput.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMetadataManagerVmMetadataInput.to_json()

# convert the object into a dict
virtual_machine_metadata_manager_vm_metadata_input_dict = virtual_machine_metadata_manager_vm_metadata_input_instance.to_dict()
# create an instance of VirtualMachineMetadataManagerVmMetadataInput from a dict
virtual_machine_metadata_manager_vm_metadata_input_form_dict = virtual_machine_metadata_manager_vm_metadata_input.from_dict(virtual_machine_metadata_manager_vm_metadata_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


