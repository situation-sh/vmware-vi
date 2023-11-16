# VmFaultToleranceTooManyVMsOnHost

This fault is returned when a host has more than the recommended number of Fault Tolerance VMs running on it.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** |  | [optional] 
**max_num_ft_vms** | **int** | The recommended number of Fault Tolerance VMs running on the host.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_too_many_vms_on_host import VmFaultToleranceTooManyVMsOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceTooManyVMsOnHost from a JSON string
vm_fault_tolerance_too_many_vms_on_host_instance = VmFaultToleranceTooManyVMsOnHost.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceTooManyVMsOnHost.to_json()

# convert the object into a dict
vm_fault_tolerance_too_many_vms_on_host_dict = vm_fault_tolerance_too_many_vms_on_host_instance.to_dict()
# create an instance of VmFaultToleranceTooManyVMsOnHost from a dict
vm_fault_tolerance_too_many_vms_on_host_form_dict = vm_fault_tolerance_too_many_vms_on_host.from_dict(vm_fault_tolerance_too_many_vms_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


