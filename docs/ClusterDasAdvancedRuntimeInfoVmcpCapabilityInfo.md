# ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo

Class for capability to support VM Component Protection  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_apd_supported** | **bool** | If all hosts in the cluster support the reaction of VM Component Protection to storage All Paths Down timeout (@link vim.host.MountInfo.InaccessibleReason#AllPathsDown\\_Timeout}  ***Since:*** vSphere API 6.0  | 
**storage_pdl_supported** | **bool** | If all hosts in the cluster support the reaction of VM Component Protection to storage Permanent Device Loss (@link vim.host.MountInfo.InaccessibleReason#PermanentDeviceLoss}  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.cluster_das_advanced_runtime_info_vmcp_capability_info import ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo from a JSON string
cluster_das_advanced_runtime_info_vmcp_capability_info_instance = ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo.to_json()

# convert the object into a dict
cluster_das_advanced_runtime_info_vmcp_capability_info_dict = cluster_das_advanced_runtime_info_vmcp_capability_info_instance.to_dict()
# create an instance of ClusterDasAdvancedRuntimeInfoVmcpCapabilityInfo from a dict
cluster_das_advanced_runtime_info_vmcp_capability_info_form_dict = cluster_das_advanced_runtime_info_vmcp_capability_info.from_dict(cluster_das_advanced_runtime_info_vmcp_capability_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


