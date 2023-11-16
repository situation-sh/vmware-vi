# VirtualMachineMetadataManagerVmMetadata

VmMetadata is a pair of VM ID and opaque metadata.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_id** | **str** | Datastore URL-based ID for VM, for example, \&quot;\\[datastore1\\] SomeVM/SomeVM.vmx\&quot;.  ***Since:*** vSphere API 5.5  | 
**metadata** | **str** | Opaque metadata for the VM identified by vmId.  If no value is supplied, the entry for this VM is removed.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_metadata_manager_vm_metadata import VirtualMachineMetadataManagerVmMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMetadataManagerVmMetadata from a JSON string
virtual_machine_metadata_manager_vm_metadata_instance = VirtualMachineMetadataManagerVmMetadata.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMetadataManagerVmMetadata.to_json()

# convert the object into a dict
virtual_machine_metadata_manager_vm_metadata_dict = virtual_machine_metadata_manager_vm_metadata_instance.to_dict()
# create an instance of VirtualMachineMetadataManagerVmMetadata from a dict
virtual_machine_metadata_manager_vm_metadata_form_dict = virtual_machine_metadata_manager_vm_metadata.from_dict(virtual_machine_metadata_manager_vm_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


