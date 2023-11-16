# HostNumaInfo

Information about NUMA (non-uniform memory access). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Deprecated as of vSphere API 5.1, this property is always set to \&quot;NUMA\&quot;.  The type of NUMA technology.  | 
**num_nodes** | **int** | The number of NUMA nodes on the host.  The value is 0 if the host is not NUMA-capable.  | 
**numa_node** | [**List[HostNumaNode]**](HostNumaNode.md) | Information about each of the NUMA nodes on the host.  The array is empty if the host is not NUMA-capable.  | [optional] 

## Example

```python
from vmware_vi.models.host_numa_info import HostNumaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNumaInfo from a JSON string
host_numa_info_instance = HostNumaInfo.from_json(json)
# print the JSON string representation of the object
print HostNumaInfo.to_json()

# convert the object into a dict
host_numa_info_dict = host_numa_info_instance.to_dict()
# create an instance of HostNumaInfo from a dict
host_numa_info_form_dict = host_numa_info.from_dict(host_numa_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


