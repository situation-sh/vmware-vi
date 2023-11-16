# QueryMemoryOverheadRequestType

The parameters of *HostSystem.QueryMemoryOverhead*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_size** | **int** | The amount of virtual system RAM, in bytes. For an existing virtual machine, this value can be found (in megabytes) as the memoryMB property of the *VirtualHardware*.  | 
**video_ram_size** | **int** | The amount of virtual video RAM, in bytes. For an existing virtual machine on a host that supports advertising this property, this value can be found (in kilobytes) as the videoRamSizeInKB property of the *VirtualMachineVideoCard*. If this parameter is left unset, the default video RAM size for virtual machines on this host is assumed.  | [optional] 
**num_vcpus** | **int** | The number of virtual CPUs. For an existing virtual machine, this value can be found as the numCPU property of the *VirtualHardware*.  | 

## Example

```python
from vmware_vi.models.query_memory_overhead_request_type import QueryMemoryOverheadRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMemoryOverheadRequestType from a JSON string
query_memory_overhead_request_type_instance = QueryMemoryOverheadRequestType.from_json(json)
# print the JSON string representation of the object
print QueryMemoryOverheadRequestType.to_json()

# convert the object into a dict
query_memory_overhead_request_type_dict = query_memory_overhead_request_type_instance.to_dict()
# create an instance of QueryMemoryOverheadRequestType from a dict
query_memory_overhead_request_type_form_dict = query_memory_overhead_request_type.from_dict(query_memory_overhead_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


