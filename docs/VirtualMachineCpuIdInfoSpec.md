# VirtualMachineCpuIdInfoSpec

Wrapper class to support incremental updates of the cpuFeatureMask.  As of vSphere API 6.5 *VirtualMachineConfigSpec.extraConfig* is the recommended method for setting the mask for a virtual machine with hardware version 9 and above (newer). They can be viewed via *featureMask*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**HostCpuIdInfo**](HostCpuIdInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_cpu_id_info_spec import VirtualMachineCpuIdInfoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCpuIdInfoSpec from a JSON string
virtual_machine_cpu_id_info_spec_instance = VirtualMachineCpuIdInfoSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCpuIdInfoSpec.to_json()

# convert the object into a dict
virtual_machine_cpu_id_info_spec_dict = virtual_machine_cpu_id_info_spec_instance.to_dict()
# create an instance of VirtualMachineCpuIdInfoSpec from a dict
virtual_machine_cpu_id_info_spec_form_dict = virtual_machine_cpu_id_info_spec.from_dict(virtual_machine_cpu_id_info_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


