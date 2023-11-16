# HostNumaNode

Information about a single NUMA node. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Zero-based NUMA ID for the node.  | 
**cpu_id** | **List[int]** | Information about each of the CPUs associated with the node.  | 
**memory_size** | **int** | The total amount of memory in this NUMA node, in bytes.  | [optional] 
**memory_range_begin** | **int** | Deprecated as of vSphere 8.0, this property is always set to zero. The memory of a NUMA node is not necessarily a single physically contiguous range.  Beginning memory range for this NUMA node.  | 
**memory_range_length** | **int** | Deprecated as of vSphere 8.0, this property is replaced by *HostNumaNode.memorySize* and is set to the same value. The memory of a NUMA node is not necessarily a single physically contiguous range.  Length of the memory range for this node in bytes, that is, the amount of memory on the node.  | 
**pci_id** | **List[str]** | Information about each of the pci devices associated with the node.  The string is of SBDF format, \&quot;Segment:Bus:Device.Function\&quot;.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_numa_node import HostNumaNode

# TODO update the JSON string below
json = "{}"
# create an instance of HostNumaNode from a JSON string
host_numa_node_instance = HostNumaNode.from_json(json)
# print the JSON string representation of the object
print HostNumaNode.to_json()

# convert the object into a dict
host_numa_node_dict = host_numa_node_instance.to_dict()
# create an instance of HostNumaNode from a dict
host_numa_node_form_dict = host_numa_node.from_dict(host_numa_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


