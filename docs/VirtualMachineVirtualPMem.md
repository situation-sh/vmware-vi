# VirtualMachineVirtualPMem

Virtual Persistent Memory configuration for the VM.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_mode** | **str** | An enum describing behavior of NVDIMM devices when a VM snapshot is taken and restored.  If unset, taking a VM snapshot will fail when the VM is configured with NVDIMMs. See *VirtualMachineVirtualPMemSnapshotMode_enum* for supported values. The snapshot mode applies to all NVDIMMs configured for the VM. Property is currently only applicable to VMs with virtual NVDIMMs and not applicable to vPMem disks. Setting this property will fail if the VM has existing snapshots.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_p_mem import VirtualMachineVirtualPMem

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualPMem from a JSON string
virtual_machine_virtual_p_mem_instance = VirtualMachineVirtualPMem.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualPMem.to_json()

# convert the object into a dict
virtual_machine_virtual_p_mem_dict = virtual_machine_virtual_p_mem_instance.to_dict()
# create an instance of VirtualMachineVirtualPMem from a dict
virtual_machine_virtual_p_mem_form_dict = virtual_machine_virtual_p_mem.from_dict(virtual_machine_virtual_p_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


