# VirtualMachineConfigInfoOverheadInfo

Information about virtualization overhead required to power on the virtual machine on the registered host.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_memory_reservation** | **int** | Memory overhead required for virtual machine to be powered on (in bytes).  ***Since:*** vSphere API 5.0  | [optional] 
**initial_swap_reservation** | **int** | Disk space required for virtual machine to be powered on (in bytes).  This space is used by virtualization infrastructure to swap out virtual machine process memory. Location of the file is specified by sched.swap.vmxSwapDir virtual machinge advanced config option or in case it is not specified - current virtual machine home directory is being used.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_config_info_overhead_info import VirtualMachineConfigInfoOverheadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigInfoOverheadInfo from a JSON string
virtual_machine_config_info_overhead_info_instance = VirtualMachineConfigInfoOverheadInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigInfoOverheadInfo.to_json()

# convert the object into a dict
virtual_machine_config_info_overhead_info_dict = virtual_machine_config_info_overhead_info_instance.to_dict()
# create an instance of VirtualMachineConfigInfoOverheadInfo from a dict
virtual_machine_config_info_overhead_info_form_dict = virtual_machine_config_info_overhead_info.from_dict(virtual_machine_config_info_overhead_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


