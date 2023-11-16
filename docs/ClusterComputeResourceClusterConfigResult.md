# ClusterComputeResourceClusterConfigResult

ClusterConfigResult is the result returned for the *ClusterComputeResource.ConfigureHCI_Task* method.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_hosts** | [**List[FolderFailedHostResult]**](FolderFailedHostResult.md) | List of failed hosts.  ***Since:*** vSphere API 6.7.1  | [optional] 
**configured_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of successfully configured hosts.  ***Since:*** vSphere API 6.7.1  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_cluster_config_result import ClusterComputeResourceClusterConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceClusterConfigResult from a JSON string
cluster_compute_resource_cluster_config_result_instance = ClusterComputeResourceClusterConfigResult.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceClusterConfigResult.to_json()

# convert the object into a dict
cluster_compute_resource_cluster_config_result_dict = cluster_compute_resource_cluster_config_result_instance.to_dict()
# create an instance of ClusterComputeResourceClusterConfigResult from a dict
cluster_compute_resource_cluster_config_result_form_dict = cluster_compute_resource_cluster_config_result.from_dict(cluster_compute_resource_cluster_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


