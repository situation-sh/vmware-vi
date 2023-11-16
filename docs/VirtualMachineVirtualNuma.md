# VirtualMachineVirtualNuma

This data object describes the virtual NUMA configuration for this virtual machine and configured through ConfigSpec. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores_per_numa_node** | **int** | Cores per vNUMA node for this VM.  The number of vNUMA nodes is calculated by total number of cores divided by corePerNumaNode. If set to be zero, it clears any manual override and autosize vNUMA node. If set to be non zero, VM uses the value as vNUMA node size. If unset, the VM continue to follow the behavior in last poweron.  | [optional] 
**expose_vnuma_on_cpu_hotadd** | **bool** | Capability to expose virtual NUMA when CPU hotadd is enabled.  If set to true, ESXi will consider exposing virtual NUMA to the VM when CPU hotadd is enabled. If set to false, ESXi will enforce the VM to have single virtual NUMA node when CPU hotadd is enabled. If unset, the VM continue to follow the behavior in last poweron.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_numa import VirtualMachineVirtualNuma

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualNuma from a JSON string
virtual_machine_virtual_numa_instance = VirtualMachineVirtualNuma.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualNuma.to_json()

# convert the object into a dict
virtual_machine_virtual_numa_dict = virtual_machine_virtual_numa_instance.to_dict()
# create an instance of VirtualMachineVirtualNuma from a dict
virtual_machine_virtual_numa_form_dict = virtual_machine_virtual_numa.from_dict(virtual_machine_virtual_numa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


