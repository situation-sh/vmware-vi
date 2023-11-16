# HostCpuInfo

Information about the CPUs. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cpu_packages** | **int** | Number of physical CPU packages on the host.  | 
**num_cpu_cores** | **int** | Number of physical CPU cores on the host.  | 
**num_cpu_threads** | **int** | Number of physical CPU threads on the host.  | 
**hz** | **int** | CPU speed per core.  This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as hz \\* numCpuCores  | 

## Example

```python
from vmware_vi.models.host_cpu_info import HostCpuInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostCpuInfo from a JSON string
host_cpu_info_instance = HostCpuInfo.from_json(json)
# print the JSON string representation of the object
print HostCpuInfo.to_json()

# convert the object into a dict
host_cpu_info_dict = host_cpu_info_instance.to_dict()
# create an instance of HostCpuInfo from a dict
host_cpu_info_form_dict = host_cpu_info.from_dict(host_cpu_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


