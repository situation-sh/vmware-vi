# ClusterComputeResourceHostVmkNicInfo

This data object describes how a vmknic on a host must be configured.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_spec** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | 
**service** | **str** | Service type for this adapter.  See *HostVirtualNicManagerNicType_enum* for supported values.  ***Since:*** vSphere API 6.7.1  | 

## Example

```python
from vmware_vi.models.cluster_compute_resource_host_vmk_nic_info import ClusterComputeResourceHostVmkNicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHostVmkNicInfo from a JSON string
cluster_compute_resource_host_vmk_nic_info_instance = ClusterComputeResourceHostVmkNicInfo.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHostVmkNicInfo.to_json()

# convert the object into a dict
cluster_compute_resource_host_vmk_nic_info_dict = cluster_compute_resource_host_vmk_nic_info_instance.to_dict()
# create an instance of ClusterComputeResourceHostVmkNicInfo from a dict
cluster_compute_resource_host_vmk_nic_info_form_dict = cluster_compute_resource_host_vmk_nic_info.from_dict(cluster_compute_resource_host_vmk_nic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


