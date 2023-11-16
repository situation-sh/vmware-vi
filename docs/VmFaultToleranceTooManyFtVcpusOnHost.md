# VmFaultToleranceTooManyFtVcpusOnHost

This fault is returned when a host has more than the recommended number of Fault Tolerance vCPUs running on it.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host  ***Since:*** vSphere API 6.0  | [optional] 
**max_num_ft_vcpus** | **int** | The recommended number of FT protected vCPUs on a host.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_too_many_ft_vcpus_on_host import VmFaultToleranceTooManyFtVcpusOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceTooManyFtVcpusOnHost from a JSON string
vm_fault_tolerance_too_many_ft_vcpus_on_host_instance = VmFaultToleranceTooManyFtVcpusOnHost.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceTooManyFtVcpusOnHost.to_json()

# convert the object into a dict
vm_fault_tolerance_too_many_ft_vcpus_on_host_dict = vm_fault_tolerance_too_many_ft_vcpus_on_host_instance.to_dict()
# create an instance of VmFaultToleranceTooManyFtVcpusOnHost from a dict
vm_fault_tolerance_too_many_ft_vcpus_on_host_form_dict = vm_fault_tolerance_too_many_ft_vcpus_on_host.from_dict(vm_fault_tolerance_too_many_ft_vcpus_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


