# HostHardwareSummary

This data object type summarizes hardware used by the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | The hardware vendor identification.  | 
**model** | **str** | The system model identification.  | 
**uuid** | **str** | The hardware BIOS identification.  | 
**other_identifying_info** | [**List[HostSystemIdentificationInfo]**](HostSystemIdentificationInfo.md) | Other identification information.  This information may be vendor specific.  ***Since:*** VI API 2.5  | [optional] 
**memory_size** | **int** | The physical memory size in bytes.  | 
**cpu_model** | **str** | The CPU model.  | 
**cpu_mhz** | **int** | The speed of the CPU cores.  This is an average value if there are multiple speeds. The product of cpuMhz and numCpuCores is approximately equal to the sum of the MHz for all the individual cores on the host.  | 
**num_cpu_pkgs** | **int** | Number of physical CPU packages on the host.  Physical CPU packages are chips that contain one or more processors. Processors contained by a package are also known as CPU cores. For example, one dual-core package is comprised of one chip that contains two CPU cores.  | 
**num_cpu_cores** | **int** | Number of physical CPU cores on the host.  Physical CPU cores are the processors contained by a CPU package.  | 
**num_cpu_threads** | **int** | Number of physical CPU threads on the host.  | 
**num_nics** | **int** | The number of network adapters.  | 
**num_hbas** | **int** | The number of host bus adapters (HBAs).  | 

## Example

```python
from vmware_vi.models.host_hardware_summary import HostHardwareSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HostHardwareSummary from a JSON string
host_hardware_summary_instance = HostHardwareSummary.from_json(json)
# print the JSON string representation of the object
print HostHardwareSummary.to_json()

# convert the object into a dict
host_hardware_summary_dict = host_hardware_summary_instance.to_dict()
# create an instance of HostHardwareSummary from a dict
host_hardware_summary_form_dict = host_hardware_summary.from_dict(host_hardware_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


