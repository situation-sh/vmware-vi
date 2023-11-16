# VirtualMachineVirtualNumaInfo

vNUMA: This is read-only data for ConfigInfo since this portion is not configurable. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores_per_numa_node** | **int** | Cores per NUMA node.  When this virtual machine is powered off and \&quot;autoCoresPerNumaNode\&quot; is True, coresPerNumaNode will be assigned during power-on and this field should be ignored. In other cases, this field represents the virtual NUMA node size seen by the guest.  | [optional] 
**auto_cores_per_numa_node** | **bool** | Whether coresPerNode is determined automatically.  | [optional] 
**vnuma_on_cpu_hotadd_exposed** | **bool** | Whether virtual NUMA topology is exposed when CPU hotadd is enabled.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_numa_info import VirtualMachineVirtualNumaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualNumaInfo from a JSON string
virtual_machine_virtual_numa_info_instance = VirtualMachineVirtualNumaInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualNumaInfo.to_json()

# convert the object into a dict
virtual_machine_virtual_numa_info_dict = virtual_machine_virtual_numa_info_instance.to_dict()
# create an instance of VirtualMachineVirtualNumaInfo from a dict
virtual_machine_virtual_numa_info_form_dict = virtual_machine_virtual_numa_info.from_dict(virtual_machine_virtual_numa_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


