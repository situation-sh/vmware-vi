# VirtualMachinePciSharedGpuPassthroughInfo

Description of a gpu PCI device that can be shared with a virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vgpu** | **str** | The VGPU corresponding to this GPU passthrough device.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_pci_shared_gpu_passthrough_info import VirtualMachinePciSharedGpuPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachinePciSharedGpuPassthroughInfo from a JSON string
virtual_machine_pci_shared_gpu_passthrough_info_instance = VirtualMachinePciSharedGpuPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachinePciSharedGpuPassthroughInfo.to_json()

# convert the object into a dict
virtual_machine_pci_shared_gpu_passthrough_info_dict = virtual_machine_pci_shared_gpu_passthrough_info_instance.to_dict()
# create an instance of VirtualMachinePciSharedGpuPassthroughInfo from a dict
virtual_machine_pci_shared_gpu_passthrough_info_form_dict = virtual_machine_pci_shared_gpu_passthrough_info.from_dict(virtual_machine_pci_shared_gpu_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


