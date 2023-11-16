# ArrayOfClusterComputeResourceHostVmkNicInfo

A boxed array of *ClusterComputeResourceHostVmkNicInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceHostVmkNicInfo]**](ClusterComputeResourceHostVmkNicInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_host_vmk_nic_info import ArrayOfClusterComputeResourceHostVmkNicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceHostVmkNicInfo from a JSON string
array_of_cluster_compute_resource_host_vmk_nic_info_instance = ArrayOfClusterComputeResourceHostVmkNicInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceHostVmkNicInfo.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_host_vmk_nic_info_dict = array_of_cluster_compute_resource_host_vmk_nic_info_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceHostVmkNicInfo from a dict
array_of_cluster_compute_resource_host_vmk_nic_info_form_dict = array_of_cluster_compute_resource_host_vmk_nic_info.from_dict(array_of_cluster_compute_resource_host_vmk_nic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


