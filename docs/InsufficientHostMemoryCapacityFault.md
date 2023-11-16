# InsufficientHostMemoryCapacityFault

The host does not have enough memory capacity for running the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreserved** | **int** | The memory available on the host in bytes.  ***Since:*** vSphere API 4.0  | 
**requested** | **int** | The memory resource amount requested in the failed operation in bytes.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.insufficient_host_memory_capacity_fault import InsufficientHostMemoryCapacityFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientHostMemoryCapacityFault from a JSON string
insufficient_host_memory_capacity_fault_instance = InsufficientHostMemoryCapacityFault.from_json(json)
# print the JSON string representation of the object
print InsufficientHostMemoryCapacityFault.to_json()

# convert the object into a dict
insufficient_host_memory_capacity_fault_dict = insufficient_host_memory_capacity_fault_instance.to_dict()
# create an instance of InsufficientHostMemoryCapacityFault from a dict
insufficient_host_memory_capacity_fault_form_dict = insufficient_host_memory_capacity_fault.from_dict(insufficient_host_memory_capacity_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


