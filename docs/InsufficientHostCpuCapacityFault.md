# InsufficientHostCpuCapacityFault

The host does not have enough CPU capacity for running the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreserved** | **int** | The CPU available on the host in MHz.  ***Since:*** vSphere API 4.0  | 
**requested** | **int** | The CPU resource amount requested in the failed operation in MHz.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.insufficient_host_cpu_capacity_fault import InsufficientHostCpuCapacityFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientHostCpuCapacityFault from a JSON string
insufficient_host_cpu_capacity_fault_instance = InsufficientHostCpuCapacityFault.from_json(json)
# print the JSON string representation of the object
print InsufficientHostCpuCapacityFault.to_json()

# convert the object into a dict
insufficient_host_cpu_capacity_fault_dict = insufficient_host_cpu_capacity_fault_instance.to_dict()
# create an instance of InsufficientHostCpuCapacityFault from a dict
insufficient_host_cpu_capacity_fault_form_dict = insufficient_host_cpu_capacity_fault.from_dict(insufficient_host_cpu_capacity_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


