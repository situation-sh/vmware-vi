# ComputeResourceSummary

This data object type encapsulates a typical set of ComputeResource information that is useful for list views and summary pages. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cpu** | **int** | Aggregated CPU resources of all hosts, in MHz.  | 
**total_memory** | **int** | Aggregated memory resources of all hosts, in bytes.  | 
**num_cpu_cores** | **int** | Number of physical CPU cores.  Physical CPU cores are the processors contained by a CPU package.  | 
**num_cpu_threads** | **int** | Aggregated number of CPU threads.  | 
**effective_cpu** | **int** | Effective CPU resources (in MHz) available to run virtual machines.  This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.  | 
**effective_memory** | **int** | Effective memory resources (in MB) available to run virtual machines.  This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.  | 
**num_hosts** | **int** | Total number of hosts.  | 
**num_effective_hosts** | **int** | Total number of effective hosts.  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.compute_resource_summary import ComputeResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceSummary from a JSON string
compute_resource_summary_instance = ComputeResourceSummary.from_json(json)
# print the JSON string representation of the object
print ComputeResourceSummary.to_json()

# convert the object into a dict
compute_resource_summary_dict = compute_resource_summary_instance.to_dict()
# create an instance of ComputeResourceSummary from a dict
compute_resource_summary_form_dict = compute_resource_summary.from_dict(compute_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


